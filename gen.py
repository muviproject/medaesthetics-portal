# -*- coding: utf-8 -*-
"""Genera index.html (autocontenido) + README.md del portal Med Aesthetics Miami."""
import html as H
from urllib.parse import quote

WA = "https://wa.me/18456996606?text="
def wa(msg):
    return WA + quote(msg, safe="")

def esc(s):
    return H.escape(s, quote=True)

def fb(piece):
    """Bloque de feedback por WhatsApp para una pieza: cajita + botón.

    El nombre de la pieza es el mismo que usa el botón de aprobar de esa
    pieza. El JS (mamFeedback) abre WhatsApp con el mensaje prellenado
    "Sobre [pieza]: [comentario]"; nada se envía solo.
    """
    return ('<div class="fb"><textarea rows="2" placeholder="Escribí tu comentario sobre esta pieza…"></textarea>'
            '<button type="button" class="fb-btn" data-piece="%s" onclick="mamFeedback(this)">Enviar comentario por WhatsApp</button></div>' % esc(piece))

NETS = {
    "IG": ("Instagram", "net-ig"),
    "Instagram": ("Instagram", "net-ig"),
    "FB": ("Facebook", "net-fb"),
    "Facebook": ("Facebook", "net-fb"),
    "TikTok": ("TikTok", "net-tt"),
    "YT": ("YouTube", "net-yt"),
    "YouTube": ("YouTube", "net-yt"),
}
def nets_pills(redes):
    """Convierte 'IG + FB + TikTok + YouTube' en cápsulas con el color de cada marca.

    El color se define una sola vez en el CSS (.net-ig, .net-fb, .net-tt,
    .net-yt). No cambia qué redes lleva cada pieza, solo cómo se muestran.
    """
    if not redes or redes.strip() in ("—", "-"):
        return ""
    out = []
    for tok in redes.split("+"):
        tok = tok.strip()
        if tok in NETS:
            label, cls = NETS[tok]
            out.append('<span class="net %s">%s</span>' % (cls, label))
    return '<div class="nets">%s</div>' % "".join(out) if out else ""

def pv_btn():
    """Botón 'Vista previa': abre el modal con el detalle completo de la pieza."""
    return ('<div class="pv"><button type="button" class="pv-btn" onclick="openPreview(this)">Vista previa</button></div>')

