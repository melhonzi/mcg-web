/* ============================================================
   MCG — ayudante del formulario de contacto
   ------------------------------------------------------------
   Esto vive DENTRO de la cuenta de Google de MCG (Google Apps
   Script). El sitio está en GitHub, que solo sabe MOSTRAR
   páginas: no sabe mandar un correo. Este ayudante es el que
   hace ese trabajo.

   Cada vez que alguien completa el formulario de la web:
     1. guarda la consulta en una planilla (por si un correo se
        traspapela, la consulta igual queda anotada);
     2. manda el correo a MCG, con "responder" apuntando a la
        persona que escribió;
     3. avisa por WhatsApp (si está cargada la llave de CallMeBot).

   El orden importa: primero se guarda. Si fallara el correo o el
   WhatsApp, la consulta ya está a salvo en la planilla.

   CÓMO SE PUBLICA: ver build/FORMULARIO.md
   ============================================================ */

/* ---------- lo único que se toca ---------- */

// A dónde llega el correo. Para mandar a dos casillas, separalas
// con coma: "una@gmail.com,otra@gmail.com"
var DESTINO = 'mcgestudioc@gmail.com';

// WhatsApp que recibe el aviso, solo números y con el código de país.
var WHATSAPP_NUMERO = '595981579250';

// Llave de CallMeBot (ver build/FORMULARIO.md, paso 5).
// Si queda vacía, no se manda WhatsApp y todo lo demás sigue igual.
var CALLMEBOT_APIKEY = '';

// Nombre de la planilla donde se anotan las consultas. Si no existe,
// se crea sola la primera vez.
var NOMBRE_PLANILLA = 'MCG — consultas de la web';

// Techo de correos por hora. Es un freno contra un robot que quiera
// inundar la casilla. Pasado el techo la consulta SE SIGUE GUARDANDO
// en la planilla; lo único que no sale es el correo.
var TECHO_POR_HORA = 40;

/* ---------- de acá para abajo no hace falta tocar nada ---------- */

var CAMPOS = [
  ['nombre', 'Nombre'],
  ['empresa', 'Empresa o proyecto'],
  ['correoContacto', 'Correo'],
  ['whatsappContacto', 'WhatsApp'],
  ['servicio', 'Servicio de interés'],
  ['situacionGeneral', 'Situación'],
  ['rubro', 'Rubro'],
  ['facturacion', 'Facturación mensual aproximada'],
  ['necesidadEmpresa', 'Principal necesidad'],
  ['paisResidencia', 'País de residencia'],
  ['tipoProyecto', 'Tipo de proyecto'],
  ['etapaProyecto', 'Etapa del proyecto'],
  ['necesidadExtranjero', 'Principal necesidad'],
  ['idioma', 'Idioma de la página'],
  ['origen', 'Página de origen']
];

var ENCABEZADOS = ['Fecha'].concat(CAMPOS.map(function (c) { return c[1]; }))
  .concat(['Correo enviado', 'WhatsApp enviado']);


/** Abrir la dirección del ayudante en el navegador contesta esto.
 *  Sirve para comprobar de un vistazo que está publicado y vivo. */
function doGet() {
  return json({
    ok: true,
    mensaje: 'Ayudante del formulario de MCG funcionando.',
    destino: DESTINO,
    whatsapp: CALLMEBOT_APIKEY ? 'configurado' : 'sin configurar'
  });
}


function doPost(e) {
  try {
    var p = (e && e.parameter) || {};

    // Trampa anti-robot: es un campo escondido que una persona nunca
    // ve ni completa. Si viene lleno, es un robot: le decimos que sí
    // y tiramos la consulta a la basura, sin avisar y sin guardar.
    if (String(p.sitioWeb || '').trim() !== '') return json({ ok: true });

    var nombre = limpio(p.nombre, 120);
    var correo = limpio(p.correoContacto, 160);
    if (!nombre || !correoValido(correo)) {
      return json({ ok: false, error: 'datos_incompletos' });
    }

    var fila = [new Date()];
    CAMPOS.forEach(function (c) { fila.push(limpio(p[c[0]], 3000)); });

    var dentroDelTecho = pedirTurno();
    var correoOk = dentroDelTecho ? mandarCorreo(nombre, correo, p) : false;
    var waOk = (dentroDelTecho && CALLMEBOT_APIKEY) ? mandarWhatsapp(nombre, p) : false;

    guardarEnPlanilla(fila.concat([correoOk ? 'sí' : 'no', waOk ? 'sí' : 'no']));

    // Se contesta ok si la consulta quedó guardada, aunque el correo
    // haya fallado: la consulta no se perdió, y así la persona no ve
    // un error por algo que ya está resuelto de nuestro lado.
    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  }
}


