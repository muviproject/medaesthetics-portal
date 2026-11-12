# Med Aesthetics Miami — Portal del cliente (MuViProject)

Portal visual para Rosanna Bermejo (Med Aesthetics Miami): calendario 10–30 nov 2026,
banco de 26 guiones de reels, 15 piezas gráficas y ofertas Q4 verificadas.
Todo es BORRADOR: nada se publica sin la aprobación de Rosanna.
Regla de publicación: cada pieza se adapta y se publica en todas las
plataformas que aceptan su formato (reel → Reels/Shorts; carrusel →
carrusel de fotos; estática → foto o Comunidad).

## Contenido de Vallure — para aprobar (10-nov-2026)

Sección con todo lo que hizo Vallure Agency y está publicado o corriendo:
10 anuncios de Meta Ads (lo visible en la Biblioteca de Anuncios) y
49 posteos orgánicos de Instagram (29-may a 29-oct-2026). Cada tarjeta
lleva su texto y el link al original para ver el visual, con los botones
de aprobar, vista previa y feedback de siempre.
Detalle y limitaciones en
`../med-aesthetics-materiales/inventario-anuncios-vallure.md`: la cuenta
publicitaria no está habilitada para Ads MCP (sin acceso por API a las
49 campañas) y los visuales no se pudieron descargar desde el entorno
(la Biblioteca devuelve 403; instagram-cli no expone las imágenes).

## Acceso (contraseña simple)

El portal pide email + contraseña antes de mostrar el contenido.

- **Email aceptado:** cualquier `@medaestheticsmiami.com` (sugerido: `info@medaestheticsmiami.com`).
- **Contraseña actual:** `MedAesthetics2026`

### Cómo cambiar la contraseña

Editar en `gen.py` (constante `PORTAL_PASSWORD` dentro del TPL, bien visible,
con el comentario `CONFIGURACIÓN DEL ACCESO`) y regenerar (`python3 gen.py`):

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

- Páginas (todas autocontenidas: CSS/JS inline, sin CDN, sin Google
  Fonts, sin imágenes externas; stack de fuentes del sistema). Todas
  llevan el mismo menú superior (siempre visible, también en el celular)
  y la misma puerta de acceso con contraseña:
  - `index.html` — Calendario 10–30 nov (la landing, la que se abre al
    entrar al portal).
  - `inicio.html` — Bienvenida + «Por qué Med Aesthetics Miami».
  - `guiones.html` — Banco de 26 guiones de reels.
  - `graficas.html` — 15 piezas gráficas.
  - `ofertas.html` — Ofertas Q4 verificadas + Black Friday.
  - `vallure.html` — Contenido de Vallure (10 anuncios + 49 posts).
  - `encuestas.html` — 5 encuestas compañeras propuestas.
  - `pendientes.html` — Pendientes de confirmación.
  Para agregar una página: una línea en `PAGES` de `gen.py` + su sección
  en el TPL con marcadores `<!-- PAGE:X-START -->` / `<!-- PAGE:X-END -->`.
- `assets/` — solo las 3 imágenes opcionales de arriba + `assets/vallure/`
  (visuales embebidos del contenido de Vallure).

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
marca (definidas una sola vez en el CSS de `gen.py`: `.net-ig` gradiente de
Instagram, `.net-fb` #1877F2, `.net-tt` negro con borde cian #25F4EE y
acento rojo #FE2C55, `.net-yt` #FF0000). Para cambiar un color, se edita
esa clase en `gen.py` y se regenera; todo el portal usa la misma definición.

### Vista previa (popup)

Cada pieza tiene un botón "Vista previa" que abre un modal con el detalle
completo de esa pieza (título, fecha, formato, redes, estado y, según el
tipo, hook + cuerpo + CTA + caption, o descripción y qué falta), con los
botones de aprobar y de feedback de esa pieza adentro. Cierra con la X, con
clic fuera del popup, o con Escape; mientras está abierto, el fondo no hace
scroll. En el celular el modal es una lámina de ~94vw y ~90vh, con el botón
de cerrar grande y alcanzable.
