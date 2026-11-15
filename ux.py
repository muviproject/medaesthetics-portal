"""Presentation layer. Source content and captured metrics remain in gen.py.

No approval is inferred from opening WhatsApp. No browser-side data is treated
as a shared record. Run python gen.py to rebuild all public pages.
"""
import html
import re
from urllib.parse import quote

E = html.escape
NAV = [('index.html', 'Resumen'), ('calendario.html', 'Calendario'),
       ('revision.html', 'Para revisar'), ('resultados.html', 'Resultados'),
       ('biblioteca.html', 'Biblioteca')]
GROUP = {'inicio.html': 'index.html', 'pendientes.html': 'revision.html',
         'anuncios.html': 'resultados.html', 'analitica.html': 'resultados.html',
         'competencia.html': 'resultados.html'}
LIBRARY = [('guiones.html', 'Guiones', '26 ideas de reels para preparar la filmación.'),
           ('graficas.html', 'Piezas gráficas', '15 piezas, con sus necesidades de producción.'),
           ('ofertas.html', 'Ofertas', 'Condiciones y precios, con las confirmaciones pendientes.'),
           ('encuestas.html', 'Encuestas', 'Preguntas para conversar con la comunidad.'),
           ('vallure.html', 'Archivo de Vallure', 'Contenido anterior para consultar y revisar.')]
DECISIONS = [
    ('precios', 'Confirmar precios de Black Friday', 'Rosanna',
     'Morpheus8: $1.750 confirmado el 10 nov. Falta confirmar láser $999 y QuantumRF $2.500 / $3.000.', 'ofertas.html'),
    ('filmacion', 'Definir la jornada de filmación', 'Rosanna y Daniel',
     'Elegir la fecha para grabar los reels pendientes con Rosanna.', 'guiones.html'),
    ('fotos', 'Revisar las fotos de antes y después', 'Rosanna',
     'Confirmar orden de las fotos y consentimiento para las piezas del 10, 17 y 28 nov.', 'graficas.html'),
    ('morpheus', 'Confirmar la oferta de Morpheus8', 'Rosanna',
     'El material anterior menciona 15% de descuento; Q4 indica $200 de descuento en la serie. Falta definir cuál rige.', 'ofertas.html'),
]


def money(n):
    return '$' + f'{n:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def link(href, text, primary=False):
    return f'<a class="ux-button{" primary" if primary else ""}" href="{E(href, quote=True)}">{E(text)}</a>'


def lead(kicker, title, description):
    return f'<header class="ux-heading"><p class="ux-eyebrow">{E(kicker)}</p><h1>{E(title)}</h1><p>{E(description)}</p></header>'


def section(content):
    return '<section class="ux-page"><div class="wrap">' + content + '</div></section>'


def decisions(limit=None):
    out = []
    for ident, title, owner, description, href in DECISIONS[:limit]:
        message = quote('Hola Daniel, sobre ' + title.lower() + ': ', safe='')
        out.append(f'''<article class="ux-decision" id="{ident}">
          <div><span class="ux-status">Por confirmar</span><h3>{E(title)}</h3>
          <p>{E(description)}</p><p class="ux-meta">Responsable: {E(owner)}</p></div>
          <div class="ux-actions">{link(href, 'Ver contexto')}
          <a class="ux-button primary" target="_blank" rel="noopener" href="https://wa.me/18456996606?text={message}">Responder por WhatsApp</a></div></article>''')
    return ''.join(out)


