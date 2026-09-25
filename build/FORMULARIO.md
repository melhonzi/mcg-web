# Cómo queda enganchado el formulario de contacto

## Por qué hace falta esto

El sitio vive en GitHub Pages, que solo sabe **mostrar** páginas: no sabe
**hacer** cosas. Mandar un correo es "hacer algo". En el hosting viejo lo
hacía `enviar.php`; en GitHub ese archivo está pero nadie lo ejecuta.

La solución es un ayudante gratuito dentro de la cuenta de Google de MCG
(Google Apps Script). Recibe lo que la persona completó y:

1. lo **guarda en una planilla** de Google (se crea sola la primera vez);
2. **manda el correo** a `mcgestudioc@gmail.com`, con "responder" apuntando
   a la persona que escribió;
3. **avisa por WhatsApp** al +595 981 579250.

Se guarda **primero**. Si fallara el correo o el WhatsApp, la consulta ya
quedó anotada: no se pierde ninguna.

Ventaja de este camino: nada pasa por una empresa de afuera, el correo sale
de la propia casilla de MCG, y no hay tope de consultas que importe.

---

## Parte A — la llave del WhatsApp (5 minutos)

El aviso por WhatsApp lo entrega un servicio gratuito llamado **CallMeBot**.
Es confiable pero **no es oficial de WhatsApp**: si algún día deja de andar,
el correo y la planilla siguen llegando igual.

1. Abrir <https://www.callmebot.com/blog/free-api-whatsapp-messages/>
2. Esa página dice a qué número de WhatsApp hay que escribirle y con qué
   frase exacta (algo como *"I allow callmebot to send me messages"*). El
   número lo cambian cada tanto, por eso hay que leerlo ahí y no confiar en
   un número anotado en otro lado.
3. **Escribir esa frase desde el WhatsApp de MCG (+595 981 579250)**, que es
   el que va a recibir los avisos.
4. Contestan con una **llave** (`apikey`), una tira de números. Guardala.

Si el WhatsApp no interesa, saltear esta parte: dejar `CALLMEBOT_APIKEY`
vacío y el ayudante hace el correo y la planilla igual.

---

## Parte B — publicar el ayudante (5 minutos)

1. Entrar a <https://script.google.com> con la cuenta de Google de MCG y
   apretar **Nuevo proyecto**.
2. Borrar todo lo que aparece en el recuadro de código y **pegar entero** el
   contenido de `build/formulario-google.gs`.
3. En la línea que dice `var CALLMEBOT_APIKEY = '';` pegar la llave de la
   Parte A entre las comillas. Si no se hizo esa parte, dejarla vacía.
4. Ponerle nombre al proyecto arriba a la izquierda (por ejemplo
   *Formulario MCG*) y guardar con el ícono del disquete.
5. Arriba a la derecha: **Implementar → Nueva implementación**. Apretar el
   engranaje y elegir **Aplicación web**. Después:
   - *Ejecutar como*: **Yo**
   - *Quién tiene acceso*: **Cualquier persona** ← esto es imprescindible;
     el formulario lo completa gente de la calle, que no tiene cuenta de
     Google. Aunque diga "cualquier persona", lo único que puede hacer es
     dejar una consulta: no ve la planilla ni el correo.
   - **Implementar**
6. La primera vez Google pide permiso: **Autorizar acceso** → elegir la
   cuenta → *Configuración avanzada* → *Ir a Formulario MCG (no seguro)* →
   **Permitir**. Ese aviso de "no seguro" sale porque el programa es propio
   y Google no lo revisó; es normal y esperable.
7. Copiar la **URL de la aplicación web**. Termina en `/exec` y se ve así:
   `https://script.google.com/macros/s/AKfycb.../exec`

**Para comprobar que quedó vivo:** pegar esa dirección en el navegador. Tiene
que contestar algo como `{"ok":true,"mensaje":"Ayudante del formulario de MCG
funcionando." ...}`. Si contesta eso, está listo.

---

## Parte C — enchufarlo al sitio

Esa dirección va en `build/site_config.py`:

```python
"formulario": {
    "endpoint": "https://script.google.com/macros/s/AKfycb.../exec",
},
```

y después se regenera el sitio con `python3 build/build.py`.

**Mientras el `endpoint` esté vacío**, el formulario ni intenta mandar nada:
va derecho al camino de WhatsApp, que es lo que hace hoy. O sea que el sitio
nunca queda esperando una dirección que todavía no existe.

---

## Qué ve la persona que completa el formulario

| Qué pasó | Qué ve |
|---|---|
| El ayudante recibió la consulta | *"Recibimos tu consulta. Te vamos a responder al correo que dejaste."* y un botón para seguir por WhatsApp si prefiere |
| El ayudante no contesta (o no hay `endpoint`) | Se le arma el mensaje y se le abre WhatsApp para que lo mande él |

Nunca se le muestra un *"enviado con éxito"* que no pasó.

---

## Detalles que conviene saber

- **La trampa anti-robot.** El formulario tiene un campo escondido
  (`sitioWeb`) que una persona nunca ve. Los robots lo completan. Si viene
  lleno, el ayudante contesta que sí y tira la consulta a la basura, sin
  guardarla ni avisar.
- **Techo de 40 correos por hora.** Es un freno por si un robot quiere
  inundar la casilla. Pasado el techo la consulta **se sigue guardando en la
  planilla**; lo único que no sale es el correo. Se cambia en la línea
  `TECHO_POR_HORA`.
- **Si se cambia el código del ayudante**, hay que volver a
  *Implementar → Administrar implementaciones → editar (el lápiz) → Versión:
  Nueva versión → Implementar*. Guardar solo con el disquete **no** actualiza
  lo que está publicado. La dirección `/exec` no cambia.
- **`enviar.php` quedó sin uso** desde la mudanza a GitHub. No se borró:
  sirve si algún día el sitio vuelve a un hosting con PHP.