# ---------------------------------------------------------------- datos
# Scripts: n, titulo, fuente, servicio, duracion, hook, cuerpo (beats), cta, caption, aviso
SCRIPTS = [
 dict(n=1, t="Walk In Taller", f="M-13 · 7-ago-2026 (49 likes / 19 comentarios)", v="Marca / Morpheus8", d="45 s",
  h="«Confidence changes how you walk into a room.»",
  b=["Alguien se ve al espejo después de un tratamiento… y se para un poco más erguida.",
     "No se trata de parecer otra persona: es parecer vos, más levantada, más refinada, más equilibrada.",
     "Un plan construido alrededor de vos, nunca talla única."],
  c="Comment CONFIDENCE and tell us — we'll reply with the treatment we'd start with.",
  cap="Confidence has a way of changing how you walk into a room. That's the whole point of what we do — helping you feel like the most confident version of yourself. Come see us in Coral Gables or Aventura."),
 dict(n=2, t="I Just Want the Fat Gone", f="M-02 · 15-oct-2026", v="Venus Bliss Max / QuantumRF", d="45 s",
  h="«“I just want the fat gone.” I hear it every week.»",
  b=["Quitar grasa sin tensar la piel casi nunca se ve como lo imaginaste.",
     "Este equipo hace las dos cosas en una sesión: reducción de grasa y tensión de piel.",
     "El enfoque correcto depende de tu cuerpo y tus metas: por eso empezamos con una consulta."],
  c="Book a body consultation — link in bio.",
  cap="“I just want the fat gone.” That's the most common way patients ask for it — and it's only half the plan. Remove fat without tightening the skin above it and the result rarely looks the way anyone pictured."),
 dict(n=3, t="Don't Throw It Out", f="M-05 · 23-sep-2026 · Rosanna a cámara", v="Skincare / HydraFacial", d="40 s",
  h="«Before you throw this out — watch this.»",
  b=["Purging y un brote real se ven igual, pero necesitan respuestas opuestas.",
     "Purging significa que el producto está funcionando: limpia, luego calma. Un brote significa parar y reevaluar.",
     "¿No sabés cuál es? Traé el producto a tu consulta y te decimos."],
  c="Save this — and bring the product to your next visit.",
  cap="Before you throw out the product, watch this. Purging and a true breakout look similar and need opposite responses. Rosanna breaks down the difference."),
 dict(n=4, t="Tired Eyes? It's Not One Treatment", f="NF-03 No Filter · 9-oct-2026 (24 likes)", v="Relleno de ojeras / PRP", d="45 s",
  h="«Under eyes looking hollow, dark, tired?»",
  b=["La ojera no es un área de un solo tratamiento para todos.",
     "A veces es volumen (relleno). A veces es calidad de piel (PRP). A veces lo mejor es combinar.",
     "Miramos volumen, color y piel, y armamos el plan desde ahí."],
  c="DM us EYES and we'll send you what to ask at your consultation.",
  cap="Under eyes looking hollow, dark, tired? We don't look at the under eye as a one treatment fits all area. Sometimes it's filler, sometimes it's PRP, and sometimes the best result comes from combining them."),
 dict(n=5, t="Your Routine Should Change Too", f="M-09 · 15-sep-2026 · Rosanna a cámara", v="HydraFacial / Morpheus8", d="45 s",
  h="«The season changed. Your routine should too.»",
  b=["El verano deja daño solar. El otoño es cuando lo reparamos y reconstruimos colágeno.",
     "Tres cosas primero: hidratación, daño solar y colágeno. HydraFacial para la superficie, Morpheus8 para lo de abajo.",
     "El orden importa: no apilamos tratamientos, los secuenciamos."],
  c="Book your fall skin consultation — link in bio.",
  cap="The season changed. Your routine should too. Rosanna walks through what your skin actually needs going into fall, from sun damage to collagen."),
 dict(n=6, t="Snatch Your Jawline", f="MO-01 Monaco · 29-oct-2026 (21 interacciones)", v="Morpheus8", d="40 s",
  h="«Tighter skin. Smoother texture. No surgery.»",
  b=["Morpheus8 combina microneedling con radiofrecuencia: reconstruye tu colágeno desde adentro.",
     "Mandíbula, debajo del mentón, cuello: contornea el tercio inferior y suaviza líneas finas.",
     "Somos Top 10% Morpheus8 provider en EE. UU., tres años seguidos."],
  c="Book a Morpheus8 consultation — link in bio.",
  cap="If you want tighter skin, smoother texture, and sculpted definition without surgery, Morpheus8 is the treatment. From a recognized Top 10% provider in the US, 3 years in a row."),
 dict(n=7, t="Your First Visit Shouldn't Feel Intimidating", f="NF-02 No Filter · 8-oct-2026 (18 likes)", v="Consulta inicial", d="40 s",
  h="«Your first medspa visit shouldn't feel intimidating.»",
  b=["Lugar nuevo, gente nueva, alguien mirando tu piel de cerca: lo entendemos.",
     "Acá escuchamos primero, explicamos cada paso y nunca recomendamos un tratamiento que no necesitás.",
     "Si lo venís pensando… esta es tu señal."],
  c="Book your first consultation — link in bio.",
  cap="Your first MedSpa appointment shouldn't feel intimidating. The best results start with the right guidance, a personalized approach, and a team that makes you feel comfortable every step of the way."),
 dict(n=8, t="Three Clocks", f="M-11 · 28-ago-2026", v="HydraFacial / Botox / Morpheus8", d="50 s",
  h="«Your skin, your muscles, and your collagen all work on different clocks.»",
  b=["HydraFacial mantiene la superficie limpia e hidratada: mensual.",
     "Botox suaviza el movimiento: cada 3–4 meses.",
     "Morpheus8 estimula colágeno: una serie, cada 4–6 semanas."],
  c="Save this post — and book your next visit through the link in bio.",
  cap="Your skin, your muscles, and your collagen all work on different clocks. HydraFacial keeps the surface clear and hydrated on a monthly cycle. Botox softens movement for three to four months at a time. Morpheus8 stimulates collagen through a series of treatments spaced four to six weeks apart."),
 dict(n=9, t="Where Does Age Show First?", f="R7 · deck de noviembre (23-nov)", v="Morpheus8 / inyectables", d="45 s",
  h="«Where does age show first? Not where you think.»",
  b=["La mayoría mira las arrugas. Yo miro tres lugares primero.",
     "Uno: debajo de los ojos. Dos: el cuello. Tres: la mandíbula. Ahí es donde se van primero el volumen y el colágeno.",
     "La buena noticia: también son los lugares que mejor responden."],
  c="Comment AGE and tell us where you notice it first.",
  cap="Where does age show first? Rosanna shows you the three places aging appears before anywhere else — and why those are also the places that respond best."),
 dict(n=10, t="What Is PRP?", f="R5 · deck de noviembre (19-nov, Día Internacional del Hombre)", v="PRP", d="45 s",
  h="«What is PRP? Everyone asks. Almost no one explains it.»",
  b=["PRP es tu propia sangre: tomamos una muestra pequeña, concentramos las plaquetas y las ponemos donde tu piel necesita reparación.",
     "Las plaquetas llevan factores de crecimiento: no agregamos nada extraño, le decimos a tu piel que se cure sola.",
     "Funciona para calidad de piel, para cabello y, sí, también para hombres."],
  c="Book a PRP consultation — link in bio.",
  cap="What is PRP? Explained by Rosanna. PRP uses your own platelets to support skin repair, hair, and rejuvenation — for women and for men."),
 dict(n=11, t="Where Can Sculptra Go?", f="R4 · deck de noviembre (14-nov) + Monaco", v="Sculptra", d="45 s",
  h="«Where can Sculptra go? More places than you think.»",
  b=["Rostro: restaurar volumen perdido con el tiempo. No rellenar. Restaurar.",
     "Cuello: para la piel que se ve más fina cada año.",
     "Y sí: glúteos. Un levantamiento no quirúrgico. Sculptra no funciona como el relleno: estimula tu propio colágeno, los resultados se construyen gradualmente."],
  c="Book a Sculptra consultation — link in bio.",
  cap="Where can Sculptra go? Face, neck, and buttocks. Sculptra stimulates your body's own collagen for gradual, natural-looking results."),
 dict(n=12, t="Why QuantumRF?", f="M-20 · 12-jun-2026", v="QuantumRF (15% off siempre activo)", d="45 s",
  h="«Why QuantumRF? Because it does two things at once.»",
  b=["Apunta a los bolsillos de grasa y tensa la piel al mismo tiempo.",
     "Abdomen, brazos, muslos, mandíbula: un resultado más refinado y esculpido.",
     "Mínimo tiempo de recuperación y resultados que pueden durar hasta dos años."],
  c="Book a QuantumRF consultation — link in bio.",
  cap="Why QuantumRF? It targets fat pockets while tightening the skin at the same time, creating a more refined and sculpted result across the abdomen, arms, thighs, and jawline. QuantumRF 15% off."),
 dict(n=13, t="54, Refreshed, Still You", f="M-19 + M-12 · membresía", v="Membresía «More Than Beauty Club»", d="45 s",
  h="«54. Refreshed. And still completely natural.»",
  b=["La diferencia no es un tratamiento. Es la constancia.",
     "La membresía está diseñada para mantener resultados sutiles y personalizados en el tiempo: tratamientos mensuales y precios de miembro.",
     "Seguís viéndote como vos: solo más levantada, más refinada, más equilibrada."],
  c="Call us to learn more about becoming a member — (305) 356-7402.",
  cap="54, refreshed, and still completely natural. The difference is consistency. Our membership is designed to maintain subtle, personalized results over time."),
]