def dashboard(g):
    d = g['ADS_DATA']
    return section(lead('Med Aesthetics Miami · Noviembre 2026', 'Hola, Rosanna.',
                        'Las decisiones, el contenido y los resultados de tu marca, en un solo lugar.') + f'''
      <div class="ux-welcome"><div><span class="ux-eyebrow">El siguiente paso</span>
      <h2>Dejemos lista la próxima producción.</h2>
      <p>Precios, fecha de filmación y fotografías: estas confirmaciones ayudan a avanzar con el contenido.</p>
      {link('revision.html', 'Revisar pendientes', True)}</div>
      <aside><span class="ux-status">Contenido en revisión</span><p>La publicación de cada pieza requiere tu aprobación.</p>
      <span class="ux-meta">Plan disponible: 10–30 nov 2026</span></aside></div>
      <div class="ux-section-title"><h2>Necesitamos tu respuesta</h2>{link('revision.html', 'Ver todas')}</div>
      {decisions(2)}
      <div class="ux-section-title"><h2>Tu contenido de noviembre</h2></div>
      <div class="ux-links"><a href="calendario.html"><span>01 · Planificación</span><h3>Calendario</h3><p>Consulta las piezas y lo que falta para producirlas.</p></a>
      <a href="guiones.html"><span>02 · Producción</span><h3>Guiones de reels</h3><p>Revisa las ideas y el contenido para la filmación.</p></a>
      <a href="graficas.html"><span>03 · Diseño</span><h3>Piezas gráficas</h3><p>Consulta los diseños disponibles y sus detalles.</p></a></div>
      <div class="ux-section-title"><h2>Resultados, a primera vista</h2>{link('resultados.html', 'Ver resultados')}</div>
      <p class="ux-meta">Meta Ads · {E(d['rango'])} · Lectura: {E(d['actualizado'])}</p>
      <div class="ux-stats"><div><span>Inversión en anuncios</span><strong>{money(d['gasto_total'])}</strong></div>
      <div><span>Contactos registrados en Meta</span><strong>{d['leads_total']}</strong></div>
      <div><span>Citas confirmadas</span><strong>Sin dato</strong></div></div>
      <p class="ux-meta">Los contactos registrados no equivalen a citas ni ventas confirmadas. Estos valores corresponden al periodo indicado.</p>''')


def review():
    return section(lead('Decisiones y aprobaciones', 'Para revisar', 'Primero, las confirmaciones que necesita el equipo para avanzar.') + '''
      <p class="ux-callout">Las respuestas se envían por WhatsApp. Abrir el mensaje no registra una aprobación: envíalo y el equipo confirmará el estado.</p>
      ''' + decisions() + '''<div class="ux-section-title"><h2>Revisar el contenido</h2></div>
      <div class="ux-actions">''' + link('calendario.html', 'Piezas del calendario') + link('guiones.html', 'Guiones') + link('graficas.html', 'Diseños') + '''</div>
      <details class="ux-disclosure"><summary>Otros pendientes y antecedentes</summary><p>Consulta también accesos a redes, publicaciones anteriores y material de archivo.</p>''' + link('pendientes.html', 'Ver listado completo') + '</details>')


def results(g):
    d = g['ADS_DATA']
    return section(lead('Seguimiento de marketing', 'Resultados', 'Cada fuente conserva su periodo y su fecha de lectura. Los contactos y las acciones web son medidas diferentes.') + f'''
      <article class="ux-result"><div class="ux-section-title"><div><span class="ux-eyebrow">Publicidad · Meta Ads</span><h2>Inversión y contactos</h2></div>{link('anuncios.html', 'Ver anuncios')}</div>
      <p class="ux-meta">{E(d['rango'])} · Lectura: {E(d['actualizado'])}</p>
      <div class="ux-stats"><div><span>Inversión</span><strong>{money(d['gasto_total'])}</strong></div>
      <div><span>Contactos registrados</span><strong>{d['leads_total']}</strong></div>
      <div><span>Coste por contacto</span><strong>{money(d['gasto_total']/d['leads_total']) if d['leads_total'] else 'Sin dato'}</strong></div></div>
      <p>El siguiente paso es comprobar cuántos contactos llegaron a una cita. No hay un dato confirmado de ventas en este informe.</p></article>
      <article class="ux-result"><div class="ux-section-title"><div><span class="ux-eyebrow">Sitio web · Google Analytics</span><h2>Visitas e interés</h2></div>{link('analitica.html', 'Ver analítica web')}</div>
      <p class="ux-meta">Consulta las ventanas de 30 y 90 días en el informe · Lectura: 14 nov 2026 · Datos hasta el 13 nov</p>
      <p>Las acciones de reserva o contacto miden actividad en la web. Una persona puede realizar varias acciones; no son citas confirmadas.</p></article>
      <article class="ux-result"><div class="ux-section-title"><div><span class="ux-eyebrow">Instagram · Referencias de mercado</span><h2>Contexto de la competencia</h2></div>{link('competencia.html', 'Ver comparación')}</div>
      <p class="ux-meta">Medición publicada: 10 nov 2026 · Incluye estimaciones de fechas anteriores</p>
      <p>La comparación orienta la investigación. Las muestras y los métodos son distintos; el orden del ranking todavía necesita validación.</p></article>''')


