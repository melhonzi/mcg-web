# MCG Consultora — estado del sitio

Relevamiento de lo que está publicado en `https://www.mcgconsultora.com.py`.

Este repositorio estaba **vacío** (cero commits). Los archivos de este commit
fueron **rescatados descargándolos del hosting**, que hasta ahora era la única
copia existente del sitio.

## Qué está publicado y funciona

| Archivo | Estado |
|---|---|
| `index.html` (español) | OK — 27 KB, página completa |
| `styles.css` | OK — 24 KB |
| `config.js` | OK — datos del negocio |
| `partials.js` | OK — menú, FAQ, idioma |
| `img/...logo-dorado.png` | OK |
| `img/...logo-blanco.png` | OK |
| `img/...logo-oficial-cuadrado.jpg` | OK |
| `robots.txt` | OK |

## Qué falta subir (responde 404)

**Páginas internas** — las 8 están enlazadas desde el menú, el footer y los
botones de la home, pero ninguna existe en el servidor:

- `contabilidad-empresarial.html`
- `estrategia-tributaria.html`
- `constitucion-sociedades.html`
- `empresarios-extranjeros.html`
- `implementacion-erp-contable.html`
- `direccion-equipo.html`
- `contacto.html`
- `preguntas-frecuentes.html`

**Versiones en otros idiomas** — `en/` y `pt/` completas (el selector ES/EN/PT
del menú apunta a ellas).

**Imágenes**

- `img/mcg-consultora-contable-oficina-cristina-rolon-asuncion-paraguay.jpg`
  — foto de fondo del hero; también es la imagen que se muestra al compartir el
  link (`og:image`). Por eso el hero se ve azul plano.
- `img/mcg-consultora-contable-patron-monograma.png` — textura de fondo del CSS.

**Otros**

- `sitemap.xml` — declarado en `robots.txt` pero no existe.
- `favicon.ico`.

## Problemas detectados

1. **Redirección de idioma a páginas que no existen.** `partials.js` detecta el
   idioma del navegador y redirige solo con `en/index.html` o `pt/index.html`.
   Como esas páginas no están subidas, un visitante con el navegador en inglés o
   portugués cae directo en un 404 y no ve nada del sitio. Afecta justamente al
   público extranjero al que apunta la consultora.

2. **No hay formulario de contacto.** El único formulario vivía en
   `contacto.html`, que no está subida. Hoy los únicos canales que funcionan son
   el botón de WhatsApp y el mail. `config.js` ya trae los textos de respuesta
   del formulario, así que el formulario estaba previsto pero nunca llegó al
   servidor.

3. **El sitio está bloqueado para Google.** Es intencional mientras sea vista
   previa, pero hay que revertirlo al publicar:
   - `robots.txt` tiene `Disallow: /`
   - cada HTML tiene `<meta name="robots" content="noindex, nofollow">`

4. **Banner de vista previa visible** en producción: "Vista previa interna — no
   indexada — datos sujetos a confirmación antes de publicar".

5. **Error de tipeo en el menú:** dice "Estrategia tributaia" (falta la `r`).

6. **Footer con año 2026.**

## Nota sobre el origen de los archivos

`config.js` arranca con el comentario `generado desde build/site_config.py`: el
proyecto original tenía un generador en Python que tampoco está en este
repositorio. Sin él, los archivos fuente completos siguen estando solo en la
máquina donde se creó el sitio.
