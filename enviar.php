<?php
/* ============================================================
   Recepción del formulario de contacto — MCG
   Envía por correo los datos que la persona completó en la web.
   Requiere un hosting con PHP (BanaHosting, cPanel, etc.).
   Si el sitio se aloja en un hosting estático, este archivo no
   se ejecuta y el formulario vuelve solo al envío por WhatsApp.
   ------------------------------------------------------------
   Para cambiar la casilla que recibe los avisos, editar
   $DESTINO más abajo.
   ============================================================ */

$DESTINO = "mcgestudioc@gmail.com";
$ASUNTO_BASE = "Nueva consulta desde la web";

header("Content-Type: application/json; charset=utf-8");

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    echo json_encode(["ok" => false, "error" => "metodo_no_permitido"]);
    exit;
}

/* Trampa anti-spam: los robots completan este campo oculto. */
if (!empty($_POST["sitioWeb"])) {
    echo json_encode(["ok" => true]); // fingimos éxito y descartamos
    exit;
}

function limpio($clave, $max = 400) {
    if (!isset($_POST[$clave])) return "";
    $v = trim((string) $_POST[$clave]);
    $v = str_replace(["\r", "\n", "%0a", "%0d"], " ", $v);
    $v = strip_tags($v);
    return mb_substr($v, 0, $max);
}

function limpio_largo($clave, $max = 3000) {
    if (!isset($_POST[$clave])) return "";
    $v = trim((string) $_POST[$clave]);
    $v = strip_tags($v);
    return mb_substr($v, 0, $max);
}

$nombre   = limpio("nombre", 120);
$empresa  = limpio("empresa", 160);
$correo   = limpio("correoContacto", 160);
$whatsapp = limpio("whatsappContacto", 60);
$servicio = limpio("servicio", 120);
$situacion = limpio("situacionGeneral", 60);
$idioma   = limpio("idioma", 10);

if ($nombre === "" || $correo === "" || !filter_var($correo, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(["ok" => false, "error" => "datos_incompletos"]);
    exit;
}

$lineas = [];
$lineas[] = "Nombre: " . $nombre;
$lineas[] = "Empresa o proyecto: " . ($empresa !== "" ? $empresa : "-");
$lineas[] = "Correo: " . $correo;
$lineas[] = "WhatsApp: " . ($whatsapp !== "" ? $whatsapp : "-");
$lineas[] = "Servicio de interés: " . ($servicio !== "" ? $servicio : "-");
$lineas[] = "Situación: " . ($situacion !== "" ? $situacion : "-");

if ($situacion === "empresa") {
    $lineas[] = "";
    $lineas[] = "— Empresa existente —";
    $lineas[] = "Rubro: " . (limpio("rubro", 160) ?: "-");
    $lineas[] = "Facturación mensual aproximada: " . (limpio("facturacion", 120) ?: "-");
    $lineas[] = "Principal necesidad: " . (limpio_largo("necesidadEmpresa") ?: "-");
} elseif ($situacion === "extranjero") {
    $lineas[] = "";
    $lineas[] = "— Proyecto de extranjero/inversionista —";
    $lineas[] = "País de residencia: " . (limpio("paisResidencia", 120) ?: "-");
    $lineas[] = "Tipo de proyecto: " . (limpio("tipoProyecto", 160) ?: "-");
    $lineas[] = "Etapa del proyecto: " . (limpio("etapaProyecto", 160) ?: "-");
    $lineas[] = "Principal necesidad: " . (limpio_largo("necesidadExtranjero") ?: "-");
}

$lineas[] = "";
$lineas[] = "— Datos del envío —";
$lineas[] = "Idioma de la página: " . ($idioma !== "" ? $idioma : "es");
$lineas[] = "Página de origen: " . limpio("origen", 300);
$lineas[] = "Fecha: " . date("d/m/Y H:i");

$cuerpo = implode("\n", $lineas);
$asunto = $ASUNTO_BASE . " — " . $nombre;

$remitenteDominio = isset($_SERVER["HTTP_HOST"]) ? preg_replace('/[^a-zA-Z0-9\.\-]/', '', $_SERVER["HTTP_HOST"]) : "localhost";
$cabeceras  = "From: Web MCG <no-reply@" . $remitenteDominio . ">\r\n";
$cabeceras .= "Reply-To: " . $correo . "\r\n";
$cabeceras .= "Content-Type: text/plain; charset=UTF-8\r\n";
$cabeceras .= "MIME-Version: 1.0\r\n";

$enviado = @mail($DESTINO, "=?UTF-8?B?" . base64_encode($asunto) . "?=", $cuerpo, $cabeceras);

if ($enviado) {
    echo json_encode(["ok" => true]);
} else {
    http_response_code(500);
    echo json_encode(["ok" => false, "error" => "envio_fallido"]);
}
