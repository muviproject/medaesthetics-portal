#!/usr/bin/env python3
"""Mockup borrador del carrusel G-02 (10-nov) para el portal de Med Aesthetics.
Diseño con PIL (determinista): sin fotos de pacientes inventadas — los marcos
de ANTES/DESPUÉS son placeholders explícitos, pendientes de la foto real
con consentimiento que pasa Rosanna. Estilo brandbook: dorado #e3b533,
gris #606163, fondo crema. Formato carrusel IG 4:5 (1080x1350).
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.expanduser(
    "~/workspace/goals/vallure-agency-partnership-response/files/med-aesthetics-portal/assets")
W, H = 1080, 1350
GOLD = (227, 181, 51)
GRAY = (96, 97, 99)
DARK = (43, 43, 43)
CREAM = (251, 248, 241)
WHITE = (255, 255, 255)
LIGHT_GOLD_BG = (253, 246, 224)


def font(sz, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/" + name, sz)


def center(draw, y, text, fnt, fill, tracking=0):
    # centrado simple (sin tracking real; PIL no lo soporta directo)
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 8


def dashed_rect(draw, box, fill, dash=18, gap=12, width=3):
    x0, y0, x1, y1 = box
    x = x0
    while x < x1:
        draw.line([(x, y0), (min(x + dash, x1), y0)], fill=fill, width=width)
        draw.line([(x, y1), (min(x + dash, x1), y1)], fill=fill, width=width)
        x += dash + gap
    y = y0
    while y < y1:
        draw.line([(x0, y), (x0, min(y + dash, y1))], fill=fill, width=width)
        draw.line([(x1, y), (x1, min(y + dash, y1))], fill=fill, width=width)
        y += dash + gap


def base(tag):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 16], fill=GOLD)  # barra dorada superior
    # tag BORRADOR arriba a la izquierda
    d.rounded_rectangle([36, 44, 300, 96], radius=26, fill=GOLD)
    d.text((66, 58), "BORRADOR", font=font(30, True), fill=WHITE)
    # pie fijo
    d.text((36, H - 120), "Med Aesthetics Miami", font=font(30, True), fill=GRAY)
    d.text((36, H - 78), "(305) 356-7402", font=font(30), fill=GRAY)
    d.text((W - 36 - d.textlength("1 / 3", font=font(28)), H - 120),
           tag, font=font(28), fill=GRAY)
    return img, d


def cover():
    img, d = base("1 / 3")
    y = 210
    y = center(d, y, "MED AESTHETICS MIAMI", font(38, True), GRAY)
    y += 30
    d.line([(W // 2 - 90, y), (W // 2 + 90, y)], fill=GOLD, width=6)
    y += 46
    y = center(d, y, "QuantumRF", font(150, True), DARK)
    y = center(d, y, "Men Included", font(96, True), GOLD)
    y += 40
    y = center(d, y, "Before & After  ·  Abdomen", font(44), GRAY)
    y += 90
    y = center(d, y, "Deslizá para ver el", font(40), GRAY)
    y = center(d, y, "antes y el después  →", font(40, True), GRAY)
    y = H - 220
    d.text(((W - d.textlength("Individual results vary", font=font(28))) / 2, y),
           "Individual results vary", font=font(28), fill=GRAY)
    img.save(os.path.join(OUT, "carousel-10nov-1.png"))


def photo_slide(label, tag, cta=None):
    img, d = base(tag)
    y = 200
    y = center(d, y, label, font(120, True), DARK)
    d.line([(W // 2 - 90, y + 8), (W // 2 + 90, y + 8)], fill=GOLD, width=6)
    # marco placeholder con borde punteado
    box = (110, 420, W - 110, 980)
    dashed_rect(d, box, GOLD, width=4)
    d.rectangle([box[0] + 4, box[1] + 4, box[2] - 4, box[3] - 4], fill=LIGHT_GOLD_BG)
    cy = 560
    cy = center(d, cy, "FOTO REAL", font(64, True), GRAY)
    cy = center(d, cy, "PENDIENTE", font(64, True), GRAY)
    cy += 30
    cy = center(d, cy, "La pasa Rosanna", font(38), GRAY)
    cy = center(d, cy, "con consentimiento", font(38), GRAY)
    y = 1030
    if cta:
        y = center(d, y, cta, font(44, True), DARK)
    else:
        y = center(d, y, "QuantumRF  ·  Abdomen", font(40), GRAY)
    d.text(((W - d.textlength("Individual results vary", font=font(28))) / 2, H - 220),
           "Individual results vary", font=font(28), fill=GRAY)
    img.save(os.path.join(OUT, "carousel-10nov-%s.png" % tag.split(" / ")[0]))


cover()
photo_slide("ANTES", "2 / 3")
photo_slide("DESPUÉS", "3 / 3", cta="Book your consultation")
print("OK: 3 slides en", OUT)
