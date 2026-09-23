# -*- coding: utf-8 -*-
"""
Generador estático del sitio de MCG Consultora Contable y Tributaria.
Produce las tres versiones del sitio (es / en / pt) con header y footer
renderizados en el HTML (no por JavaScript), enlaces hreflang entre idiomas,
datos estructurados y sitemap.
"""
import datetime
import json
import os
import sys
import html as htmlmod

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from site_config import CONFIG, DOMAIN, IMG, PUBLICAR  # noqa: E402

# Con PUBLICAR = True el sitio sale público; con False queda como vista previa
# interna (ver build/site_config.py).
META_ROBOTS = "index, follow" if PUBLICAR else "noindex, nofollow"


def banner_preview(data):
    """Franja de aviso de vista previa. Vacía cuando el sitio ya es público."""
    if PUBLICAR:
        return ""
    return '<div class="preview-banner">%s</div>' % e(data["preview_banner"])

LANGS = ["es", "en", "pt"]
HREFLANG = {"es": "es", "en": "en", "pt": "pt"}
PREFIX = {"es": "", "en": "en/", "pt": "pt/"}
LOCALE = {"es": "es_PY", "en": "en_US", "pt": "pt_BR"}
HTMLLANG = {"es": "es-PY", "en": "en", "pt": "pt-BR"}
PAGE_ORDER = ["home", "contabilidad", "tributaria", "erp", "sociedades",
              "extranjeros", "equipo", "faq", "contacto"]
HOY = datetime.date.today().isoformat()
PRIORIDAD = {"home": "1.0", "faq": "0.9", "contabilidad": "0.9", "tributaria": "0.9",
             "sociedades": "0.9", "extranjeros": "0.9", "erp": "0.9", "contacto": "0.8", "equipo": "0.7"}


def e(s):
    return htmlmod.escape(s, quote=True)


def load(lang):
    ns = {}
    path = os.path.join(HERE, "content_%s.py" % lang)
    with open(path, encoding="utf-8") as fh:
        exec(compile(fh.read(), path, "exec"), ns)
    return ns["DATA"]


def wa_link(mensaje):
    import urllib.parse
    return "https://wa.me/%s?text=%s" % (
        CONFIG["contacto"]["whatsappDigitos"], urllib.parse.quote(mensaje))


# ---------------------------------------------------------------- utilidades
def asset(path, lang):
    """Ruta relativa a un asset de la raíz según el idioma."""
    return ("../" + path) if lang != "es" else path


def page_href(target_key, lang, data):
    """Enlace interno dentro del mismo idioma."""
    return data["pages"][target_key]["slug"]


def abs_url(lang, slug):
    p = PREFIX[lang]
    if slug == "index.html":
        return "%s/%s" % (DOMAIN, p) if p else DOMAIN + "/"
    return "%s/%s%s" % (DOMAIN, p, slug)


def rel_between_langs(from_lang, to_lang, slug):
    """Ruta relativa desde una página de from_lang hacia slug de to_lang."""
    if from_lang == "es" and to_lang == "es":
        return slug
    if from_lang == "es":
        return "%s%s" % (PREFIX[to_lang], slug)
    if to_lang == "es":
        return "../%s" % slug
    if from_lang == to_lang:
        return slug
    return "../%s%s" % (PREFIX[to_lang], slug)


# ------------------------------------------------------------------- bloques
ICONOS = {
    "trofeo": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 21h8M12 17v4M6 4h12v5a6 6 0 0 1-12 0V4Z"/><path d="M18 5h2a2 2 0 0 1 0 4h-2M6 5H4a2 2 0 0 0 0 4h2"/></svg>',
    "birrete": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 9 12 4 2 9l10 5 10-5Z"/><path d="M6 11.5V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-4.5"/></svg>',
    "grafico": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
}
ICONO_ORDEN = ["trofeo", "birrete", "grafico"]


def b_hero(b, lang, data):
    creds = ""
    for i, c in enumerate(b.get("credenciales", [])):
        ico = ICONOS[ICONO_ORDEN[i % len(ICONO_ORDEN)]]
        creds += ('<li><span class="cred-ico">%s</span><span class="cred-txt">'
                  "<strong>%s</strong><span>%s</span></span></li>" % (ico, e(c[0]), e(c[1])))
    return (
        '<section class="hero-marca">'
        '<div class="hero-marca-escena" aria-hidden="true"></div>'
        '<div class="hero-marca-velo" aria-hidden="true"></div>'
        '<div class="container hero-marca-grid">'
        '<div class="hero-marca-texto">'
        '<span class="hero-chip">%s</span>'
        "<h1>%s</h1>"
        '<p class="hero-marca-lead">%s</p>'
        '<p class="hero-marca-firma">%s</p>'
        '<div class="btn-row">'
        '<a class="btn btn-oro" href="%s" data-evento="cta_hero_principal">%s <span aria-hidden="true">&rarr;</span></a>'
        '<a class="btn btn-borde-claro" href="%s">%s</a>'
        "</div>"
        '<ul class="hero-credenciales">%s</ul>'
        "</div></div></section>"
        % (e(b["chip"]), b["h1_html"], e(b["lead"]), b["firma_html"],
           page_href("contacto", lang, data), e(b["cta1"]),
           b.get("cta2_href", "#servicios"), e(b["cta2"]), creds)
    )


