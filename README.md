# Med Aesthetics Miami — Portal del cliente

Espacio de trabajo para Rosanna y MuViProject. GitHub Pages, rama main, raíz.
UX actualizada el 15-nov-2026; las métricas conservan sus fechas originales.

## Generar

Python 3, sin dependencias externas: `python -B gen.py`.

`gen.py` contiene el contenido, las métricas y el acceso existentes. `ux.py`
organiza las páginas; `ux.css` y `ux.js` son compartidos. Editar las fuentes
y regenerar; no editar solamente los HTML que reemplaza el siguiente build.

## Navegación

- Resumen: `index.html` e `inicio.html`.
- Calendario: `calendario.html`, piezas del 10–30 nov 2026.
- Para revisar: `revision.html`; listado original en `pendientes.html`.
- Resultados: `resultados.html`, enlaza anuncios, analítica y competencia.
- Biblioteca: `biblioteca.html`, enlaza guiones, gráficas, ofertas, encuestas y Vallure.

Las páginas anteriores siguen accesibles. La antigua portada-calendario está
ahora en `calendario.html`. `assets/` conserva las imágenes originales.

## Estados y aprobaciones

Las piezas siguen en borrador. Las confirmaciones se envían por WhatsApp:
abrir un enlace no envía el mensaje ni registra una aprobación. No hay base
de datos compartida de estados. No inventar aprobaciones ni publicaciones.
Las prioridades se definen en `ux.py` (`DECISIONS`); actualizar también las
fuentes cuando Rosanna o Daniel confirmen una decisión.

## Métricas

Son capturas fechadas, no consultas en vivo. Los anuncios usan `ADS_DATA`;
el resumen calcula el coste por contacto desde los totales de esa captura.
El informe anterior permanece desplegable como archivo. Las acciones GA4
no son citas ni ventas y no deben sumarse a los contactos de Meta.
Al actualizar las fuentes, revisar también los periodos en `ux.py`.
No hay actualización automática configurada en este repo; cualquier proceso
externo debe verificarse aparte.

## Acceso y publicación

Se conserva la cortina de acceso original y sus credenciales en `gen.py`.
Es una cortina visual, no autenticación de servidor. No se añadieron usuarios,
permisos ni servicios externos. Antes de publicar: regenerar, revisar enlaces,
navegación, modal y filtros en móvil y escritorio. El contenido social sigue
requiriendo la aprobación de Rosanna.