SCRIPTS += [
 dict(n=14, t="The Contour Edit", f="R2 · deck de noviembre (7-nov) + Q4", v="Inyectables — $200 off gastando $1,000+ (hasta 26-nov)", d="50 s",
  h="«“I don't want to look overdone.” I hear it every day.»",
  b=["Dieciséis años en antienvejecimiento me enseñaron una cosa: el mejor inyectable es el que nadie nota.",
     "Mapeamos cada jeringa a tu anatomía. Sin volumen exagerado, sin sobrecarga: solo equilibrio.",
     "Este mes, The Contour Edit: $200 off gastando $1,000 o más en inyectables, hasta el 26 de noviembre."],
  c="Book before November 26 — link in bio.",
  cap="“I don't want to look overdone.” After sixteen years in anti-aging, Rosanna knows: the best injectable is the one nobody notices. The Contour Edit — $200 off when you spend $1,000+ on injectables, until November 26."),
 dict(n=15, t="The Glow Duo", f="Estática deck 4-nov + Q4", v="HydraFacial + Aerolase — 20% off el primer dúo (hasta 26-nov)", d="40 s",
  h="«Two treatments. One glow. Twenty percent off.»",
  b=["HydraFacial limpia, extrae y rehidrata. Aerolase apunta al enrojecimiento y la textura.",
     "Juntos hacen lo que ninguno hace solo: un glow de primer plano. Por eso lo llamamos The Close-Up.",
     "20% off tu primer Glow Duo, hasta el 26 de noviembre."],
  c="Book your first Glow Duo — link in bio.",
  cap="The Glow Duo — 20% off your first HydraFacial + Aerolase. HydraFacial gently extracts, cleanses and re-hydrates; Aerolase targets redness and texture. Together: the close-up glow. Until November 26."),
 dict(n=16, t="15% Off Morpheus8", f="M-06 + M-18", v="Morpheus8", d="40 s",
  h="«Lift. Tighten. Refine. Three words. One treatment.»",
  b=["Morpheus8: microneedling más radiofrecuencia, reconstruyendo colágeno desde adentro.",
     "El nuevo Morpheus8 Burst nos da más flexibilidad: comodidad, calidad de piel, grosor, pigmentación.",
     "Somos Top 10% provider reconocido en EE. UU., tres años seguidos."],
  c="Ask about Morpheus8 series pricing — link in bio.",
  cap="Lift. Tighten. Refine. Morpheus8 from a recognized Top 10% provider in the US, 3 years in a row. Morpheus8 Burst offers greater flexibility during treatment.",
  w="El 15% del caption M-06 puede estar vencido: el Q4 trae $200 off la serie como siempre activa. Confirmar con Rosanna cuál rige antes de publicar."),
 dict(n=17, t="Results Matter", f="M-17 · 29-jun-2026 (25 likes)", v="Testimonio / marca", d="40 s",
  h="«“I not only see a difference — I want to come back.”»",
  b=["Los resultados importan. También la experiencia detrás de ellos.",
     "Un plan personalizado, cuidado continuo, un equipo que conoce tu piel, no solo tu historia clínica.",
     "Escuchar que nuestras pacientes quieren volver… por eso hacemos lo que hacemos."],
  c="Read more patient stories — link in bio.",
  cap="Results matter. So does the experience behind them. Hearing that our patients not only see a difference, but want to come back, is why we do what we do.",
  w="Requiere paciente real con consentimiento grabado; sin eso, no se graba."),
 dict(n=18, t="I Do It Too", f="MO-04 Monaco · 31-oct-2026", v="Inyectables / equipo", d="35 s",
  h="«I don't just recommend it. I do it too.»",
  b=["Precisión, técnica, atención al detalle: eso es cada procedimiento acá.",
     "Y cuando me siento yo en la silla, siento lo que sienten nuestras pacientes.",
     "Practicar lo que predicamos. Ese es el estándar."],
  c="Meet the team — link in bio.",
  cap="A little behind-the-scenes: practicing what we preach. Precision, technique, and attention to detail are at the heart of every procedure."),
 dict(n=19, t="Real Transformations (serie, parte 1)", f="MO-07/08 Monaco · 1-nov-2026", v="Marca / varios", d="45 s",
  h="«Real transformations are about confidence — not changing who you are.»",
  b=["Nos especializamos en mejoras de aspecto natural: refrescar, esculpir, levantar, rejuvenecer.",
     "Morpheus8, balance facial, contorno de mandíbula, rellenos, Sculptra, Tox.",
     "Parte uno de una serie. Siguiente: una paciente real, un plan real."],
  c="Follow for part two.",
  cap="Real transformations are about confidence, not changing who you are. At Med Aesthetics Miami, we specialize in natural-looking aesthetic enhancements designed to refresh, sculpt, lift, and rejuvenate your appearance.",
  w="La parte 2 necesita paciente real con consentimiento y antes/después verificado."),
 dict(n=20, t="Because I Wanted To", f="R6 · deck de noviembre (21-nov)", v="Retoques / Botox / HydraFacial", d="35 s",
  h="«“What's the occasion?” Nothing. I just wanted to.»",
  b=["No necesitás una boda. No necesitás un cumpleaños.",
     "Un retoque no es vanidad. Es mantenimiento, como el gimnasio o la peluquería.",
     "Si venís esperando una razón… esta es."],
  c="Book your refresh — link in bio.",
  cap="You don't need a special occasion for a refresh. Because I wanted to. Book your appointment through the link in bio."),
 dict(n=21, t="A Few Things You'll Find Here", f="R3 · deck de noviembre (12-nov)", v="Tour / Morpheus8 / inyectables", d="45 s",
  h="«A few things you'll find at Med Aesthetics Miami.»",
  b=["Primero: un equipo que escucha antes de recomendar.",
     "Segundo: Morpheus8, nuestro tratamiento más preguntado.",
     "Tercero: inyectables mapeados a tu rostro. Nunca talla única. Y el cuidado está en los detalles."],
  c="Book a visit — Coral Gables or Aventura, link in bio.",
  cap="A few things you'll find at Med Aesthetics Miami. A team that listens, Morpheus8, and injectables mapped to your face. The care is in the details."),
 dict(n=22, t="The Plate", f="R1 · deck de noviembre (2-nov)", v="Evolysse / Radiesse", d="30 s",
  h="«I have a lot on my plate right now.»",
  b=["La bandeja en cuestión: Evolysse para volumen suave, Radiesse para estructura y colágeno con el tiempo.",
     "¿Cuál agarrás primero?"],
  c="Comment EVOLYSSE or RADIESSE — we'll tell you which fits you.",
  cap="I have a lot on my plate right now. The plate in question. Which one are you picking up first?"),
 dict(n=23, t="QuantumRF Legs & Knees", f="R8 · deck de noviembre (28-nov)", v="QuantumRF corporal", d="45 s",
  h="«Legs and knees. The area nobody talks about.»",
  b=["QuantumRF tensa la piel y apunta a la grasa en la misma sesión.",
     "Paciente real, resultados reales. Individual results vary.",
     "Gold Friday hasta el 30 de noviembre. La consulta la podés reservar hoy."],
  c="Book a QuantumRF consultation — link in bio.",
  cap="Before and after: QuantumRF on legs and knees. Gold Friday continues until November 30. Individual results vary.",
  w="BLOQUEADO: precios Gold Friday a confirmar por Rosanna y orden del antes/después. No grabar sin eso."),
 dict(n=24, t="Last Day of Gold Friday", f="R9 · deck de noviembre (30-nov)", v="Gold Friday", d="30 s",
  h="«Today is the last day. That's it.»",
  b=["Gold Friday termina esta noche. Láser de cuerpo completo, Morpheus8, QuantumRF: los paquetes terminan con él.",
     "Si lo venís pensando… este es el momento.",
     "Llamanos o tocá el link en bio. Antes de medianoche."],
  c="Call (305) 356-7402 — today.",
  cap="Last day of Gold Friday. Packages end tonight. Call (305) 356-7402 or tap the link in bio. #goldfriday #cybermonday",
  w="BLOQUEADO: precios a confirmar por Rosanna. Sin precios confirmados, este reel NO se puede publicar."),
 dict(n=25, t="Glass Skin", f="SK-01 SKINNEY + LU-02 LUX (9 comentarios)", v="HydraFacial", d="35 s",
  h="«“Oh my gosh, my skin looks like glass!”»",
  b=["Ella ya se cuida la piel. Y aun así dijo eso después de un HydraFacial.",
     "Extrae suavemente, limpia y rehidrata. Eso es todo. Sin drama, sin recuperación.",
     "Tu mejor glow, en una sesión."],
  c="Book your HydraFacial — link in bio.",
  cap="Get your best glow with HydraFacial. It gently extracts, cleanses and re-hydrates the skin to leave you with perfect glass skin.",
  w="La cita «glass» es de una clienta de LUX, no de Med: debe ser una clienta real de Med o se quita la cita."),
 dict(n=26, t="Retire the Razor", f="Q4 noviembre + SK-04 + R5", v="Láser para hombres — sesión bonus (hasta 26-nov)", d="40 s",
  h="«Men need treatments too. Yes — including laser.»",
  b=["Afeitarse todos los días. Irritación. Vellos encarnados. ¿Te suena?",
     "El láser termina ese ciclo. Y este mes, una sesión bonus viene con el paquete.",
     "Misma clínica, mismo cuidado, misma discreción."],
  c="Book a men's laser consultation — link in bio.",
  cap="Men need treatments too. Retire the Razor — a bonus session with your men's laser package, until November 26. Laser Hair Removal 30% off, always on."),
]