def b_hero_simple(b, lang, data):
    btns = ""
    if b.get("cta"):
        btns = ('<div class="btn-row"><a class="btn btn-primario" href="%s" data-evento="cta_hero">%s</a></div>'
                % (page_href("contacto", lang, data), e(b["cta"])))
    return ('<section class="hero section-tight"><div class="container">'
            '<span class="eyebrow">%s</span><h1>%s</h1>'
            '<p class="lead max-w-prose">%s</p>%s</div></section>'
            % (e(b["eyebrow"]), e(b["h1"]), e(b["lead"]), btns))


def b_franja(b, lang, data):
    items = "".join(
        '<div class="franja-publico-item"><span class="check-ico">&#10003;</span> %s</div>' % e(i)
        for i in b["items"]
    )
    micro = ('<p class="microcopy mb-0" style="margin-top:18px;">%s</p>' % e(b["microcopy"])) if b.get("microcopy") else ""
    return ('<section class="franja-publico"><div class="container">'
            '<div class="franja-publico-grid">%s</div>%s</div></section>' % (items, micro))


def _head_bloque(b):
    out = ""
    if b.get("eyebrow"):
        out += '<span class="eyebrow">%s</span>' % e(b["eyebrow"])
    if b.get("h2"):
        out += "<h2>%s</h2>" % e(b["h2"])
    if b.get("lead"):
        out += '<p class="lead max-w-prose">%s</p>' % e(b["lead"])
    return out


def b_rich(b, lang, data):
    cls = "section section-alt" if b.get("alt") else "section"
    parr = "".join("<p>%s</p>" % p for p in b.get("paragraphs", []))
    return ('<section class="%s"><div class="container max-w-prose">%s%s</div></section>'
            % (cls, _head_bloque(b), parr))


def b_cards(b, lang, data):
    cls = "section section-alt" if b.get("alt") else "section"
    cols = b.get("columns", 3)
    items = "".join(
        '<div class="card"><h3>%s</h3><p class="texto-card">%s</p></div>'
        % (e(i[0]), e(i[1])) for i in b["items"]
    )
    parr = "".join('<p class="max-w-prose parrafo-post">%s</p>' % p
                   for p in b.get("paragraphs", []))
    return ('<section class="%s"><div class="container">%s'
            '<div class="grid grid-%d" style="margin-top:24px;">%s</div>%s</div></section>'
            % (cls, _head_bloque(b), cols, items, parr))


def b_checks(b, lang, data):
    cls = "section section-alt" if b.get("alt") else "section"
    lis = "".join('<li><span class="check-ico">&#10003;</span> %s</li>' % e(i) for i in b["items"])
    parr = "".join('<p class="max-w-prose">%s</p>' % p for p in b.get("paragraphs", []))
    return ('<section class="%s"><div class="container">%s'
            '<ul class="lista-check lista-check-ancha">%s</ul>%s</div></section>'
            % (cls, _head_bloque(b), lis, parr))


def b_problemas(b, lang, data):
    cls = "section section-alt" if b.get("alt") else "section"
    lis = "".join('<li><span class="marca-x">&#10005;</span><span>%s</span></li>' % e(i) for i in b["items"])
    parr = "".join('<p class="max-w-prose parrafo-post">%s</p>' % p
                   for p in b.get("paragraphs", []))
    return ('<section class="%s"><div class="container">%s'
            '<ul class="lista-problemas" style="margin-top:28px;">%s</ul>%s</div></section>'
            % (cls, _head_bloque(b), lis, parr))


def b_caminos(b, lang, data):
    cards = ""
    for i, it in enumerate(b["items"]):
        cards += (
            '<div class="camino%s">'
            '<span class="badge" style="background:rgba(255,255,255,.1); color:#fff; border-color:rgba(255,255,255,.2);">%s</span>'
            "<h3>%s</h3><p>%s</p>"
            '<div class="btn-row"><a class="btn btn-sobre-oscuro" href="%s">%s</a></div></div>'
            % (" alt" if i else "", e(it["badge"]), e(it["h3"]), e(it["p"]),
               page_href(it["target"], lang, data), e(it["cta"]))
        )
    return '<section class="section"><div class="container"><div class="caminos">%s</div></div></section>' % cards


def b_pasos(b, lang, data):
    cls = "section section-alt" if b.get("alt") else "section"
    pasos = ""
    for i, it in enumerate(b["items"], 1):
        pasos += ('<div class="paso"><div class="paso-num">%d</div><div><h3>%s</h3>'
                  '<p class="texto-paso">%s</p></div></div>'
                  % (i, e(it[0]), e(it[1])))
    return ('<section class="%s"><div class="container">%s'
            '<div class="pasos">%s</div></div></section>'
            % (cls, _head_bloque(b), pasos))


