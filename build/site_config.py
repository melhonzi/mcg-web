# -*- coding: utf-8 -*-
"""Datos editables del negocio. Única fuente de verdad: desde acá se genera
config.js y se arman todos los enlaces del sitio en los tres idiomas."""

# Interruptor de publicación.
#   True  -> sitio público: Google puede indexarlo y no se muestra el banner.
#   False -> vista previa interna: noindex en cada página, banner visible y
#            robots.txt bloqueado.
# Al cambiar este valor hay que volver a correr: python3 build/build.py
PUBLICAR = True

CONFIG = {
    "marca": {
        "nombre": "MCG Consultora Contable y Tributaria",
        "corto": "MCG",
        "instagram": "@mcgconsultoracontable",
        "instagramUrl": "https://www.instagram.com/mcgconsultoracontable/",
    },
    "direccion": {
        "nombreDirectora": "Cristina Rolón",
        "anosExperiencia": 18,
        "universidad": "Universidad Nacional de Asunción",
        "anioEgreso": 2008,
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
        "waMensajeFlotante": "Hola MCG, vengo de la página web y quiero hacer una consulta",
    },
    # Dirección del ayudante de Google que recibe el formulario y manda el
    # correo, la planilla y el aviso por WhatsApp (ver build/FORMULARIO.md).
    # MIENTRAS ESTÉ VACÍA el formulario no intenta mandar nada y va directo
    # al camino de WhatsApp, que es lo que hace hoy: así el sitio nunca
    # queda a medias esperando una dirección que todavía no existe.
    "formulario": {
        "endpoint": "",
    },
    # El sitio se sirve en www (es lo que dice el archivo CNAME, y GitHub
    # Pages manda el dominio sin www a www con una redirección). Por eso el
    # canónico, los hreflang, el og:url, el og:image y el sitemap tienen que
    # decir www: si dicen otra cosa, cada dirección que Google visita rebota
    # en una redirección antes de llegar.
    "dominio": {
        "preferido": "www.mcgconsultora.com.py",
        "urlCanonicaBase": "https://www.mcgconsultora.com.py",
    },
}

DOMAIN = CONFIG["dominio"]["urlCanonicaBase"]

IMG = {
    "escena": "img/mcg-consultora-contable-oficina-cristina-rolon-asuncion-paraguay.jpg",
    # Misma foto en WebP: pesa la mitad. El JPG se queda porque es el que viaja
    # en og:image (WhatsApp y Facebook no muestran WebP de forma confiable).
    "escena_webp": "img/mcg-consultora-contable-oficina-cristina-rolon-asuncion-paraguay.webp",
    "hero": "img/cristina-rolon-contadora-mcg-consultora-contable-tributaria.png",
    "retrato": "img/cristina-rolon-contadora-publica-directora-mcg-asuncion-paraguay.jpg",
    "equipo": "img/equipo-mcg-consultora-contable-tributaria-asuncion-paraguay.jpg",
    "logo_oficial": "img/mcg-consultora-contable-logo-oficial-navy.jpg",
    "logo_cuadrado": "img/mcg-consultora-contable-logo-oficial-cuadrado.jpg",
    "logo_dorado": "img/mcg-consultora-contable-logo-dorado.png",
    "logo_negro": "img/mcg-consultora-contable-logo-negro.png",
    "logo_blanco": "img/mcg-consultora-contable-logo-blanco.png",
    "logo_navy": "img/mcg-consultora-contable-logo-navy.jpg",
    "patron": "img/mcg-consultora-contable-patron-monograma.png",
}