# Calendario 10–30 nov: (dia, formato, tema, fuente, redes, nota)
CALENDAR = [
 ("mar 10 nov", "Carrusel", "«QuantumRF: Men Included» — antes/después abdomen masculino", "Deck · G-02", "IG + FB", "Confirmar el orden correcto del antes/después + foto real con consentimiento"),
 ("mié 11 nov", "Reel", "Rosanna a cámara: purging vs. breakout («Before you throw out the product…»)", "Banco · guion #3", "IG + FB", "Guion y video con Rosanna"),
 ("jue 12 nov", "Reel", "«A FEW THINGS YOU'LL FIND AT MED AESTHETICS MIAMI» — Rosanna muestra tratamientos", "Deck R3 · guion #21", "IG + FB + TikTok + YouTube", "Video con Rosanna"),
 ("vie 13 nov", "Estática", "Tarjeta oferta siempre activa: Botox $10/unidad", "Q4 · G-05", "IG + FB", "Aprobar diseño de la tarjeta"),
 ("sáb 14 nov", "Reel", "Sculptra — «WHERE CAN SCULPTRA GO?» (rostro, cuello, glúteos)", "Deck R4 · guion #11", "IG + FB + TikTok + YouTube", "Video y contenido de zonas"),
 ("dom 15 nov", "Carrusel", "Checklist «Preguntas para tu consulta» v2, con pregunta final para comentarios", "Banco · G-10", "IG + FB", "Contenido del checklist + CTA final"),
 ("lun 16 nov", "Reel", "Línea de tiempo de tratamientos: HydraFacial mensual, Botox 3–4 meses, Morpheus8 cada 4–6 semanas", "Banco · guion #8", "IG + FB", "Video y tiempos indicados"),
 ("mar 17 nov", "Carrusel", "QuantumRF — antes/después de brazos; «individual results vary»", "Deck · G-03", "IG + FB", "Foto real con consentimiento"),
 ("mié 18 nov", "Reel", "Ángulo «confianza» (el de mejor rendimiento de Med: M-13)", "Banco · guion #1", "IG + FB", "Definir si es material nuevo de la jornada o remontaje"),
 ("jue 19 nov", "Reel", "«What is PRP? Explained by Rosanna» — Día Internacional del Hombre", "Deck R5 · guion #10", "IG + FB + TikTok + YouTube", "Video con Rosanna"),
 ("vie 20 nov", "Estática", "Tarjeta oferta siempre activa: Morpheus8 $200 off la serie — solo Aventura", "Q4 · G-07", "IG + FB", "Diseño + aclarar «Aventura Location Only»"),
 ("sáb 21 nov", "Reel", "No hace falta ocasión especial para un retoque («Because I wanted to»)", "Deck R6 · guion #20", "IG + FB + TikTok + YouTube", "Video"),
 ("dom 22 nov", "Carrusel", "«Retire the Razor» zona por zona (espalda, pecho, cuello, línea de barba)", "Q4 · G-12", "IG + FB", "Rosanna confirma sesiones por zona"),
 ("lun 23 nov", "Reel", "«Where does age show first?» — Rosanna muestra dónde se nota primero el envejecimiento", "Deck R7 · guion #9", "IG + FB + TikTok + YouTube", "Video con Rosanna"),
 ("mar 24 nov", "Reel", "«Why QuantumRF?» — grasa + tensión de piel en una sesión", "Banco · guion #12", "IG + FB", "Video y contenido"),
 ("mié 25 nov", "Estática", "Tarjeta oferta: Glow Duo, 20% off primer HydraFacial + Aerolase — últimos días (vence 26-nov)", "Q4 · G-01", "IG + FB", "Diseño de la tarjeta"),
 ("jue 26 nov", "Estática", "Recordatorio último día: ofertas de noviembre vencen hoy (Glow Duo, The Contour Edit, Retire the Razor)", "Q4", "IG + FB", "Texto y diseño. Además: apagar anuncios de noviembre en Meta Ads"),
 ("vie 27 nov", "Carrusel", "«Gold Friday Package Event»", "Deck · G-04", "IG + FB", "PRECIOS A CONFIRMAR POR ROSANNA"),
 ("sáb 28 nov", "Reel", "Antes/después QuantumRF corporal (piernas/rodillas); Gold Friday hasta 30-nov", "Deck R8 · guion #23", "IG + FB + TikTok + YouTube", "«NOT CONFIRMED»: precios Gold Friday + foto real con consentimiento"),
 ("dom 29 nov", "Sin pieza definida", "—", "—", "—", "Falta definir: recordatorio Gold Friday, reel de humor o no publicar"),
 ("lun 30 nov", "Reel", "Último día de Gold Friday; incluye #cybermonday", "Deck R9 · guion #24", "IG + FB + TikTok + YouTube", "Precios Gold Friday a confirmar por Rosanna"),
]

# Piezas gráficas G-01..G-15: (id, pieza, tipo, fecha, falta)
GRAPHICS = [
 ("G-01", "Estática-resumen ofertas noviembre (Glow Duo + The Contour Edit + Retire the Razor)", "Tipo 2 · Tarjeta de oferta", "Deck 4-nov — a decidir: recuperar o seguir desde el 10-nov", "Decisión de Daniel/Rosanna: ¿se recupera el 4-nov o se descarta?"),
 ("G-02", "Carrusel «QuantumRF: Men Included» (antes/después abdomen masculino)", "Tipo 1 · Antes / después", "Mar 10-nov", "Confirmar el orden del antes/después + foto real con consentimiento"),
 ("G-03", "Carrusel QuantumRF antes/después de brazos", "Tipo 1 · Antes / después", "Mar 17-nov", "Foto real con consentimiento + «individual results vary»"),
 ("G-04", "Carrusel «Gold Friday Package Event»", "Tipo 2 · Tarjeta de oferta", "Vie 27-nov", "Precios A CONFIRMAR POR ROSANNA"),
 ("G-05", "Tarjeta oferta siempre activa — Botox $10/unidad", "Tipo 2 · Tarjeta de oferta", "Rotación", "Aprobación del diseño"),
 ("G-06", "Tarjeta oferta siempre activa — Láser 30% off", "Tipo 2 · Tarjeta de oferta", "Rotación", "Aprobación del diseño"),
 ("G-07", "Tarjeta oferta siempre activa — Morpheus8 $200 off la serie", "Tipo 2 · Tarjeta de oferta", "Rotación", "Aclarar «Aventura Location Only»"),
 ("G-08", "Tarjeta oferta siempre activa — QuantumRF 15% off", "Tipo 2 · Tarjeta de oferta", "Rotación", "Aprobación del diseño"),
 ("G-09", "Tarjeta oferta siempre activa — Rejuvenecimiento vaginal 30% off", "Tipo 2 · Tarjeta de oferta", "Rotación", "Aprobación de Rosanna (tema sensible: tono y foto)"),
 ("G-10", "Carrusel checklist «Preguntas para tu consulta» v2", "Tipo 3 · Checklist «guardable»", "Dom 15-nov", "Revisión del contenido + CTA final"),
 ("G-11", "Carrusel «Tu preparación para fotos de fiestas» (Glow Duo)", "Tipo 3 · Checklist «guardable»", "Semana 16–22 nov", "Rosanna confirma los tiempos antes del evento"),
 ("G-12", "Carrusel «Retire the Razor» zona por zona", "Tipo 5 · Educativo de tratamiento", "Dom 22-nov", "Rosanna confirma sesiones por zona"),
 ("G-13", "Foto testimonial con cita (formato VIO)", "Tipo 4 · Testimonial", "Sin fecha — a definir", "Falta testimonio real + consentimiento escrito"),
 ("G-14", "Estática credencial Top 10% Morpheus8 + 3 sedes", "Tipo 7 · Credencial", "Rotación", "Arte oficial del sello InMode (si existe)"),
 ("G-15", "Estática «para dos / regalo» (formato LUX)", "Tipo 6 · Para dos / regalo", "Sin fecha — NO producir en noviembre", "Confirmar si Med ofrece algo «para dos» o gift cards en noviembre"),
]