def b_planes(b, lang, data):
    cards = ""
    for it in b["items"]:
        checks = "".join('<li><span class="check-ico">&#10003;</span> %s</li>' % e(c) for c in it["checks"])
        cards += (
            '<div class="precio-card%s"><span class="badge">%s</span>'
            '<div class="precio-valor">%s</div>'
            '<p class="texto-card">%s</p>'
            '<ul class="lista-check">%s</ul>'
            '<a class="btn %s btn-block" href="%s">%s</a></div>'
            % (" destacado" if it.get("destacado") else "", e(it["badge"]), e(it["valor"]),
               e(it["p"]), checks, "btn-primario" if it.get("destacado") else "btn-secundario",
               page_href("contacto", lang, data), e(it["cta"]))
        )
    extra = "".join('<p class="max-w-prose parrafo-post">%s</p>' % p
                    for p in b.get("paragraphs", []))
    return ('<section class="section section-alt"><div class="container">%s'
            '<div class="grid grid-2" style="margin-top:28px;">%s</div>%s</div></section>'
            % (_head_bloque(b), cards, extra))


def b_faq(b, lang, data):
    cls = "section section-alt" if b.get("alt") else "section"
    items = ""
    for q, a in b["items"]:
        items += (
            '<div class="faq-item" data-abierto="false">'
            '<button class="faq-pregunta" aria-expanded="false">%s<span class="faq-plus">+</span></button>'
            '<div class="faq-respuesta"><div class="faq-respuesta-inner">%s</div></div></div>'
            % (e(q), a)
        )
    ver = ""
    if b.get("ver_todas"):
        ver = ('<p style="margin-top:18px;"><a href="%s">%s</a></p>'
               % (page_href("faq", lang, data), e(b["ver_todas"])))
    return ('<section class="%s"><div class="container max-w-prose">%s'
            '<div style="margin-top:16px;">%s</div>%s</div></section>'
            % (cls, _head_bloque(b), items, ver))


def b_bio(b, lang, data):
    lis = "".join('<li><span class="check-ico">&#10003;</span> %s</li>' % e(i) for i in b["trayectoria"])
    parr = "".join("<p>%s</p>" % p for p in b.get("paragraphs", []))
    return (
        '<section class="section"><div class="container bio-grid">'
        '<figure class="bio-figura">'
        '<img src="%s" alt="%s" width="1024" height="1280">'
        '<figcaption><strong>%s</strong><span>%s</span></figcaption>'
        "</figure>"
        '<div class="bio-texto"><h2>%s</h2><ul class="lista-check">%s</ul>%s</div>'
        "</div></section>"
        % (asset(IMG["retrato"], lang), e(b["foto_alt"]), e(b["nombre"]), e(b["cargo"]),
           e(b["h2"]), lis, parr)
    )


def b_equipo(b, lang, data):
    parr = "".join("<p>%s</p>" % p for p in b.get("paragraphs", []))
    return (
        '<section class="section section-alt"><div class="container max-w-prose" style="text-align:center;">'
        '%s</div>'
        '<div class="container equipo-foto-wrap">'
        '<img src="%s" alt="%s" width="1400" height="1120" loading="lazy">'
        "</div>"
        '<div class="container max-w-prose" style="margin-top:26px;">%s</div></section>'
        % (_head_bloque(b), asset(IMG["equipo"], lang), e(b["foto_alt"]), parr)
    )



def b_opiniones(b, lang, data):
    url = CONFIG["contacto"].get("googleReviewsUrl") or ""
    cards = ""
    for r in b.get("reseñas", []):
        cards += ('<figure class="opinion-card"><div class="opinion-estrellas" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
                  "<blockquote>%s</blockquote><figcaption>%s</figcaption></figure>" % (e(r[0]), e(r[1])))
    grid = ('<div class="opiniones-grid">%s</div>' % cards) if cards else ""
    boton = ""
    if url:
        boton = ('<div class="btn-row" style="justify-content:center; margin-top:26px;">'
                 '<a class="btn btn-secundario" href="%s" target="_blank" rel="noopener" data-evento="google_reviews_click">%s</a></div>'
                 % (url, e(b["cta"])))
    return ('<section class="section section-alt"><div class="container max-w-prose" style="text-align:center;">%s</div>'
            '<div class="container">%s%s</div></section>'
            % (_head_bloque(b), grid, boton))


def b_cta(b, lang, data):
    lead = ('<p class="lead">%s</p>' % e(b["lead"])) if b.get("lead") else ""
    return ('<section class="section section-dark text-center">'
            '<div class="container max-w-prose" style="margin:0 auto;">'
            '<h2>%s</h2>%s<a class="btn btn-sobre-oscuro" href="%s" data-evento="cta_cierre">%s</a>'
            "</div></section>"
            % (e(b["h2"]), lead, page_href("contacto", lang, data), e(b["cta"])))


