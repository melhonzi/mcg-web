/* ============================================================
   MCG — comportamientos del sitio
   El header y el footer se generan en el HTML (mejor para SEO).
   Acá solo quedan las interacciones: menú móvil, acordeón de
   preguntas frecuentes, medición de clics y detección de idioma.
   ============================================================ */
(function () {
  "use strict";

  /* ---------- idioma: preferencia guardada + detección del navegador ---------- */
  function idiomaGuardado() {
    try {
      return window.localStorage.getItem("mcg_idioma");
    } catch (err) {
      return null;
    }
  }

  function guardarIdioma(valor) {
    try {
      window.localStorage.setItem("mcg_idioma", valor);
    } catch (err) {
      /* navegación privada: seguimos sin guardar */
    }
  }

  function idiomaDelNavegador() {
    var idiomas = navigator.languages && navigator.languages.length
      ? navigator.languages
      : [navigator.language || "es"];
    for (var i = 0; i < idiomas.length; i++) {
      var base = String(idiomas[i]).toLowerCase().slice(0, 2);
      if (base === "es" || base === "en" || base === "pt") return base;
    }
    return null;
  }

  function redirigirSiCorresponde() {
    var actual = window.MCG_LANG || "es";
    var alternativas = window.MCG_ALT || {};
    var forzado = null;
    try {
      forzado = new URLSearchParams(window.location.search).get("lang");
    } catch (err) {
      forzado = null;
    }

    if (forzado && alternativas[forzado] && forzado !== actual) {
      guardarIdioma(forzado);
      window.location.replace(alternativas[forzado]);
      return;
    }

    var guardado = idiomaGuardado();
    var destino = guardado || idiomaDelNavegador();
    if (!destino || destino === actual) return;
    if (!alternativas[destino]) return;

    /* una sola redirección automática por pestaña */
    try {
      if (window.sessionStorage.getItem("mcg_redirigido") === "1") return;
      window.sessionStorage.setItem("mcg_redirigido", "1");
    } catch (err) {
      /* si no hay sessionStorage, no redirigimos para evitar bucles */
      return;
    }
    window.location.replace(alternativas[destino]);
  }

  redirigirSiCorresponde();

  document.addEventListener("DOMContentLoaded", function () {
    /* ---------- menú móvil ---------- */
    var toggle = document.getElementById("navToggle");
    var links = document.getElementById("navLinks");
    if (toggle && links) {
      toggle.addEventListener("click", function () {
        var abierto = links.classList.toggle("abierto");
        toggle.setAttribute("aria-expanded", abierto ? "true" : "false");
      });
    }

    /* ---------- selector de idioma ---------- */
    document.querySelectorAll(".lang-op").forEach(function (el) {
      el.addEventListener("click", function () {
        guardarIdioma(el.getAttribute("data-lang"));
        try {
          window.sessionStorage.setItem("mcg_redirigido", "1");
        } catch (err) {
          /* sin sessionStorage igual navega */
        }
      });
    });

    /* ---------- acordeón de preguntas frecuentes ---------- */
    document.querySelectorAll(".faq-item").forEach(function (item) {
      var btn = item.querySelector(".faq-pregunta");
      var resp = item.querySelector(".faq-respuesta");
      if (!btn || !resp) return;
      btn.addEventListener("click", function () {
        var abierto = item.getAttribute("data-abierto") === "true";
        item.setAttribute("data-abierto", abierto ? "false" : "true");
        resp.style.maxHeight = abierto ? null : resp.scrollHeight + "px";
        btn.setAttribute("aria-expanded", abierto ? "false" : "true");
      });
    });

    /* ---------- medición: solo cuenta clics, nunca datos personales ---------- */
    document.querySelectorAll("[data-evento]").forEach(function (el) {
      el.addEventListener("click", function () {
        if (window.console) {
          console.log("[medición] evento:", el.getAttribute("data-evento"));
        }
      });
    });
  });
})();