def library():
    cards = ''.join(f'<a href="{href}"><span>Material de trabajo</span><h3>{title}</h3><p>{desc}</p></a>' for href, title, desc in LIBRARY)
    return section(lead('Contenido y archivo', 'Biblioteca', 'Todo el material sigue disponible, organizado por lo que necesitas consultar.') + '<div class="ux-links">' + cards + '</div>')


def ads_report(g, original):
    d = g['ADS_DATA']
    body = lead('Publicidad · Meta Ads', 'Anuncios, con contexto', 'Resultados observados en el periodo. La evaluación no cambia campañas ni presupuestos.')
    body += f'<p class="ux-meta">Periodo: {E(d["rango"])} · Lectura: {E(d["actualizado"])}</p>'
    body += f'<div class="ux-stats"><div><span>Inversión total</span><strong>{money(d["gasto_total"])}</strong></div><div><span>Contactos registrados</span><strong>{d["leads_total"]}</strong></div><div><span>Citas confirmadas</span><strong>Sin dato</strong></div></div>'
    body += '<p class="ux-callout">Un contacto aislado no demuestra rendimiento estable. Las diferencias entre públicos y periodos son señales para investigar, no una explicación confirmada.</p>'
    body += '<h2>Qué revisar a continuación</h2><ol class="ux-next"><li>Confirmar con la clínica cuántos contactos llegaron a una cita.</li><li>Revisar la medición y el recorrido después del clic.</li><li>Comparar periodos equivalentes antes de decidir cambios.</li></ol>'
    for campaign in d['campanas']:
        enabled = campaign['estado'] == 'ENCENDIDA'
        contacts = f'{campaign["leads"]} contactos' if campaign['leads'] is not None else 'Contactos: sin dato en la fuente'
        cost = money(campaign['gasto']/campaign['leads']) if campaign['leads'] else 'No calculable con los datos disponibles'
        body += f'<details class="ux-campaign" {"open" if enabled else ""}><summary>{E(campaign["nombre"])}<span class="ux-meta">{"Encendida" if enabled else "Apagada"} en la lectura · {money(campaign["gasto"])} · {contacts}</span></summary>'
        body += f'<p class="ux-meta">{campaign["impresiones"]:,} impresiones · {campaign["clics"]} clics · Coste por contacto: {cost}</p>'
        body += '<div class="grid">'
        for ad in campaign['avisos']:
            leads = ad.get('leads')
            if ad.get('sin_datos'):
                evaluation = 'Sin datos en el periodo'
            elif leads:
                evaluation = 'Contactos registrados · señal por validar'
            else:
                evaluation = 'Sin contactos registrados en el periodo'
            image = f'<div class="thumbs one"><img src="assets/vallure/{E(ad["img"])}" loading="lazy" alt="Referencia visual de {E(ad["t"], quote=True)}"></div>' if ad.get('img') else ''
            body += f'<article class="card"><span class="badge">{E(ad["ad"])}</span><h3>{E(ad["t"])}</h3><p>{E(ad["d"])}</p>{image}<p class="ux-status">{evaluation}</p>'
            if ad.get('pausado'):
                body += f'<p class="ux-meta">Pausado el {E(ad["pausado"])}</p>'
            if not ad.get('sin_datos'):
                body += f'<div class="adnums"><b>Inversión:</b> {money(ad["spend"])}<br><b>Contactos registrados:</b> {leads if leads is not None else "Sin dato"}<br><b>Impresiones:</b> {ad["seen"]} · <b>Clics:</b> {ad["clicks"]}</div>'
            body += '<details class="ux-disclosure"><summary>Ver datos y contexto</summary>'
            if not ad.get('sin_datos'):
                body += f'<p>Alcance: {ad["reach"]} personas · CTR: {E(str(ad.get("ctr") or "Sin dato"))} · Coste por clic: {money(ad["cpc"]) if ad.get("cpc") is not None else "Sin dato"}.</p>'
            if ad.get('img_note'):
                body += f'<p class="ux-meta">{E(ad["img_note"])}</p>'
            body += '<p class="ux-meta">La atribución registrada en Meta no confirma una cita o venta. Hace falta seguimiento con la clínica.</p></details></article>'
        body += '</div>'
        if campaign.get('nota'):
            body += f'<p class="ux-callout">{E(campaign["nota"])}</p>'
        paused = campaign.get('pausados_con_gasto', [])
        if paused:
            body += '<details class="ux-disclosure"><summary>Otros avisos pausados con gasto</summary><ul>' + ''.join(f'<li>{E(a["ad"])} · {money(a["spend"])} · {a["seen"]} impresiones · {a["clicks"]} clics</li>' for a in paused) + '</ul></details>'
        if campaign.get('pausados_sin_gasto'):
            body += '<p class="ux-meta">Pausados sin gasto: ' + E(', '.join(campaign['pausados_sin_gasto'])) + '.</p>'
        body += '</details>'
    # Retain previous explanations in a clearly separated historical record.
    body += '<details class="ux-disclosure"><summary>Informe anterior y registro de cambios</summary><p class="ux-callout">Archivo de la lectura del 15 nov 2026. Conserva las etiquetas y recomendaciones originales; no son nuevas instrucciones ni cambios aplicados.</p>' + original + '</details>'
    return section(body)