def b_form(b, lang, data):
    f = b["form"]
    opts = lambda items: "".join('<option value="%s">%s</option>' % (e(v), e(t)) for v, t in items)
    radios = "".join(
        '<label class="radio-opcion"><input type="radio" name="facturacion" value="%s"> %s</label>' % (e(v), e(v))
        for v in f["facturacion_opciones"]
    )
    return (
        '<section class="section"><div class="container" style="max-width:720px;">'
        '<div class="form-card"><form id="formContacto" novalidate>'
        '<div class="form-grupo"><label for="situacion">%s</label>'
        '<select id="situacion" name="situacionGeneral" required>'
        '<option value="" disabled selected>%s</option>%s</select></div>'
        '<div class="grid grid-2">'
        '<div class="form-grupo"><label for="nombre">%s</label>'
        '<input type="text" id="nombre" name="nombre" required autocomplete="name"></div>'
        '<div class="form-grupo"><label for="empresa">%s</label>'
        '<input type="text" id="empresa" name="empresa" autocomplete="organization"></div></div>'
        '<div class="grid grid-2">'
        '<div class="form-grupo"><label for="correoContacto">%s</label>'
        '<input type="email" id="correoContacto" name="correoContacto" required autocomplete="email"></div>'
        '<div class="form-grupo"><label for="whatsappContacto">%s</label>'
        '<input type="tel" id="whatsappContacto" name="whatsappContacto" required autocomplete="tel" placeholder="%s"></div></div>'
        '<div class="form-grupo"><label for="servicio">%s</label>'
        '<select id="servicio" name="servicio" required>'
        '<option value="" disabled selected>%s</option>%s</select></div>'
        '<fieldset id="bloqueEmpresa" class="paso-tab">'
        '<legend class="eyebrow" style="margin-bottom:12px;">%s</legend>'
        '<div class="form-grupo"><label for="rubro">%s</label>'
        '<input type="text" id="rubro" name="rubro" data-obligatorio></div>'
        '<div class="form-grupo"><label>%s</label><div class="radio-row">%s</div></div>'
        '<div class="form-grupo"><label for="necesidadEmpresa">%s</label>'
        '<textarea id="necesidadEmpresa" name="necesidadEmpresa" data-obligatorio></textarea></div></fieldset>'
        '<fieldset id="bloqueExtranjero" class="paso-tab">'
        '<legend class="eyebrow" style="margin-bottom:12px;">%s</legend>'
        '<div class="grid grid-2">'
        '<div class="form-grupo"><label for="paisResidencia">%s</label>'
        '<input type="text" id="paisResidencia" name="paisResidencia" data-obligatorio></div>'
        '<div class="form-grupo"><label for="tipoProyecto">%s</label>'
        '<input type="text" id="tipoProyecto" name="tipoProyecto" data-obligatorio placeholder="%s"></div></div>'
        '<div class="form-grupo"><label for="etapaProyecto">%s</label>'
        '<select id="etapaProyecto" name="etapaProyecto" data-obligatorio>'
        '<option value="" disabled selected>%s</option>%s</select></div>'
        '<div class="form-grupo"><label for="necesidadExtranjero">%s</label>'
        '<textarea id="necesidadExtranjero" name="necesidadExtranjero" data-obligatorio></textarea></div></fieldset>'
        '<div style="position:absolute;left:-9999px;" aria-hidden="true">'
        '<label>No completar<input type="text" name="sitioWeb" tabindex="-1" autocomplete="off"></label></div>'
        '<p class="microcopy" style="margin-bottom:18px;">%s</p>'
        '<button type="submit" class="btn btn-primario btn-block">%s</button>'
        '<div id="formMensaje" class="form-mensaje" aria-live="polite"></div>'
        '<a id="linkWhatsappManual" href="#" target="_blank" rel="noopener" class="btn btn-whatsapp btn-block" '
        'style="display:none; margin-top:12px;" data-evento="whatsapp_click">%s</a>'
        "</form></div></div></section>"
        % (e(f["situacion"]), e(f["seleccione"]), opts(f["situacion_opciones"]),
           e(f["nombre"]), e(f["empresa"]), e(f["correo"]), e(f["whatsapp"]), e(f["whatsapp_ph"]),
           e(f["servicio"]), e(f["seleccione_servicio"]), opts(f["servicio_opciones"]),
           e(f["legend_empresa"]), e(f["rubro"]), e(f["facturacion"]), radios, e(f["necesidad"]),
           e(f["legend_extranjero"]), e(f["pais"]), e(f["tipo_proyecto"]), e(f["tipo_ph"]),
           e(f["etapa"]), e(f["seleccione_etapa"]), opts(f["etapa_opciones"]), e(f["necesidad"]),
           e(f["aviso"]), e(f["enviar"]), e(f["abrir_wa"]))
    )