# Ofertas: (grupo, nombre, detalle, vigencia, confirmar?)
OFFERS = [
 ("Siempre activas", "Láser depilación", "30% off", "Siempre", False),
 ("Siempre activas", "Rejuvenecimiento vaginal", "30% off", "Siempre", False),
 ("Siempre activas", "Botox", "$10 / unidad", "Siempre", False),
 ("Siempre activas", "Morpheus8 (serie)", "$200 off la serie — solo sede Aventura", "Siempre", False),
 ("Siempre activas", "QuantumRF", "15% off", "Siempre", False),
 ("Noviembre · 1–26 nov", "Glow Duo — HydraFacial + Aerolase", "20% off el primer Glow Duo", "Hasta 26-nov", False),
 ("Noviembre · 1–26 nov", "The Contour Edit — Inyectables", "$200 off gastando $1,000+ en inyectables", "Hasta 26-nov", False),
 ("Noviembre · 1–26 nov", "Retire the Razor — Láser para hombres", "Sesión bonus con paquete de láser para hombres", "Hasta 26-nov", False),
 ("Gold Friday · 27–30 nov", "Láser cuerpo completo", "$999 + sesión bonus", "27–30 nov", True),
 ("Gold Friday · 27–30 nov", "Morpheus8 (paquete de 3)", "$4,500", "27–30 nov", True),
 ("Gold Friday · 27–30 nov", "QuantumRF", "$2,500 cara / $3,000 cuerpo", "27–30 nov", True),
]

PENDIENTES = [
 "Orden del antes/después del carrusel del 10-nov (lo pidió Rosanna).",
 "Precios del Gold Friday 27–30 nov (láser $999, Morpheus8 3×$4,500, QuantumRF $2,500/$3,000).",
 "Posts del 2, 4 y 7-nov: recuperar o seguir desde el 10-nov.",
 "Fecha de la jornada de filmación mensual (los reels del 11, 12, 16, 18, 19, 21, 23 y 24-nov la necesitan).",
 "Fotos reales con consentimiento para los antes/después del 10, 17 y 28-nov.",
 "Accesos para publicar: TikTok y Pinterest sin aceptar; Meta Business/Instagram y YouTube sin constancia; falta Meta Ads Manager.",
 "Morpheus8: el caption M-06 ofrece 15% off, el Q4 trae $200 off la serie — confirmar cuál rige.",
]

