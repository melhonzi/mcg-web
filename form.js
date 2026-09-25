/* ============================================================
   Formulario de contacto — MCG
   No hay backend/CRM conectado en esta vista previa. Alternativa
   honesta: armamos el mensaje con lo que la persona completó y
   lo dejamos listo para enviar por WhatsApp. Nunca mostramos un
   "enviado con éxito" falso: el envío real lo hace la persona
   dentro de WhatsApp.
   ============================================================ */

(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("formContacto");
    if (!form) return;

    var situacionSel = document.getElementById("situacion");
    var bloqueEmpresa = document.getElementById("bloqueEmpresa");
    var bloqueExtranjero = document.getElementById("bloqueExtranjero");
    var mensajeBox = document.getElementById("formMensaje");
    var linkWa = document.getElementById("linkWhatsappManual");

    function actualizarBloques() {
      var val = situacionSel.value;
      bloqueEmpresa.classList.toggle("paso-tab", true);
      bloqueExtranjero.classList.toggle("paso-tab", true);
      bloqueEmpresa.classList.toggle("activo", val === "empresa");
      bloqueExtranjero.classList.toggle("activo", val === "extranjero");
      // Los campos ocultos no deben bloquear el envío por "required"
      toggleRequired(bloqueEmpresa, val === "empresa");
      toggleRequired(bloqueExtranjero, val === "extranjero");
    }

    function toggleRequired(contenedor, activo) {
      contenedor.querySelectorAll("[data-obligatorio]").forEach(function (campo) {
        if (activo) campo.setAttribute("required", "required");
        else campo.removeAttribute("required");
      });
    }

    if (situacionSel) {
      situacionSel.addEventListener("change", actualizarBloques);
      actualizarBloques();
    }

    function valorRadio(nombre) {
      var el = form.querySelector('input[name="' + nombre + '"]:checked');
      return el ? el.value : "";
    }

    function armarMensaje() {
      var l = [];
      l.push(window.MCG_WA_SALUDO || "Hola MCG, vengo de la página web y quiero hacer una consulta.");
      l.push("");
      l.push("Nombre: " + (form.nombre.value || "-"));
      l.push("Empresa o proyecto: " + (form.empresa.value || "-"));
      l.push("Correo: " + (form.correoContacto.value || "-"));
      l.push("WhatsApp: " + (form.whatsappContacto.value || "-"));
      l.push("Servicio de interés: " + (form.servicio.value || "-"));

      var situacion = situacionSel ? situacionSel.value : "";
      if (situacion === "empresa") {
        l.push("");
        l.push("— Empresa existente —");
        l.push("Rubro: " + (form.rubro.value || "-"));
        l.push("Facturación mensual aproximada: " + (valorRadio("facturacion") || "-"));
        l.push("Principal necesidad: " + (form.necesidadEmpresa.value || "-"));
      } else if (situacion === "extranjero") {
        l.push("");
        l.push("— Proyecto de extranjero/inversionista —");
        l.push("País de residencia: " + (form.paisResidencia.value || "-"));
        l.push("Tipo de proyecto: " + (form.tipoProyecto.value || "-"));
        l.push("Etapa del proyecto: " + (form.etapaProyecto.value || "-"));
        l.push("Principal necesidad: " + (form.necesidadExtranjero.value || "-"));
      }
      return l.join("\n");
    }

    function mostrarMensaje(tipo, texto) {
      mensajeBox.className = "form-mensaje " + tipo;
      mensajeBox.textContent = texto;
      mensajeBox.setAttribute("role", "status");
    }

    /* Dirección del ayudante que recibe la consulta y manda el correo.
       Sale de config.js (build/site_config.py), nunca escrita acá: el día
       que cambie se toca en un solo lugar. Vacía = todavía no hay ayudante
       publicado, así que ni se intenta y se va derecho a WhatsApp. */
    function endpoint() {
      var c = window.MCG_CONFIG && window.MCG_CONFIG.formulario;
      return (c && c.endpoint) || "";
    }

    /* Camino 1: el ayudante recibe la consulta, la guarda y manda el correo.
       Camino 2: si no contesta, se abre WhatsApp con el mensaje armado.
       Nunca mostramos un "enviado con éxito" que no pasó. */
    function caminoWhatsapp(textoPrevio) {
      var mensaje = armarMensaje();
      var link = window.MCG_WHATSAPP_LINK ? window.MCG_WHATSAPP_LINK(mensaje) : "#";
      linkWa.href = link;
      linkWa.style.display = "inline-flex";
      mostrarMensaje(
        "exito",
        (textoPrevio ? textoPrevio + " " : "") +
          (window.MCG_TEXTOS && window.MCG_TEXTOS.formWhatsapp
            ? window.MCG_TEXTOS.formWhatsapp
            : "Preparamos tu consulta y abrimos WhatsApp en una pestaña nueva: revisá el mensaje y presioná enviar allí. Si no se abrió, usá el botón de abajo.")
      );
      window.open(link, "_blank");
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        mostrarMensaje(
          "error",
          (window.MCG_TEXTOS && window.MCG_TEXTOS.formIncompleto) ||
            "Completá los campos obligatorios antes de continuar."
        );
        return;
      }

      if (window.console) console.log("[medición] evento: formulario_enviado");

      var datos = new FormData(form);
      datos.append("facturacion", valorRadio("facturacion"));
      datos.append("idioma", window.MCG_LANG || "es");
      datos.append("origen", window.location.href);

      var boton = form.querySelector('button[type="submit"]');
      if (boton) boton.disabled = true;

      var destino = endpoint();
      if (!destino) {
        if (boton) boton.disabled = false;
        caminoWhatsapp();
        return;
      }

      var listo = false;
      var corte = setTimeout(function () {
        if (!listo) {
          listo = true;
          if (boton) boton.disabled = false;
          caminoWhatsapp();
        }
      }, 10000);

      /* Se manda como FormData a propósito. Con JSON el navegador pregunta
         primero "¿me dejás?" (una llamada OPTIONS) y el ayudante de Google
         no sabe contestar esa pregunta, así que el envío fallaría siempre. */
      fetch(destino, { method: "POST", body: datos })
        .then(function (r) {
          return r.ok ? r.json() : Promise.reject(r.status);
        })
        .then(function (res) {
          if (listo) return;
          listo = true;
          clearTimeout(corte);
          if (boton) boton.disabled = false;
          if (res && res.ok) {
            form.reset();
            actualizarBloques();
            mostrarMensaje(
              "exito",
              (window.MCG_TEXTOS && window.MCG_TEXTOS.formOk) ||
                "Recibimos tu consulta. Te vamos a responder al correo que dejaste. Si preferís que hablemos ahora, escribinos por WhatsApp."
            );
            linkWa.href = window.MCG_WHATSAPP_LINK ? window.MCG_WHATSAPP_LINK(armarMensaje()) : "#";
            linkWa.style.display = "inline-flex";
          } else {
            caminoWhatsapp();
          }
        })
        .catch(function () {
          if (listo) return;
          listo = true;
          clearTimeout(corte);
          if (boton) boton.disabled = false;
          caminoWhatsapp();
        });
    });
  });
})();
