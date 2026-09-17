# MCG Consultora — estado del sitio

## Resumen

El repositorio estaba **vacío** (cero commits). Ahora contiene el sitio
completo: los 28 HTML en tres idiomas, las imágenes, el formulario y el
generador en Python.

El sitio publicado en `https://www.mcgconsultora.com.py` está **incompleto**:
solo subió la home en español. Todo el resto responde 404.

## Qué hay publicado hoy en el hosting

**Responde 200:** `index.html` (español, versión vieja), `styles.css`,
`config.js`, `partials.js`, `robots.txt`, `404.html`, `form.js` y
`enviar.php` (responde 405 a GET, que es lo correcto: solo acepta POST, y
confirma que **el hosting ejecuta PHP**). De las imágenes, solo los 3 logos.

**Responde 404:**

- Las 8 páginas internas en español: contabilidad, estrategia tributaria, ERP,
  sociedades, extranjeros, equipo, contacto y preguntas frecuentes.
- Las 9 páginas en inglés (`en/`) y las 9 en portugués (`pt/`).
- `img/...oficina-cristina-rolon...jpg` — fondo del hero y también la imagen
  que se ve al compartir el link. Por eso el hero aparece azul plano.
- `img/...patron-monograma.png` — textura de fondo del CSS.
- `sitemap.xml`.

Además, el `index.html` que está publicado es **anterior** al del paquete: en
el menú dice "Estrategia tributa**i**a", error que el paquete ya tenía
corregido.

## Consecuencias de que falten esas páginas

1. **Un visitante con el navegador en inglés o portugués no ve nada del
   sitio.** `partials.js` detecta el idioma y redirige solo a `en/index.html`
   o `pt/index.html`. Como no están subidas, cae directo en un 404. Afecta
   justo al público extranjero al que apunta la consultora.

2. **No hay formulario de contacto.** Vive en `contacto.html`, que no está
   subida. Hoy solo funcionan el botón de WhatsApp y el mail.

3. **Todos los botones "Hablá con nosotros" llevan a un 404**, porque apuntan
   a `contacto.html`.

## Cambios hechos en este repositorio

Se agregó un interruptor de publicación en `build/site_config.py`:

```python
PUBLICAR = True   # True = sitio público | False = vista previa interna
```

Antes, el `noindex` y el banner de vista previa estaban escritos fijos dentro
de `build/build.py`, así que para publicar había que editarlos a mano en cada
página. Ahora el interruptor controla las tres cosas a la vez:

| | `PUBLICAR = True` | `PUBLICAR = False` |
|---|---|---|
| Etiqueta robots | `index, follow` | `noindex, nofollow` |
| Banner de vista previa | no se muestra | se muestra |
| `robots.txt` | `Allow: /` | `Disallow: /` |

El `robots.txt` ahora también lo genera el build, para que no pueda quedar en
desacuerdo con las páginas.

El sitio de este repositorio está regenerado con `PUBLICAR = True`. Verificado:
27 páginas con `index, follow`, ninguna con banner, 475 enlaces internos y 0
rotos. `404.html` conserva el `noindex`, que es lo correcto para una página de
error.

Para regenerar después de cualquier cambio:

```bash
python3 build/build.py
```

## Qué falta hacer

**Subir el contenido de este repositorio al `public_html` del hosting**, salvo
`build/` y `ESTADO.md`, que son de trabajo interno y no hacen falta en el
servidor. Respetando la estructura de carpetas: `en/` y `pt/` son carpetas, no
archivos sueltos.

Que `enviar.php` ya responda en el servidor confirma que el formulario va a
funcionar una vez que `contacto.html` esté arriba.

## Pendiente de verificar en el hosting

El formulario manda el correo con `From: no-reply@mcgconsultora.com.py` hacia
`mcgestudioc@gmail.com`. Si el dominio no tiene SPF configurado, Gmail puede
mandar esos avisos a spam o rechazarlos. Conviene hacer una prueba real de
envío después de subir y revisar también la carpeta de spam.

La casilla que recibe los avisos se cambia en `enviar.php`, en la variable
`$DESTINO`.