# ---------------------------------------------------------------- render
CSS = """
:root{--gold:#e3b533;--gray:#606163;--ink:#2b2b2b;--light:#f2f9ff;--cream:#ecf0e4;--brown:#4b3618;--white:#fff}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;color:var(--ink);background:#faf8f2;line-height:1.55;overflow-x:hidden}
.brand{font-family:Georgia,'Times New Roman',serif}
.wrap{max-width:1060px;margin:0 auto;padding:0 20px}
/* ---------- login ---------- */
#gate{position:fixed;inset:0;z-index:100;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#4b3618 0%,#606163 55%,#e3b533 130%);padding:20px}
#gate.hidden{display:none}
.gate-card{background:#fff;border-radius:14px;max-width:420px;width:100%;padding:34px 30px;box-shadow:0 20px 60px rgba(0,0,0,.35);text-align:center}
.gate-card h1{font-family:Georgia,serif;color:var(--brown);font-size:26px;font-weight:400;letter-spacing:1px}
.gate-card .sub{color:var(--gray);font-size:14px;margin:6px 0 22px}
.gate-card label{display:block;text-align:left;font-size:13px;color:var(--gray);margin:12px 0 4px}
.gate-card input{width:100%;padding:11px 12px;border:1px solid #d8d2c4;border-radius:8px;font-size:15px}
.gate-card input:focus{outline:2px solid var(--gold)}
.btn{display:inline-block;background:var(--gold);color:#fff;border:0;border-radius:8px;padding:12px 22px;font-size:15px;font-weight:700;cursor:pointer;text-decoration:none}
.btn:hover{background:#cfa12a}
.btn-ghost{background:#fff;color:var(--brown);border:1.5px solid var(--gold)}
#gate-err{color:#b3261e;font-size:13px;min-height:18px;margin-top:10px}
.gate-note{font-size:12px;color:#999;margin-top:16px}
/* ---------- hero ---------- */
.hero{position:relative;color:#fff;overflow:hidden;background:linear-gradient(120deg,#4b3618 0%,#606163 60%,#8a7a3a 100%)}
.hero-media{position:absolute;inset:0}
.hero-media img{width:100%;height:100%;object-fit:cover;display:block}
.hero-media::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,rgba(75,54,24,.88),rgba(96,97,99,.72) 60%,rgba(227,181,51,.45))}
.hero-inner{position:relative;padding:64px 0 54px}
.hero-eyebrow{letter-spacing:3px;font-size:12px;text-transform:uppercase;color:var(--gold)}
.hero h1{font-family:Georgia,serif;font-weight:400;font-size:44px;line-height:1.15;margin:12px 0 10px;max-width:640px}
.hero p.lede{font-size:18px;max-width:620px;color:#f4efe2}
.hero-cta{margin-top:22px;display:flex;gap:12px;flex-wrap:wrap}
.hero-cta .btn-ghost{color:#fff;border-color:#fff;background:transparent}
.seals{display:flex;gap:10px;flex-wrap:wrap;margin-top:28px}
.seal{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:7px 14px;font-size:13px}
/* ---------- sections ---------- */
section{padding:44px 0}
section h2{font-family:Georgia,serif;font-weight:400;font-size:30px;color:var(--brown);margin-bottom:6px}
section .intro{color:var(--gray);margin-bottom:22px;max-width:760px}
.why{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:26px}
.why div{background:#fff;border:1px solid #e8e2d2;border-radius:12px;padding:18px}
.why b{color:var(--gold);font-size:22px;font-family:Georgia,serif;display:block}
.why h3{font-size:16px;margin:4px 0}
.why p{font-size:14px;color:var(--gray)}
.badge{display:inline-block;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:999px;padding:3px 10px;background:var(--cream);color:var(--brown)}
.badge.warn{background:#fdeecb;color:#8a6d00}
.badge.gold{background:var(--gold);color:#fff}
.badge.gray{background:#e9e9e9;color:var(--gray)}
/* calendar */
.cal{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.day{background:#fff;border:1px solid #e8e2d2;border-radius:12px;padding:18px}
.day .d{font-family:Georgia,serif;font-size:19px;color:var(--brown)}
.day .fmt{font-size:13px;color:var(--gray);margin:2px 0 8px}
.day p{font-size:14px}
.day .note{font-size:13px;color:#8a6d00;background:#fdf6e0;border-radius:8px;padding:8px 10px;margin-top:10px}
.day .nets{font-size:12px;color:var(--gray);margin-top:8px}
.day.empty{background:var(--cream);border-style:dashed}
/* scripts */
details{background:#fff;border:1px solid #e8e2d2;border-radius:12px;margin-bottom:12px;padding:16px 18px}
details summary{cursor:pointer;font-family:Georgia,serif;font-size:19px;color:var(--brown);list-style:none}
details summary::-webkit-details-marker{display:none}
details summary .n{color:var(--gold);font-weight:700;margin-right:8px}
details .meta{font-size:13px;color:var(--gray);margin:6px 0 10px}
details .lbl{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--gray);margin-top:12px}
details .hook{font-family:Georgia,serif;font-size:18px;color:var(--brown)}
details ul{margin:6px 0 6px 20px;font-size:14px}
details .cap{font-size:13px;color:var(--gray);background:var(--light);border-radius:8px;padding:10px 12px;margin-top:8px}
.warnbox{font-size:13px;color:#8a6d00;background:#fdf6e0;border-radius:8px;padding:8px 10px;margin-top:10px}
/* graphics + offers */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.card{background:#fff;border:1px solid #e8e2d2;border-radius:12px;padding:18px}
.card h3{font-family:Georgia,serif;font-weight:400;font-size:18px;color:var(--brown);margin:6px 0}
.card p{font-size:14px}
.card .price{font-family:Georgia,serif;font-size:22px;color:var(--brown);margin:6px 0}
.card .vig{font-size:12px;color:var(--gray)}
.card .need{font-size:13px;color:#8a6d00;background:#fdf6e0;border-radius:8px;padding:8px 10px;margin-top:10px}
.approve{margin-top:12px}
.approve a{display:inline-block;background:#25D366;color:#fff;font-weight:700;font-size:13px;border-radius:999px;padding:8px 16px;text-decoration:none}
.approve a:hover{background:#1da851}
/* feedback por WhatsApp */
.fb{margin-top:10px}
.fb textarea{width:100%;padding:10px 12px;border:1px solid #d8d2c4;border-radius:8px;font-size:14px;font-family:inherit;resize:vertical;min-height:56px}
.fb textarea:focus{outline:2px solid var(--gold)}
.fb-btn{display:inline-block;margin-top:8px;background:#fff;color:var(--brown);border:1.5px solid var(--gold);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit}
.fb-btn:hover{background:#fdf6e0}
.band{position:relative;overflow:hidden;border-radius:12px;min-height:120px;display:flex;align-items:center;justify-content:center;background:linear-gradient(120deg,#4b3618,#606163 60%,#e3b533);margin:8px 0 22px}
.band img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.band span{position:relative;color:#fff;font-family:Georgia,serif;font-size:22px;text-align:center;padding:20px}
/* pendientes */
.pend{background:#fff;border:1px solid #e8e2d2;border-radius:12px;padding:22px}
.pend li{margin:8px 0 8px 20px;font-size:14px}
footer{background:var(--brown);color:#e8dfc8;padding:30px 0;text-align:center;font-size:13px}
footer a{color:var(--gold)}
.topbar{background:var(--brown);color:#fff;font-size:13px;padding:10px 0}
.topbar .wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
.topbar a{color:var(--gold);text-decoration:none}
/* redes: cápsulas con el color de cada marca (definido una vez acá) */
.nets{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.net{display:inline-flex;align-items:center;border-radius:999px;padding:3px 11px;font-size:11px;font-weight:700;letter-spacing:.4px;color:#fff;white-space:nowrap}
.net-ig{background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)}
.net-fb{background:#1877F2}
.net-tt{background:#010101;border:1.5px solid #25F4EE;box-shadow:inset 0 -2px 0 #FE2C55}
.net-yt{background:#FF0000}
/* botón vista previa */
.pv{margin-top:10px}
.pv-btn{display:inline-block;background:#fff;color:var(--brown);border:1.5px solid var(--gray);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit}
.pv-btn:hover{border-color:var(--gold);background:#fdf6e0}
/* modal de vista previa */
.modal-overlay{position:fixed;inset:0;z-index:200;display:none;align-items:center;justify-content:center;background:rgba(43,43,43,.65);padding:16px}
.modal-overlay.open{display:flex}
.modal{position:relative;background:#fff;border-radius:14px;max-width:640px;width:100%;max-height:88vh;overflow-y:auto;padding:26px 24px 22px;box-shadow:0 24px 70px rgba(0,0,0,.4)}
.modal-close{position:absolute;top:10px;right:12px;width:44px;height:44px;border:0;border-radius:50%;background:var(--cream);color:var(--brown);font-size:28px;line-height:1;cursor:pointer;z-index:1}
.modal-close:hover{background:var(--gold);color:#fff}
.modal .day,.modal .card{border:0;padding:0}
.modal details{border:0;padding:0;margin:0}
.modal .approve,.modal .fb{margin-top:14px}
@media(max-width:640px){
  .hero h1{font-size:32px}
  section h2{font-size:25px}
  .hero-inner{padding:44px 20px 38px}
  .modal-overlay{padding:8px}
  .modal{width:94vw;max-height:90vh;padding:22px 16px 18px;border-radius:16px}
  .modal-close{width:48px;height:48px;font-size:30px;top:8px;right:8px}
  .approve a,.fb-btn,.pv-btn{display:block;text-align:center;margin-top:8px}
  .fb textarea{font-size:16px}
}
"""

def cal_rows():
    out = []
    for dia, fmt, tema, fuente, redes, nota in CALENDAR:
        empty = " empty" if dia.startswith("dom 29") else ""
        warn = "A CONFIRMAR POR ROSANNA" in nota or "PRECIOS" in nota
        piece = "la pieza del " + dia + ": " + tema
        msg = "Hola Daniel, apruebo " + piece
        out.append(
            '<article class="day%s"><span class="badge%s">%s</span> '
            '<div class="d">%s</div><div class="fmt">%s · %s</div><p>%s</p>'
            '%s%s'
            '<div class="approve"><a href="%s" target="_blank" rel="noopener">Aprobar por WhatsApp</a></div>%s%s</article>' % (
                empty, " warn" if warn else "", esc(fmt), esc(dia), esc(fmt), esc(fuente), esc(tema),
                nets_pills(redes),
                ('<div class="note">%s</div>' % esc(nota)) if nota and nota != "—" else "",
                wa(msg), pv_btn(), fb(piece)))
    return "\n".join(out)