/* ---------- guardar ---------- */

function planilla() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty('planillaId');
  if (id) {
    try { return SpreadsheetApp.openById(id); } catch (err) { /* se borró: la rehacemos */ }
  }
  var ss = SpreadsheetApp.create(NOMBRE_PLANILLA);
  ss.getActiveSheet().appendRow(ENCABEZADOS);
  ss.getActiveSheet().setFrozenRows(1);
  props.setProperty('planillaId', ss.getId());
  return ss;
}

function guardarEnPlanilla(fila) {
  // El candado evita que dos consultas que llegan en el mismo segundo
  // se pisen y una termine escrita arriba de la otra.
  var candado = LockService.getScriptLock();
  try {
    candado.waitLock(20000);
    planilla().getActiveSheet().appendRow(fila);
  } finally {
    try { candado.releaseLock(); } catch (err) { /* nada */ }
  }
}


/* ---------- correo ---------- */

function mandarCorreo(nombre, correo, p) {
  var l = [];
  var situacion = limpio(p.situacionGeneral, 60);
  CAMPOS.forEach(function (c) {
    var v = limpio(p[c[0]], 3000);
    if (!v) return;
    // Los campos de empresa no se mezclan con los de extranjero.
    if (situacion === 'extranjero' && ['rubro', 'facturacion', 'necesidadEmpresa'].indexOf(c[0]) >= 0) return;
    if (situacion === 'empresa' && ['paisResidencia', 'tipoProyecto', 'etapaProyecto', 'necesidadExtranjero'].indexOf(c[0]) >= 0) return;
    l.push(c[1] + ': ' + v);
  });
  l.push('');
  l.push('Fecha: ' + Utilities.formatDate(new Date(), 'America/Asuncion', 'dd/MM/yyyy HH:mm'));
  l.push('Para responderle, contestá este mismo correo.');

  try {
    MailApp.sendEmail({
      to: DESTINO,
      replyTo: correo,
      name: 'Web MCG',
      subject: 'Nueva consulta desde la web — ' + nombre,
      body: l.join('\n')
    });
    return true;
  } catch (err) {
    return false;
  }
}


/* ---------- WhatsApp ---------- */

function mandarWhatsapp(nombre, p) {
  var t = 'Nueva consulta en la web de MCG\n'
        + 'Nombre: ' + nombre + '\n'
        + 'Correo: ' + limpio(p.correoContacto, 160) + '\n'
        + 'WhatsApp: ' + (limpio(p.whatsappContacto, 60) || '-') + '\n'
        + 'Servicio: ' + (limpio(p.servicio, 120) || '-') + '\n'
        + 'El detalle completo está en el correo y en la planilla.';
  var url = 'https://api.callmebot.com/whatsapp.php'
          + '?phone=' + encodeURIComponent(WHATSAPP_NUMERO)
          + '&apikey=' + encodeURIComponent(CALLMEBOT_APIKEY)
          + '&text=' + encodeURIComponent(t);
  try {
    // muteHttpExceptions: si CallMeBot está caído, queremos seguir de
    // largo, no que reviente y se pierda el guardado en la planilla.
    var r = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
    return r.getResponseCode() === 200;
  } catch (err) {
    return false;
  }
}


/* ---------- ayudas ---------- */

function pedirTurno() {
  var props = PropertiesService.getScriptProperties();
  var horaActual = Utilities.formatDate(new Date(), 'UTC', 'yyyyMMddHH');
  var guardado = (props.getProperty('contador') || '').split(':');
  var n = (guardado[0] === horaActual) ? (parseInt(guardado[1], 10) || 0) : 0;
  if (n >= TECHO_POR_HORA) return false;
  props.setProperty('contador', horaActual + ':' + (n + 1));
  return true;
}

function limpio(v, max) {
  if (v === undefined || v === null) return '';
  return String(v).replace(/[\r\n]+/g, ' ').trim().slice(0, max);
}

function correoValido(v) {
  return /^[^@\s]+@[^@\s.]+\.[^@\s]+$/.test(v);
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
