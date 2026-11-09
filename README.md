# Med Aesthetics Miami — Portal del cliente (MuViProject)

Portal visual para Rosanna Bermejo (Med Aesthetics Miami): calendario 10–30 nov 2026,
banco de 26 guiones de reels, 15 piezas gráficas y ofertas Q4 verificadas.
Todo es BORRADOR: nada se publica sin la aprobación de Rosanna.

## Acceso (contraseña simple)

El portal pide email + contraseña antes de mostrar el contenido.

- **Email aceptado:** cualquier `@medaestheticsmiami.com` (sugerido: `info@medaestheticsmiami.com`).
- **Contraseña actual:** `MedAesthetics2026`

### Cómo cambiar la contraseña

Editar en `index.html`, al inicio del archivo (bien visible, con el comentario
`CONFIGURACIÓN DEL ACCESO`):

```js
var PORTAL_PASSWORD = "MedAesthetics2026";
```

Cambiar el valor entre comillas, hacer commit y push. No hay nada más que tocar.

> **Aviso honesto:** esta contraseña es una **cortina visual, no seguridad real**.
> Al ser un sitio estático (GitHub Pages), cualquiera que lea el código fuente
> puede verla. Para acceso protegido de verdad, usar Cloudflare Access
> (gratis, con código por email) en lugar de esta contraseña.

## Imágenes

El portal funciona con o sin imágenes. Si existen, las usa; si no, muestra un
gradiente con los colores de marca (no se rompe nada):

- `assets/hero.png` — foto principal del hero (portada).
- `assets/flatlay.png` — imagen de la sección de piezas gráficas.
- `assets/texture.png` — imagen de la banda de la sección de ofertas.

Las imágenes llegan aparte (desde ChatGPT) y se suben a `assets/` con esos
nombres exactos. No usar fotos reales de pacientes ni antes/después sin
consentimiento.

## Estructura

- `index.html` — todo el portal, autocontenido (CSS/JS inline, sin CDN, sin
  Google Fonts, sin imágenes externas). Stack de fuentes del sistema.
- `assets/` — solo las 3 imágenes opcionales de arriba.

## Publicación

- Repo: `muviproject/medaesthetics-portal` (organización `muviproject`).
- GitHub Pages: rama `main`, raíz.
- URL pública: https://muviproject.github.io/medaesthetics-portal/
- Subdominio previsto (DNS en Namecheap, lo hace Daniel): CNAME
  `medaesthetics.muviproject.com` → `muviproject.github.io`.

## Aprobaciones

El sitio estático no guarda aprobaciones. Cada pieza tiene un botón
"Aprobar por WhatsApp" que abre WhatsApp a Daniel (+1 845-699-6606) con el
mensaje prellenado. La aprobación sigue siendo por WhatsApp, como hasta ahora.

### Comentarios (feedback)

Cada pieza tiene además una cajita "Escribí tu comentario sobre esta pieza…"
con un botón "Enviar comentario por WhatsApp". Si la cajita está vacía, el
portal pide que se escriba algo y no abre nada. Si tiene texto, abre WhatsApp
a Daniel con el mensaje prellenado `Sobre [nombre de la pieza]: [comentario]`,
con el mismo nombre de pieza que usa el botón de aprobar. Como con las
aprobaciones, nada se envía solo: el mensaje se manda solo cuando Rosanna
pulsa Enviar en WhatsApp. El portal no guarda comentarios.

### Redes: cápsulas de color

Donde se publica cada pieza se muestra con cápsulas con el color de cada
marca (definidas una sola vez en el CSS: `.net-ig` gradiente de Instagram,
`.net-fb` #1877F2, `.net-tt` negro con borde cian #25F4EE y acento rojo
#FE2C55, `.net-yt` #FF0000). Para cambiar un color, se edita esa clase en
`index.html`; todo el portal usa la misma definición.

### Vista previa (popup)

Cada pieza tiene un botón "Vista previa" que abre un modal con el detalle
completo de esa pieza (título, fecha, formato, redes, estado y, según el
tipo, hook + cuerpo + CTA + caption, o descripción y qué falta), con los
botones de aprobar y de feedback de esa pieza adentro. Cierra con la X, con
clic fuera del popup, o con Escape; mientras está abierto, el fondo no hace
scroll. En el celular el modal es una lámina de ~94vw y ~90vh, con el botón
de cerrar grande y alcanzable.