def script_blocks():
    out = []
    for s in SCRIPTS:
        beats = "".join("<li>%s</li>" % esc(b) for b in s["b"])
        warn = ('<div class="warnbox">%s</div>' % esc(s["w"])) if s.get("w") else ""
        piece = "el guion #%d: %s" % (s["n"], s["t"])
        msg = "Hola Daniel, apruebo " + piece
        out.append(
            '<details><summary><span class="n">#%d</span>%s</summary>'
            '<div class="meta">%s · %s · %s · %s</div>'
            '<div class="lbl">Hook (0–3 s)</div><div class="hook">%s</div>'
            '<div class="lbl">Cuerpo</div><ul>%s</ul>'
            '<div class="lbl">CTA único</div><p>%s</p>'
            '<div class="cap"><b>Caption:</b> %s</div>%s'
            '<div class="approve"><a href="%s" target="_blank" rel="noopener">Aprobar guion por WhatsApp</a></div>%s%s</details>' % (
                s["n"], esc(s["t"]), esc(s["f"]), esc(s["v"]), esc(s["d"]), "Inglés",
                esc(s["h"]), beats, esc(s["c"]), esc(s["cap"]), warn, wa(msg), pv_btn(), fb(piece)))
    return "\n".join(out)

def graphic_cards():
    out = []
    for gid, pieza, tipo, fecha, falta in GRAPHICS:
        und = "SIN DEFINIR" in fecha or "NO producir" in fecha
        piece = "la pieza %s: %s" % (gid, pieza)
        msg = "Hola Daniel, apruebo " + piece
        out.append(
            '<article class="card"><span class="badge%s">%s</span>'
            '<h3>%s</h3><p>%s</p><p class="vig">%s</p>'
            '<div class="need">Falta: %s</div>'
            '<div class="approve"><a href="%s" target="_blank" rel="noopener">Aprobar por WhatsApp</a></div>%s%s</article>' % (
                " warn" if und else "", esc(gid), esc(pieza), esc(tipo), esc(fecha), esc(falta), wa(msg), pv_btn(), fb(piece)))
    return "\n".join(out)

def offer_cards():
    out = []
    for grupo, nombre, detalle, vig, confirmar in OFFERS:
        piece = "la oferta: %s — %s" % (nombre, detalle)
        msg = "Hola Daniel, apruebo " + piece
        out.append(
            '<article class="card"><span class="badge%s">%s</span>'
            '<h3>%s</h3><div class="price">%s</div><p class="vig">Vigencia: %s</p>%s'
            '<div class="approve"><a href="%s" target="_blank" rel="noopener">Aprobar por WhatsApp</a></div>%s%s</article>' % (
                " warn" if confirmar else " gold", esc(grupo), esc(nombre), esc(detalle), esc(vig),
                '<div class="need">Precio A CONFIRMAR POR ROSANNA — no usar sin su confirmación.</div>' if confirmar else "",
                wa(msg), pv_btn(), fb(piece)))
    return "\n".join(out)

TPL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Med Aesthetics Miami — Portal del cliente · MuViProject</title>
<style>__CSS__</style>
</head>
<body>
<!-- ============================================================
     CONFIGURACIÓN DEL ACCESO (editar acá para cambiar la clave)
     La contraseña de este portal es una CORTINA VISUAL, no
     seguridad real: al ser un sitio estático (GitHub Pages),
     cualquiera que lea el código puede verla. Para acceso
     protegido de verdad, usar Cloudflare Access.
     ============================================================ -->
<script>
var PORTAL_PASSWORD = "MedAesthetics2026";
var PORTAL_EMAIL_DOMAIN = "@medaestheticsmiami.com";
</script>

<div id="gate">
  <div class="gate-card">
    <div class="brand" style="color:#e3b533;font-size:15px;letter-spacing:2px">MED AESTHETICS MIAMI</div>
    <h1>Portal del cliente</h1>
    <div class="sub">MuViProject · Contenido en revisión — nada se publica sin la aprobación de Rosanna</div>
    <form id="gate-form">
      <label for="gate-email">Email</label>
      <input id="gate-email" type="email" placeholder="info@medaestheticsmiami.com" autocomplete="username" required>
      <label for="gate-pass">Contraseña</label>
      <input id="gate-pass" type="password" placeholder="Contraseña" autocomplete="current-password" required>
      <div id="gate-err"></div>
      <div style="margin-top:16px"><button class="btn" type="submit" style="width:100%">Entrar al portal</button></div>
    </form>
    <div class="gate-note">Acceso para Rosanna y el equipo de Med Aesthetics Miami.<br>¿Problemas para entrar? Escribinos por WhatsApp al (845) 699-6606.</div>
  </div>
</div>
<script>
(function(){
  var gate = document.getElementById('gate');
  try { if (sessionStorage.getItem('mam_auth') === '1') { gate.classList.add('hidden'); } } catch(e){}
  document.getElementById('gate-form').addEventListener('submit', function(ev){
    ev.preventDefault();
    var email = document.getElementById('gate-email').value.trim().toLowerCase();
    var pass = document.getElementById('gate-pass').value;
    var err = document.getElementById('gate-err');
    if (email.slice(-PORTAL_EMAIL_DOMAIN.length) !== PORTAL_EMAIL_DOMAIN) {
      err.textContent = 'Usá tu email de Med Aesthetics Miami (@medaestheticsmiami.com).';
      return;
    }
    if (pass !== PORTAL_PASSWORD) {
      err.textContent = 'Contraseña incorrecta. Revisala e intentá de nuevo.';
      return;
    }
    try { sessionStorage.setItem('mam_auth', '1'); } catch(e){}
    gate.classList.add('hidden');
    window.scrollTo(0, 0);
  });
})();
</script>

<div class="topbar"><div class="wrap"><span>Med Aesthetics Miami · Portal del cliente — MuViProject</span><span><a href="#" onclick="try{sessionStorage.removeItem('mam_auth')}catch(e){};location.reload();return false;">Salir</a></span></div></div>

<header class="hero">
  <div class="hero-media"><img src="assets/hero.png" alt="" onerror="this.remove()"></div>
  <div class="wrap hero-inner">
    <div class="hero-eyebrow">Med Aesthetics Miami · Coral Gables · Aventura · Lauderdale-By-The-Sea</div>
    <h1 class="brand">Look and Feel Your Best.<br>Believe in you! Embrace your beauty.</h1>
    <p class="lede">Todo el contenido de noviembre en un solo lugar: calendario de publicaciones, guiones de reels y piezas gráficas. Cada pieza está en borrador y se publica solo con la aprobación de Rosanna.</p>
    <div class="hero-cta">
      <a class="btn" href="#calendario">Ver calendario de noviembre</a>
      <a class="btn btn-ghost" href="tel:+13053567402">Call (305) 356-7402</a>
    </div>
    <div class="seals">
      <span class="seal">Top 10% Morpheus8 Provider (InMode)</span>
      <span class="seal">3 sedes en el sur de Florida</span>
      <span class="seal">Planes personalizados para mujeres y hombres</span>
      <span class="seal">Planes de pago para calificados</span>
    </div>
  </div>
