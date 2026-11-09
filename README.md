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

- `assets/hero.jpg` — foto principal del hero (portada).
- `assets/flatlay.jpg` — imagen de la sección de piezas gráficas.
- `assets/texture.jpg` — imagen de la banda de la sección de ofertas.

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