def navigation(filename):
    active = GROUP.get(filename, filename if filename in dict(NAV) else 'biblioteca.html')
    links = ''.join(f'<a href="{href}"' + (' class="active" aria-current="page"' if href == active else '') + f'>{label}</a>' for href, label in NAV)
    return '<nav class="nav" aria-label="Navegación principal"><div class="wrap">' + links + '</div></nav>'


def compact_cards(content):
    """Move secondary content behind a native disclosure, with no JS dependency."""
    def compact(m):
        card = m.group(0)
        # Preserve image previews on the card, keep decisions and detailed text together.
        thumbs = re.findall(r'<div class="thumbs[^"]*">.*?</div>', card, re.S)
        for t in thumbs:
            card = card.replace(t, '')
        if '<div class="approve">' not in card:
            return card
        cut = re.search(r'<div class="(?:note|need|adapt|approve)">', card)
        if not cut:
            return card
        intro, detail = card[:cut.start()], card[cut.start():-10]
        return intro + ''.join(thumbs) + '<span class="ux-status">Borrador · por revisar</span><details class="ux-disclosure"><summary>Revisar pieza y responder</summary>' + detail + '<p class="ux-meta">La respuesta se envía por WhatsApp; el portal no la registra automáticamente.</p></details></article>'
    return re.sub(r'<article\b[^>]*>.*?</article>', compact, content, flags=re.S)