def b_contacto_extra(b, lang, data):
    correo = CONFIG["contacto"]["correo"]
    mail = ('<a class="btn btn-secundario" href="mailto:%s" data-evento="email_click">%s</a>' % (correo, correo)) if correo else ""
    mapa = ""
    if CONFIG["contacto"].get("mapaUrl"):
        mapa = ('<div class="direccion-card">'
                '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" '
                'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/></svg>'
                "<div><strong>%s</strong><span>%s</span>"
                '<a href="%s" target="_blank" rel="noopener" data-evento="mapa_click">%s</a></div></div>'
                % (e(b.get("direccion_titulo", "Dirección")), e(CONFIG["contacto"]["direccionTexto"]),
                   CONFIG["contacto"]["mapaUrl"], e(b.get("mapa_cta", "Ver en Google Maps"))))
    return (mapa and "" or "") + (
        '<section class="section section-alt"><div class="container max-w-prose">%s'
        "<p>%s</p>"
        '<div class="btn-row">'
        '<a class="btn btn-whatsapp" href="%s" data-evento="whatsapp_click" target="_blank" rel="noopener">%s</a>'
        '<a class="btn btn-secundario" href="%s" target="_blank" rel="noopener">%s</a>%s</div>'
        "%s</div></section>"
        % (_head_bloque(b), e(b["p"]), wa_link(b["wa_mensaje"]), e(b["wa_cta"]),
           CONFIG["marca"]["instagramUrl"], e(b["ig_cta"]), mail, mapa)
    )


RENDER = {
    "hero": b_hero, "hero_simple": b_hero_simple, "franja": b_franja, "rich": b_rich, "cards": b_cards,
    "checks": b_checks, "problemas": b_problemas, "caminos": b_caminos,
    "pasos": b_pasos, "planes": b_planes, "faq": b_faq, "bio": b_bio,
    "equipo": b_equipo, "opiniones": b_opiniones, "cta": b_cta, "form": b_form, "contacto_extra": b_contacto_extra,
}


# ------------------------------------------------------------ header / footer
def render_header(data, lang, page_key, alldata):
    nav = ""
    for key in PAGE_ORDER:
        if key in ("home", "contacto"):
            continue
        p = data["pages"][key]
        cur = ' aria-current="page"' if key == page_key else ""
        nav += '<li><a href="%s"%s>%s</a></li>' % (p["slug"], cur, e(p["nav"]))
    home_cur = ' aria-current="page"' if page_key == "home" else ""
    nav = ('<li><a href="index.html"%s>%s</a></li>' % (home_cur, e(data["pages"]["home"]["nav"]))) + nav
    nav += ('<li class="nav-item-cta"><a class="btn btn-oro btn-block" href="%s" data-evento="cta_menu">%s</a></li>'
            % (data["pages"]["contacto"]["slug"], e(data["cta_nav"])))

    switch = ""
    for l in LANGS:
        slug = alldata[l]["pages"][page_key]["slug"]
        href = rel_between_langs(lang, l, slug)
        act = " activo" if l == lang else ""
        switch += ('<a class="lang-op%s" href="%s" hreflang="%s" data-lang="%s" rel="alternate">%s</a>'
                   % (act, href, HREFLANG[l], l, l.upper()))

    return (
        '<a class="saltar-contenido" href="#contenido">%s</a>'
        '%s'
        '<header class="site-header"><nav class="nav-bar" aria-label="%s">'
        '<a href="index.html" class="brand">'
        '<img class="brand-logo" src="%s" alt="%s" width="900" height="450"></a>'
        '<button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navLinks" aria-label="%s">'
        '<svg width="22" height="22" viewBox="0 0 22 22" fill="none" aria-hidden="true">'
        '<path d="M2 5H20M2 11H20M2 17H20" stroke="#112250" stroke-width="2" stroke-linecap="round"/></svg>'
        "</button>"
        '<ul class="nav-links" id="navLinks">%s</ul>'
        '<div class="nav-cta"><div class="lang-switch" role="group" aria-label="%s">%s</div>'
        '<a class="btn btn-primario" href="%s" data-evento="cta_nav">%s</a></div>'
        "</nav></header>"
        % (e(data.get("saltar", "Ir al contenido")), banner_preview(data), e(data["nav_aria"]),
           asset(IMG["logo_dorado"], lang), e(data["logo_alt"]), e(data["menu_label"]),
           nav, e(data["lang_aria"]), switch,
           data["pages"]["contacto"]["slug"], e(data["cta_nav"]))
    )


