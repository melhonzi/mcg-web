/* Datos editables del negocio — generado desde build/site_config.py */
window.MCG_CONFIG = {
  "marca": {
    "nombre": "MCG Consultora Contable y Tributaria",
    "corto": "MCG",
    "instagram": "@mcgconsultoracontable",
    "instagramUrl": "https://www.instagram.com/mcgconsultoracontable/"
  },
  "direccion": {
    "nombreDirectora": "Cristina Rolón",
    "anosExperiencia": 18,
    "universidad": "Universidad Nacional de Asunción",
    "anioEgreso": 2008
  },
  "contacto": {
    "whatsappNumero": "+595 981 579250",
    "whatsappDigitos": "595981579250",
    "direccionTexto": "De Las Palmeras entre Cruz del Chaco y Cruz del Defensor, Asunción, Paraguay",
    "ciudad": "Asunción",
    "pais": "Paraguay",
    "correo": "mcgestudioc@gmail.com",
    "mapaUrl": "https://maps.app.goo.gl/AhZBTNs8369onMqa8",
    "googleReviewsUrl": "https://maps.app.goo.gl/AhZBTNs8369onMqa8",
    "waMensajeFlotante": "Hola MCG, vengo de la página web y quiero hacer una consulta"
  },
  "dominio": {
    "preferido": "mcgconsultora.com.py",
    "urlCanonicaBase": "https://mcgconsultora.com.py"
  }
};

window.MCG_WHATSAPP_LINK = function (mensaje) {
  var base = "https://wa.me/" + window.MCG_CONFIG.contacto.whatsappDigitos;
  var texto = encodeURIComponent(mensaje || "Hola MCG, vengo de la página web y quiero hacer una consulta");
  return base + "?text=" + texto;
};