def enhance(pages, g):
    template = pages['index.html']
    # Header/login/footer are retained from the existing generator.
    nav_end = template.index('</nav>') + len('</nav>')
    footer_start = template.index('<footer>')
    head, tail = template[:nav_end], template[footer_start:]
    pages['calendario.html'] = pages['index.html']
    ads_old = g['anuncios_rows']()
    pages['anuncios.html'] = head + ads_report(g, ads_old) + tail
    for filename, content in [('index.html', dashboard(g)), ('inicio.html', dashboard(g)),
                              ('revision.html', review()), ('resultados.html', results(g)),
                              ('biblioteca.html', library())]:
        pages[filename] = head + content + tail
    labels = dict(NAV, **{'inicio.html': 'Resumen', 'anuncios.html': 'Anuncios'})
    for filename, page in list(pages.items()):
        page = re.sub(r'<nav class="nav">.*?</nav>', navigation(filename), page, count=1, flags=re.S)
        page = page.replace('</head>', '<link rel="stylesheet" href="ux.css">\n</head>')
        page = page.replace('</body>', '<script src="ux.js" defer></script>\n</body>')
        start = page.index('</nav>') + len('</nav>')
        end = page.index('<footer>')
        content = page[start:end]
        if filename in ('calendario.html', 'graficas.html', 'ofertas.html', 'vallure.html'):
            content = compact_cards(content)
        # Each route has a meaningful visible main heading.
        if '<h1' not in content:
            content = content.replace('<h2', '<h1', 1).replace('</h2>', '</h1>', 1)
        if filename not in ('index.html', 'inicio.html', 'revision.html', 'resultados.html', 'biblioteca.html'):
            group = GROUP.get(filename, 'calendario.html' if filename == 'calendario.html' else 'biblioteca.html')
            content = f'<div class="wrap ux-breadcrumb"><a href="{group}">{dict(NAV)[group]}</a><span aria-hidden="true"> / </span><span>{E(next((p[2] for p in g["PAGES"] if p[0] == filename), "Calendario"))}</span></div>' + content
        page = page[:start] + '<main id="contenido">' + content + '</main>' + page[end:]
        page = page.replace('<body>', '<body><a class="skip-link" href="#contenido">Saltar al contenido</a>', 1)
        if filename in labels:
            page = re.sub(r'<title>.*?</title>', '<title>' + labels[filename] + ' · Med Aesthetics Miami</title>', page, count=1)
        page = page.replace('Vista previa', 'Ver detalle')
        page = page.replace('Se actualiza una vez por día.', 'Consulta la fecha de lectura de cada informe.')
        page = page.replace('Los números son reales, leídos en Ads Manager, y se actualizan una vez por día.', 'Datos registrados en Ads Manager. Consulta el periodo y la fecha de lectura del informe.')
        page = page.replace('Próxima actualización: diaria.', 'Próxima lectura: pendiente de confirmar.')
        page = page.replace('<b>Borradores — nada se publica sin la aprobación de Rosanna.</b>', '<b>Med Aesthetics Miami · Tu espacio de trabajo con MuViProject</b>')
        if filename == 'analitica.html':
            page = page.replace('694 reservas', '694 acciones de reserva o contacto').replace('66 reservas', '66 acciones de reserva o contacto').replace('22 reservas', '22 acciones de reserva o contacto')
            page = page.replace('reservas (1.348)', 'acciones de reserva o contacto (1.348)')
            page = page.replace('menos reservas que', 'menos acciones de reserva o contacto que').replace('más reserva.', 'más acciones de reserva o contacto registra.')
            page = page.replace('concentran las reservas:', 'concentran las acciones de reserva o contacto:')
        if filename == 'competencia.html':
            page = page.replace('Top 10 nacional por interacción', '10 referencias nacionales · ranking por validar')
            page = page.replace('Ordenado por interacción mediana por post', 'Listado original: combina medianas medidas y promedios estimados. Fórmula de interacción por post')
            page = re.sub(r'<h3 class="sub">Actualización semanal</h3>.*?(?=</div></section>)', '<h3 class="sub">Fecha y próxima revisión</h3><p>Última medición publicada: 10-nov-2026. La próxima revisión debe comparar ventanas y métodos equivalentes; su fecha está pendiente de confirmar.</p>', page, flags=re.S)
        pages[filename] = page
    return pages