def render_footer(data, lang):
    f = data["footer"]
    col1 = "".join('<li><a href="%s">%s</a></li>' % (data["pages"][k]["slug"], e(data["pages"][k]["nav_footer"]))
                   for k in ["contabilidad", "tributaria", "sociedades", "extranjeros"])
    col2 = "".join('<li><a href="%s">%s</a></li>' % (data["pages"][k]["slug"], e(data["pages"][k]["nav_footer"]))
                   for k in ["equipo", "faq", "contacto"])
    correo = CONFIG["contacto"]["correo"]
    mail_li = ('<li><a href="mailto:%s" data-evento="email_click">%s</a></li>' % (correo, correo)) if correo else ""
    return (
        '<footer class="site-footer"><div class="container"><div class="footer-grid">'
        "<div>"
        '<img class="footer-brand-logo" src="%s" alt="%s" width="190" height="95">'
        "<p>%s</p><p>%s</p></div>"
        "<div><h4>%s</h4><ul>%s</ul></div>"
        "<div><h4>%s</h4><ul>%s</ul></div>"
        "<div><h4>%s</h4><ul>"
        '<li><a href="%s" data-evento="whatsapp_click" target="_blank" rel="noopener">WhatsApp: %s</a></li>'
        "%s"
        '<li><a href="%s" target="_blank" rel="noopener">Instagram</a></li>'
        '<li><a href="%s" target="_blank" rel="noopener" data-evento="mapa_click">%s</a></li>'
        "</ul></div></div>"
        '<div class="footer-legal"><span>&copy; %s %s</span><span>%s</span></div>'
        "</div></footer>"
        '<a class="wa-flotante" href="%s" target="_blank" rel="noopener" data-evento="whatsapp_click" aria-label="WhatsApp">'
        '<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2Zm5.8 14.06c-.24.68-1.4 1.3-1.94 1.35-.5.05-1.13.07-1.82-.11-.42-.11-.96-.29-1.66-.59-2.92-1.26-4.82-4.2-4.97-4.4-.14-.2-1.19-1.58-1.19-3.02 0-1.43.75-2.14 1.02-2.43.27-.29.58-.36.78-.36l.56.01c.18 0 .42-.7.65.5.24.58.82 2.01.89 2.16.07.14.12.31.02.51-.09.2-.14.32-.28.49-.14.17-.3.38-.42.51-.14.14-.29.29-.12.58.16.29.72 1.2 1.55 1.94 1.07.95 1.97 1.25 2.26 1.39.29.14.45.12.62-.07.17-.2.71-.83.9-1.11.19-.29.38-.24.65-.14.26.09 1.69.8 1.98.94.29.14.48.22.55.34.07.12.07.68-.17 1.36Z"/></svg></a>'
        % (asset(IMG["logo_blanco"], lang), e(data["logo_alt"]), e(f["tagline"]), e(f["ciudad"]),
           e(f["col_servicios"]), col1, e(f["col_estudio"]), col2, e(f["col_contacto"]),
           wa_link(f["wa_mensaje"]), CONFIG["contacto"]["whatsappNumero"], mail_li,
           CONFIG["marca"]["instagramUrl"],
           CONFIG["contacto"]["mapaUrl"], e(CONFIG["contacto"]["direccionTexto"]),
           2026, e(f["copyright"]), e(f["legal"]),
           wa_link(f["wa_mensaje"]))
    )


# --------------------------------------------------------------- estructurados
def jsonld_org(data, lang):
    d = {
        "@context": "https://schema.org",
        "@type": "AccountingService",
        "@id": DOMAIN + "/#organizacion",
        "name": CONFIG["marca"]["nombre"],
        "alternateName": "MCG",
        "description": data["org_description"],
        "url": abs_url(lang, "index.html"),
        "image": DOMAIN + "/" + IMG["logo_cuadrado"],
        "logo": DOMAIN + "/" + IMG["logo_cuadrado"],
        "telephone": CONFIG["contacto"]["whatsappNumero"],
        "areaServed": [{"@type": "Country", "name": "Paraguay"}],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CONFIG["contacto"]["direccionTexto"],
            "addressLocality": CONFIG["contacto"]["ciudad"],
            "addressCountry": "PY",
        },
        "hasMap": CONFIG["contacto"].get("mapaUrl", ""),
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "customer service",
            "telephone": CONFIG["contacto"]["whatsappNumero"],
            "availableLanguage": ["Spanish", "English", "Portuguese"],
            "areaServed": "PY",
        }],
        "currenciesAccepted": "PYG",
        "knowsLanguage": ["es", "en", "pt"],
        "sameAs": [CONFIG["marca"]["instagramUrl"]],
        "founder": {
            "@type": "Person",
            "@id": DOMAIN + "/#cristina-rolon",
            "name": CONFIG["direccion"]["nombreDirectora"],
            "jobTitle": data["person_jobtitle"],
            "alumniOf": {"@type": "CollegeOrUniversity", "name": CONFIG["direccion"]["universidad"]},
        },
    }
    return d


def jsonld_person(data, lang):
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": DOMAIN + "/#cristina-rolon",
        "name": CONFIG["direccion"]["nombreDirectora"],
        "jobTitle": data["person_jobtitle"],
        "description": data["person_description"],
        "image": DOMAIN + "/" + IMG["retrato"],
        "url": abs_url(lang, data["pages"]["equipo"]["slug"]),
        "alumniOf": {"@type": "CollegeOrUniversity", "name": CONFIG["direccion"]["universidad"]},
        "worksFor": {"@type": "AccountingService", "@id": DOMAIN + "/#organizacion",
                     "name": CONFIG["marca"]["nombre"]},
        "knowsAbout": data["person_knows"],
        "address": {"@type": "PostalAddress", "addressLocality": CONFIG["contacto"]["ciudad"],
                    "addressCountry": "PY"},
        "sameAs": [CONFIG["marca"]["instagramUrl"]],
    }