</header>

<section><div class="wrap">
  <h2>Por qué Med Aesthetics Miami</h2>
  <div class="why">
    <div><b>01</b><h3>Top-rated experts</h3><p>Equipo médico y estético con la credencial Top 10% Morpheus8 tres años seguidos.</p></div>
    <div><b>02</b><h3>Luxury, personalized experience</h3><p>Planes a medida, nunca un molde único: cada tratamiento se arma alrededor de cada paciente.</p></div>
    <div><b>03</b><h3>Cutting-edge treatments</h3><p>Morpheus8, QuantumRF, Sculptra, PRP, HydraFacial y láser de última generación.</p></div>
  </div>
</div></section>

<section id="calendario" style="background:#fff"><div class="wrap">
  <h2>Calendario · 10 al 30 de noviembre de 2026</h2>
  <p class="intro">21 días, día por día. Todas las piezas se publican en <span class="net net-ig">Instagram</span> y <span class="net net-fb">Facebook</span>; <span class="net net-tt">TikTok</span> y <span class="net net-yt">YouTube</span> (Shorts) solo en las fechas que indica cada pieza. Todas las piezas están en estado <b>Borrador</b>. Los posts del 2, 4 y 7-nov nunca salieron y quedan a decidir: recuperar o seguir desde el 10-nov.</p>
  <div class="cal">__CALENDAR__</div>
</div></section>

<section><div class="wrap">
  <h2>Banco de scripts · 26 reels</h2>
  <p class="intro">Guiones rankeados con el método Kallaway (hook 0–3 s, cuerpo por beats, un solo CTA). Están escritos en inglés, como el material fuente. Hacé clic en cada uno para ver el hook, el cuerpo, el CTA y el caption.</p>
  __SCRIPTS__
</div></section>

<section style="background:#fff"><div class="wrap">
  <h2>Piezas gráficas · 15 productos</h2>
  <p class="intro">Clasificación por tipo, con lo que falta para producir cada una. Antes/después y testimoniales solo con fotos reales y consentimiento. Ninguna pieza se produce con fotos generadas ni de stock.</p>
  <div class="band"><img src="assets/flatlay.png" alt="" onerror="this.remove()"><span>«More offers to explore» — las ofertas, en tarjetas</span></div>
  <div class="grid">__GRAPHICS__</div>
</div></section>

<section><div class="wrap">
  <h2>Ofertas vigentes · Q4 2026</h2>
  <p class="intro">Solo las ofertas verificadas del documento Q4. Las de Gold Friday (27–30 nov) están <b>a confirmar por Rosanna</b>: no se usan sus precios hasta que ella los confirme.</p>
  <div class="band"><img src="assets/texture.png" alt="" onerror="this.remove()"><span>«Ready to Claim This Month's Offer? Call (305) 356-7402»</span></div>
  <div class="grid">__OFFERS__</div>
  <p class="intro" style="margin-top:18px">Diciembre (Lip Filler «The Midnight Kiss» 15% off · QuantumRF «New Year, Already Snatched» · Gift Cards «Drop a Hint» $250 + $50 bonus) se programa en el calendario de diciembre, no en este portal.</p>
</div></section>

<section style="background:#fff"><div class="wrap">
  <h2>Pendientes de confirmación</h2>
  <p class="intro">Lo que todavía necesita una decisión de Rosanna (o de Daniel) antes de producir o publicar:</p>
  <div class="pend"><ul>__PENDIENTES__</ul></div>
</div></section>

<footer>
  <div class="wrap">
    <p><b>Borradores — nada se publica sin la aprobación de Rosanna.</b></p>
    <p style="margin-top:8px">Med Aesthetics Miami · (305) 356-7402 · info@medaestheticsmiami.com<br>Portal preparado por <a href="https://muviproject.com">MuViProject</a> · Noviembre 2026</p>
  </div>
</footer>
<div id="modal-overlay" class="modal-overlay" onclick="if(event.target===this)closePreview()">
  <div class="modal" role="dialog" aria-modal="true" aria-label="Vista previa">
    <button type="button" class="modal-close" onclick="closePreview()" aria-label="Cerrar">×</button>
    <div id="modal-body"></div>
  </div>
</div>
<script>
/* Vista previa: clona la pieza en el modal, con su botón de aprobar y su
   cajita de feedback. Cierra con la X, con clic fuera del popup, o con
   Escape. Mientras está abierto, el fondo no hace scroll. */
var _pvScroll = 0;
function openPreview(btn){
  var piece = btn.closest('article, details');
  if(!piece) return;
  var clone = piece.cloneNode(true);
  var pv = clone.querySelector('.pv');
  if(pv) pv.remove();
  if(clone.tagName === 'DETAILS') clone.setAttribute('open', '');
  var body = document.getElementById('modal-body');
  body.innerHTML = '';
  body.appendChild(clone);
  document.getElementById('modal-overlay').classList.add('open');
  _pvScroll = window.scrollY || 0;
  document.body.style.overflow = 'hidden';
  var c = document.querySelector('.modal-close');
  if(c) c.focus();
}
function closePreview(){
  document.getElementById('modal-overlay').classList.remove('open');
  document.getElementById('modal-body').innerHTML = '';
  document.body.style.overflow = '';
  window.scrollTo(0, _pvScroll);
}
document.addEventListener('keydown', function(ev){
  if(ev.key === 'Escape') closePreview();
});
</script>
<script>
/* Feedback por WhatsApp: abre WhatsApp con "Sobre [pieza]: [comentario]".
   No envía nada solo: el mensaje se manda solo si Rosanna pulsa Enviar
   en WhatsApp. Si la cajita está vacía, no abre nada. */
function mamFeedback(btn){
  var box = btn.parentElement;
  var ta = box ? box.querySelector('textarea') : null;
  var txt = ta ? ta.value.trim() : '';
  if (!txt) { alert('Escribí tu comentario sobre esta pieza antes de enviarlo.'); if (ta) ta.focus(); return; }
  var piece = btn.getAttribute('data-piece') || 'esta pieza';
  var url = 'https://wa.me/18456996606?text=' + encodeURIComponent('Sobre ' + piece + ': ' + txt);
  window.open(url, '_blank');
}
</script>
</body>
</html>
"""

def build():
    out = TPL.replace("__CSS__", CSS)
    out = out.replace("__CALENDAR__", cal_rows())
    out = out.replace("__SCRIPTS__", script_blocks())
    out = out.replace("__GRAPHICS__", graphic_cards())
    out = out.replace("__OFFERS__", offer_cards())
    out = out.replace("__PENDIENTES__", "".join("<li>%s</li>" % esc(p) for p in PENDIENTES))
    return out

README = """# Med Aesthetics Miami — Portal del cliente (MuViProject)

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
"""

if __name__ == "__main__":
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base, "index.html"), "w", encoding="utf-8") as f:
        f.write(build())
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    print("OK: index.html + README.md generados")