def jsonld_faq(page):
    items = []
    for b in page["blocks"]:
        if b["type"] == "faq" and b.get("schema", True):
            for q, a in b["items"]:
                txt = a.replace("<strong>", "").replace("</strong>", "")
                txt = txt.replace("<em>", "").replace("</em>", "")
                import re as _re
                txt = _re.sub(r"<[^>]+>", "", txt)
                items.append({"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": txt}})
    if not items:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}


def jsonld_service(page, data, lang):
    if not page.get("service"):
        return None
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": page["service"],
        "name": page["h1"],
        "description": page["description"],
        "provider": {"@type": "AccountingService", "@id": DOMAIN + "/#organizacion",
                     "name": CONFIG["marca"]["nombre"]},
        "areaServed": {"@type": "Country", "name": "Paraguay"},
        "url": abs_url(lang, page["slug"]),
        "availableLanguage": ["es", "en", "pt"],
    }


def jsonld_breadcrumb(page, data, lang, page_key):
    items = [{"@type": "ListItem", "position": 1, "name": data["pages"]["home"]["nav"],
              "item": abs_url(lang, "index.html")}]
    if page_key != "home":
        items.append({"@type": "ListItem", "position": 2, "name": page["nav"],
                      "item": abs_url(lang, page["slug"])})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


# ------------------------------------------------------------------ documento
def render_page(lang, page_key, data, alldata, wrap=True):
    page = data["pages"][page_key]
    slug = page["slug"]
    canonical = abs_url(lang, slug)

    alt_links = ""
    alt_map = {}
    for l in LANGS:
        s = alldata[l]["pages"][page_key]["slug"]
        alt_links += '<link rel="alternate" hreflang="%s" href="%s">' % (HREFLANG[l], abs_url(l, s))
        alt_map[l] = rel_between_langs(lang, l, s)
    alt_links += '<link rel="alternate" hreflang="x-default" href="%s">' % abs_url("es", alldata["es"]["pages"][page_key]["slug"])

    schemas = [jsonld_org(data, lang), jsonld_breadcrumb(page, data, lang, page_key),
               {"@context": "https://schema.org", "@type": "WebSite",
                "@id": DOMAIN + "/#sitio-" + lang,
                "name": CONFIG["marca"]["nombre"],
                "url": abs_url(lang, "index.html"),
                "inLanguage": HTMLLANG[lang],
                "publisher": {"@id": DOMAIN + "/#organizacion"}}]
    if page_key == "equipo":
        schemas.append(jsonld_person(data, lang))
    f = jsonld_faq(page)
    if f:
        schemas.append(f)
    s = jsonld_service(page, data, lang)
    if s:
        schemas.append(s)
    schema_html = "".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False)
        for x in schemas
    )

    # La foto del hero se pide de entrada y con prioridad alta: es lo más
    # grande que se ve al abrir y de ella depende la sensación de "ya cargó".
    # Se pide la versión WebP (la mitad de peso) con su type: el navegador que
    # no la entiende simplemente ignora esta línea y baja el JPG al leer el CSS.
    preload = ('<link rel="preload" as="image" type="image/webp" href="%s" fetchpriority="high">'
               % asset(IMG["escena_webp"], lang)) if page_key == "home" else ""
    # Las dos tipografías que se ven apenas abre la página. Se piden de entrada
    # para que el texto no aparezca primero con la letra de reserva y salte.
    preload += (
        '<link rel="preload" as="font" type="font/woff2" crossorigin href="%s">'
        '<link rel="preload" as="font" type="font/woff2" crossorigin href="%s">'
        % (asset("fonts/inter-latin.woff2", lang),
           asset("fonts/cormorant-garamond-latin.woff2", lang))
    )
    og_img = DOMAIN + "/" + (IMG["escena"] if page_key == "home" else
                             IMG["retrato"] if page_key == "equipo" else IMG["logo_cuadrado"])

    head = (
        "<title>%s</title>"
        '<meta name="description" content="%s">'
        '<meta name="robots" content="%s">'
        '<link rel="canonical" href="%s">'
        "%s"
        '<meta property="og:type" content="website">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:url" content="%s">'
        '<meta property="og:image" content="%s">'
        '<meta property="og:locale" content="%s">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<link rel="icon" type="image/jpeg" href="%s">'
        '<link rel="apple-touch-icon" href="%s">'
        '<meta name="theme-color" content="#001D45">'
        '%s'
        # Las tipografías ya no se piden a Google: viven en fonts/ y se declaran
        # dentro de styles.css. Aquel <link> a fonts.googleapis.com frenaba el
        # dibujado de la página hasta que respondía un servidor de terceros.
        '<link rel="stylesheet" href="%s">'
        "%s"
        '<script>window.MCG_LANG="%s";window.MCG_ALT=%s;window.MCG_WA_SALUDO=%s;window.MCG_TEXTOS=%s;</script>'
        % (e(page["title"]), e(page["description"]), META_ROBOTS, canonical, alt_links,
           e(page["title"]), e(page["description"]), canonical,
           og_img, LOCALE[lang],
           asset(IMG["logo_cuadrado"], lang), asset(IMG["logo_cuadrado"], lang), preload,
           asset("styles.css", lang), schema_html, lang, json.dumps(alt_map, ensure_ascii=False),
           json.dumps(data["footer"]["wa_mensaje"], ensure_ascii=False),
           json.dumps(data.get("textos_form", {}), ensure_ascii=False))
    )

    breadcrumb = ""
    if page_key != "home":
        breadcrumb = ('<div class="container breadcrumb"><a href="index.html">%s</a> / %s</div>'
                      % (e(data["pages"]["home"]["nav"]), e(page["nav"])))

    body = render_header(data, lang, page_key, alldata)
    body += '<main id="contenido">' + breadcrumb
    for i, b in enumerate(page["blocks"]):
        if b["type"] == "cta" and page.get("service"):
            otros = [k for k in ("contabilidad", "tributaria", "erp", "sociedades", "extranjeros", "faq")
                     if k != page_key]
            enlaces = "".join(
                '<li><a href="%s">%s</a></li>' % (data["pages"][k]["slug"], e(data["pages"][k]["nav_footer"]))
                for k in otros)
            body += ('<section class="section section-alt"><div class="container max-w-prose">'
                     '<span class="eyebrow">%s</span><ul class="enlaces-relacionados">%s</ul>'
                     "</div></section>" % (e(data.get("relacionados", "Seguí explorando")), enlaces))
        body += RENDER[b["type"]](b, lang, data)
    body += "</main>"
    body += render_footer(data, lang)
    body += '<script src="%s"></script>' % asset("config.js", lang)
    body += '<script src="%s"></script>' % asset("partials.js", lang)
    if page_key == "contacto":
        body += '<script src="%s"></script>' % asset("form.js", lang)

    if not wrap:
        return head + body
    return ('<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            "%s\n</head>\n<body>\n%s\n</body>\n</html>\n" % (HTMLLANG[lang], head, body))


def build():
    alldata = {l: load(l) for l in LANGS}
    written = []
    for lang in LANGS:
        data = alldata[lang]
        outdir = ROOT if lang == "es" else os.path.join(ROOT, lang)
        os.makedirs(outdir, exist_ok=True)
        for key in PAGE_ORDER:
            page = data["pages"][key]
            # TODAS las páginas se escriben como documento completo. La portada
            # en español era la única excepción: salía sin <!doctype>, sin
            # <html lang>, sin <meta charset> y sin <meta viewport>. Es un resto
            # de cuando el hosting viejo le ponía la cabecera por fuera. En un
            # hosting estático nadie se la pone, así que el navegador la abría
            # en modo antiguo y el celular la armaba a 999 px de ancho.
            html_out = render_page(lang, key, data, alldata, wrap=True)
            path = os.path.join(outdir, page["slug"])
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(html_out)
            written.append(os.path.relpath(path, ROOT))

    # sitemap
    urls = ""
    for lang in LANGS:
        for key in PAGE_ORDER:
            slug = alldata[lang]["pages"][key]["slug"]
            alts = "".join(
                '\n    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
                % (HREFLANG[l], abs_url(l, alldata[l]["pages"][key]["slug"])) for l in LANGS)
            urls += ('  <url>\n    <loc>%s</loc>%s\n    <lastmod>%s</lastmod>'
                     '\n    <changefreq>monthly</changefreq>'
                     '\n    <priority>%s</priority>\n  </url>\n'
                     % (abs_url(lang, slug), alts, HOY, PRIORIDAD[key]))
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap)
    written.append("sitemap.xml")

    # robots.txt — acompaña al interruptor PUBLICAR para que no queden en
    # desacuerdo (sitio público con robots.txt bloqueado, o al revés).
    if PUBLICAR:
        robots = ("# %s\nUser-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n"
                  % (CONFIG["marca"]["nombre"], DOMAIN))
    else:
        robots = (
            "# Vista previa interna de %s.\n"
            "# Este sitio TODAVIA NO debe indexarse: es una vista previa de revisión.\n"
            "# Para publicarlo, poner PUBLICAR = True en build/site_config.py y\n"
            "# volver a correr: python3 build/build.py\n\n"
            "User-agent: *\nDisallow: /\n\nSitemap: %s/sitemap.xml\n"
            % (CONFIG["marca"]["nombre"], DOMAIN))
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(robots)
    written.append("robots.txt")

    # config.js
    cfg = ("/* Datos editables del negocio — generado desde build/site_config.py */\n"
           "window.MCG_CONFIG = %s;\n\n"
           "window.MCG_WHATSAPP_LINK = function (mensaje) {\n"
           '  var base = "https://wa.me/" + window.MCG_CONFIG.contacto.whatsappDigitos;\n'
           '  var texto = encodeURIComponent(mensaje || "Hola MCG, vengo de la página web y quiero hacer una consulta");\n'
           '  return base + "?text=" + texto;\n};\n' % json.dumps(CONFIG, ensure_ascii=False, indent=2))
    with open(os.path.join(ROOT, "config.js"), "w", encoding="utf-8") as fh:
        fh.write(cfg)
    written.append("config.js")

    print("Generado: %d archivos" % len(written))
    for w in written:
        print("  " + w)


if __name__ == "__main__":
    build()
