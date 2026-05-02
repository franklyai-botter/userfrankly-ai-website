from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
FRAMES = 72
FPS_MS = 45

INK = (3, 12, 16)
PANEL = (6, 20, 26)
IVORY = (245, 241, 232)
SILVER = (205, 206, 210)
MUTED = (154, 157, 164)
CYAN = (63, 212, 224)
GREEN = (69, 226, 168)
GOLD = (212, 175, 55)
RED = (255, 110, 127)
BLUE = (110, 168, 255)
VIOLET = (185, 128, 255)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


F_TITLE = font(22, True)
F_BODY = font(15)
F_SMALL = font(12, True)
F_TINY = font(10, True)
F_HERO = font(28, True)


def mix(color: tuple[int, int, int], alpha: int) -> tuple[int, int, int, int]:
    return color[0], color[1], color[2], alpha


def bezier(points: tuple[tuple[float, float], tuple[float, float], tuple[float, float], tuple[float, float]], steps: int = 100) -> list[tuple[float, float]]:
    p0, p1, p2, p3 = points
    out: list[tuple[float, float]] = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        out.append((x, y))
    return out


def path_point(path: list[tuple[float, float]], t: float) -> tuple[float, float]:
    t = t % 1.0
    idx = min(len(path) - 2, max(0, int(t * (len(path) - 1))))
    local = t * (len(path) - 1) - idx
    x = path[idx][0] + (path[idx + 1][0] - path[idx][0]) * local
    y = path[idx][1] + (path[idx + 1][1] - path[idx][1]) * local
    return x, y


def draw_background(base: Image.Image) -> None:
    draw = ImageDraw.Draw(base, "RGBA")
    draw.rectangle((0, 0, W, H), fill=INK)

    for radius, alpha, color, cx, cy in [
        (420, 70, CYAN, 620, 190),
        (360, 42, GREEN, 840, 430),
        (300, 28, GOLD, 150, 120),
    ]:
        blob = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        bdraw = ImageDraw.Draw(blob, "RGBA")
        bdraw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=mix(color, alpha))
        base.alpha_composite(blob.filter(ImageFilter.GaussianBlur(radius // 2)))

    for x in range(-80, W + 80, 92):
        draw.line((x, 0, x + 160, H), fill=(63, 212, 224, 18), width=1)
    for y in range(72, H, 72):
        draw.line((0, y, W, y), fill=(63, 212, 224, 16), width=1)

    draw.rounded_rectangle((20, 38, W - 20, H - 38), radius=24, outline=(205, 206, 210, 30), width=1)
    draw.ellipse((-90, H - 112, W + 90, H + 120), outline=(212, 175, 55, 28), width=2)
    draw.ellipse((-110, H - 106, W + 110, H + 128), outline=(63, 212, 224, 16), width=1)


def glow_line(layer: Image.Image, pts: Iterable[tuple[float, float]], color: tuple[int, int, int], width: int = 3) -> None:
    pts2 = [(int(x), int(y)) for x, y in pts]
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow, "RGBA")
    for w, a in [(18, 36), (10, 58), (5, 95)]:
        gdraw.line(pts2, fill=mix(color, a), width=w, joint="curve")
    layer.alpha_composite(glow.filter(ImageFilter.GaussianBlur(5)))
    draw = ImageDraw.Draw(layer, "RGBA")
    draw.line(pts2, fill=mix(color, 225), width=width, joint="curve")
    draw.line(pts2, fill=(255, 255, 255, 90), width=1, joint="curve")


def draw_packet(layer: Image.Image, x: float, y: float, color: tuple[int, int, int], size: int = 8) -> None:
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow, "RGBA")
    gdraw.ellipse((x - size * 4, y - size * 4, x + size * 4, y + size * 4), fill=mix(color, 105))
    layer.alpha_composite(glow.filter(ImageFilter.GaussianBlur(12)))
    draw = ImageDraw.Draw(layer, "RGBA")
    draw.ellipse((x - size, y - size, x + size, y + size), fill=mix(color, 245))
    draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(255, 255, 255, 210))


def wrap_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, fnt: ImageFont.FreeTypeFont) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        probe = f"{current} {word}".strip()
        if draw.textbbox((0, 0), probe, font=fnt)[2] <= max_width:
            current = probe
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def icon(draw: ImageDraw.ImageDraw, kind: str, x: int, y: int, color: tuple[int, int, int]) -> None:
    cx, cy = x + 20, y + 30
    if kind == "mail":
        draw.rounded_rectangle((cx - 18, cy - 13, cx + 18, cy + 13), radius=4, outline=mix(color, 220), width=2)
        draw.line((cx - 18, cy - 12, cx, cy + 2, cx + 18, cy - 12), fill=mix(color, 180), width=2)
    elif kind == "doc":
        draw.rounded_rectangle((cx - 15, cy - 18, cx + 15, cy + 18), radius=3, outline=mix(color, 220), width=2)
        for yy in [-6, 2, 10]:
            draw.line((cx - 8, cy + yy, cx + 9, cy + yy), fill=mix(color, 155), width=2)
    elif kind == "search":
        draw.ellipse((cx - 13, cy - 13, cx + 10, cy + 10), outline=mix(color, 225), width=2)
        draw.line((cx + 8, cy + 8, cx + 18, cy + 18), fill=mix(color, 225), width=2)
    elif kind == "ai":
        draw.rounded_rectangle((cx - 15, cy - 15, cx + 15, cy + 15), radius=6, outline=mix(color, 220), width=2)
        draw.ellipse((cx - 7, cy - 4, cx - 3, cy), fill=mix(color, 220))
        draw.ellipse((cx + 3, cy - 4, cx + 7, cy), fill=mix(color, 220))
        draw.arc((cx - 8, cy - 2, cx + 8, cy + 11), 15, 165, fill=mix(color, 200), width=2)
        draw.line((cx, cy - 15, cx, cy - 23), fill=mix(color, 200), width=2)
    elif kind == "risk":
        for i, c in enumerate([GREEN, GOLD, RED]):
            draw.ellipse((cx - 15 + i * 15, cy - 7, cx - 5 + i * 15, cy + 3), fill=mix(c, 230))
    else:
        draw.text((cx - 13, cy - 18), "{}", font=F_HERO, fill=mix(color, 230))


def node(layer: Image.Image, item: dict) -> None:
    x, y, w, h = item["box"]
    color = item["color"]
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow, "RGBA")
    gdraw.rounded_rectangle((x - 3, y - 3, x + w + 3, y + h + 3), radius=11, fill=mix(color, 65))
    layer.alpha_composite(glow.filter(ImageFilter.GaussianBlur(14)))

    draw = ImageDraw.Draw(layer, "RGBA")
    draw.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=(4, 21, 27, 230), outline=mix(color, 235), width=2)
    draw.rounded_rectangle((x + 4, y + 4, x + w - 4, y + h - 4), radius=8, outline=(255, 255, 255, 28), width=1)

    draw.ellipse((x - 7, y + h / 2 - 7, x + 7, y + h / 2 + 7), fill=mix(color, 230))
    draw.ellipse((x + w - 7, y + h / 2 - 7, x + w + 7, y + h / 2 + 7), fill=mix(color, 230))
    icon(draw, item.get("icon", "code"), x + 6, y + 14, color)
    draw.text((x + 54, y + 16), item["eyebrow"], font=F_TINY, fill=mix(color, 230))
    draw.text((x + 54, y + 38), item["title"], font=F_TITLE, fill=mix(IVORY, 245))

    if item.get("caption"):
        lines = wrap_text(draw, item["caption"], w + 22, F_BODY)[:2]
        yy = y + h + 14
        for line in lines:
            tw = draw.textbbox((0, 0), line, font=F_BODY)[2]
            draw.text((x + w / 2 - tw / 2, yy), line, font=F_BODY, fill=mix(MUTED, 210))
            yy += 19


def draw_connection_labels(layer: Image.Image, connections: list[dict]) -> None:
    draw = ImageDraw.Draw(layer, "RGBA")
    for con in connections:
        if not con.get("label"):
            continue
        x, y = path_point(con["path"], con.get("label_at", 0.52))
        text = con["label"]
        tw, th = draw.textbbox((0, 0), text, font=F_SMALL)[2:]
        draw.text((x - tw / 2, y - 25), text, font=F_SMALL, fill=mix(con["color"], 230))


def draw_case(case: dict, frame: int) -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    draw_background(img)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((58, 56), case["kicker"], font=F_SMALL, fill=mix(GOLD, 230))
    draw.text((58, 78), case["headline"], font=F_HERO, fill=mix(IVORY, 240))

    for con in case["connections"]:
        glow_line(img, con["path"], con["color"], con.get("width", 3))

    draw_connection_labels(img, case["connections"])

    phase = frame / FRAMES
    for con in case["connections"]:
        speed = con.get("speed", 1.0)
        for offset in con.get("offsets", [0.0]):
            x, y = path_point(con["path"], phase * speed + offset)
            draw_packet(img, x, y, con["color"], con.get("packet", 7))

    for item in case["nodes"]:
        node(img, item)

    # Soft reflection at the bottom, matching the luminous reference style.
    reflection = img.crop((0, 420, W, H)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    reflection = reflection.resize((W, 160))
    reflection.putalpha(34)
    img.alpha_composite(reflection.filter(ImageFilter.GaussianBlur(7)), (0, H - 148))

    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette, "RGBA")
    vdraw.rectangle((0, 0, W, H), outline=(0, 0, 0, 0))
    for i in range(70):
        a = int(i * 2.4)
        vdraw.rectangle((i, i, W - i, H - i), outline=(0, 0, 0, a // 6))
    img.alpha_composite(vignette)
    return img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)


def c(p0, p1, p2, p3, color, label="", label_at=0.5, speed=1.0, offsets=None):
    return {
        "path": bezier((p0, p1, p2, p3), 120),
        "color": color,
        "label": label,
        "label_at": label_at,
        "speed": speed,
        "offsets": offsets or [0.0, 0.55],
    }


def n(x, y, w, h, color, eyebrow, title, caption, icon_name="code"):
    return {
        "box": (x, y, w, h),
        "color": color,
        "eyebrow": eyebrow,
        "title": title,
        "caption": caption,
        "icon": icon_name,
    }


CASES = [
    {
        "file": OUT / "mail-neon-workflow.gif",
        "kicker": "CASE 01 / E-MAILS ENTLASTEN",
        "headline": "Wichtige Mails zuerst. Entwuerfe vorbereitet.",
        "nodes": [
            n(80, 306, 190, 90, GREEN, "EINGANG", "Neue Mail", "Nachricht, Anhang, Termin.", "mail"),
            n(330, 220, 180, 84, GOLD, "FILTER", "Wichtig", "Frist, Absender, Thema.", "code"),
            n(330, 420, 180, 84, GOLD, "FILTER", "Routine", "Newsletter, Info, Ablage.", "code"),
            n(585, 316, 206, 94, CYAN, "ASSISTENT", "Einordnen", "Dringend, Antwort, spaeter.", "ai"),
            n(900, 150, 178, 84, RED, "HEUTE", "Handeln", "Sofort sichtbar.", "doc"),
            n(900, 316, 178, 84, GOLD, "ENTWURF", "Antwort", "Vorbereitet, nicht gesendet.", "doc"),
            n(900, 486, 178, 84, BLUE, "SPAETER", "Ablage", "Lesen oder ablegen.", "doc"),
            n(1100, 316, 120, 84, GREEN, "FREIGABE", "Mensch", "Sendet erst nach OK.", "risk"),
        ],
        "connections": [
            c((270, 350), (300, 350), (304, 262), (330, 262), GREEN, "1 Mail"),
            c((270, 350), (300, 350), (304, 462), (330, 462), GREEN, "1 Mail"),
            c((510, 262), (548, 262), (545, 352), (585, 352), GOLD, "Kontext"),
            c((510, 462), (548, 462), (545, 372), (585, 372), GOLD, "Noise"),
            c((791, 363), (835, 363), (830, 192), (900, 192), RED, "Heute", 0.58),
            c((791, 363), (835, 363), (850, 358), (900, 358), GOLD, "Entwurf", 0.58),
            c((791, 363), (835, 363), (830, 528), (900, 528), BLUE, "Spaeter", 0.58),
            c((1078, 358), (1090, 358), (1090, 358), (1100, 358), GREEN, "OK"),
        ],
    },
    {
        "file": OUT / "documents-neon-workflow.gif",
        "kicker": "CASE 02 / DOKUMENTE VERSTEHEN",
        "headline": "Aus Ordnern werden Antworten mit Fundstellen.",
        "nodes": [
            n(80, 300, 170, 88, CYAN, "DATEI", "PDF", "Vertrag, Rechnung, Akte.", "doc"),
            n(300, 180, 175, 84, GREEN, "ORDNER", "Scans", "Mehrere Dateien.", "doc"),
            n(300, 414, 175, 84, GREEN, "INPUT", "Bilder", "Bild-PDFs und Fotos.", "doc"),
            n(540, 300, 190, 88, GOLD, "LESBAR", "OCR", "Bild wird Text.", "search"),
            n(790, 205, 190, 88, CYAN, "BELEG", "Fundstelle", "Seite und Passage.", "doc"),
            n(790, 410, 190, 88, CYAN, "LOKAL", "Analyse", "Auf dem eigenen System.", "ai"),
            n(1050, 210, 170, 84, GREEN, "OUT A", "Kurzblick", "Was steht drin?", "doc"),
            n(1050, 415, 170, 84, BLUE, "OUT B", "Bausteine", "Angebot, Liste, Antwort.", "doc"),
        ],
        "connections": [
            c((250, 344), (280, 344), (275, 222), (300, 222), CYAN, "Datei"),
            c((250, 344), (280, 344), (275, 456), (300, 456), CYAN, "Scan"),
            c((475, 222), (510, 222), (500, 344), (540, 344), GREEN, "Text"),
            c((475, 456), (510, 456), (500, 344), (540, 344), GREEN, "Text"),
            c((730, 344), (760, 344), (755, 247), (790, 247), GOLD, "Quelle"),
            c((730, 344), (760, 344), (755, 452), (790, 452), GOLD, "Analyse"),
            c((980, 247), (1018, 247), (1015, 252), (1050, 252), GREEN, "Belegbar"),
            c((980, 452), (1018, 452), (1015, 457), (1050, 457), BLUE, "Output"),
        ],
    },
    {
        "file": OUT / "answers-neon-workflow.gif",
        "kicker": "CASE 03 / ANTWORTEN SICHERN",
        "headline": "Quellen zuerst. Dann Risiko-Ampel.",
        "nodes": [
            n(80, 312, 175, 88, CYAN, "FRAGE", "Anliegen", "Was soll entschieden werden?", "search"),
            n(310, 210, 185, 84, GREEN, "QUELLEN", "Suchen", "Dokumente und Passagen.", "doc"),
            n(310, 425, 185, 84, GREEN, "WISSEN", "Abgleich", "Nur passende Belege.", "doc"),
            n(570, 312, 190, 90, CYAN, "ANTWORT", "Entwurf", "Mit Quellenhinweis.", "ai"),
            n(825, 312, 180, 90, GOLD, "AMPEL", "Risiko", "Auswirkung und Regeln.", "risk"),
            n(1070, 130, 160, 82, GREEN, "GRUEN", "Nutzen", "Direkt verwendbar.", "doc"),
            n(1070, 314, 160, 82, GOLD, "GELB", "Pruefen", "Mensch gibt frei.", "doc"),
            n(1070, 500, 160, 82, RED, "ROT", "Stop", "Fachpruefung statt Auto-Aktion.", "doc"),
        ],
        "connections": [
            c((255, 356), (285, 356), (278, 252), (310, 252), CYAN, "Frage"),
            c((255, 356), (285, 356), (278, 467), (310, 467), CYAN, "Scope"),
            c((495, 252), (535, 252), (530, 356), (570, 356), GREEN, "Quellen"),
            c((495, 467), (535, 467), (530, 356), (570, 356), GREEN, "Kontext"),
            c((760, 356), (790, 356), (795, 356), (825, 356), CYAN, "Antwort"),
            c((1005, 356), (1035, 356), (1015, 171), (1070, 171), GREEN, "Low"),
            c((1005, 356), (1035, 356), (1035, 356), (1070, 356), GOLD, "Middle"),
            c((1005, 356), (1035, 356), (1015, 541), (1070, 541), RED, "High"),
        ],
    },
    {
        "file": OUT / "rag-model-neon-workflow.gif",
        "kicker": "CASE 03 / RAG MODELL",
        "headline": "Frage rein. Quellen finden. Antwort belegen.",
        "nodes": [
            n(80, 312, 175, 88, CYAN, "FRAGE", "Anliegen", "Was soll beantwortet werden?", "search"),
            n(310, 185, 185, 84, GREEN, "INDEX", "Wissen", "Dokumente und Textstellen.", "doc"),
            n(310, 440, 185, 84, BLUE, "FILTER", "Scope", "Nur passende Inhalte.", "code"),
            n(565, 312, 205, 90, GOLD, "KONTEXT", "Paket", "Kleine Auswahl relevanter Belege.", "doc"),
            n(835, 225, 190, 88, CYAN, "MODELL", "Antwort", "Formuliert mit Kontext.", "ai"),
            n(835, 430, 190, 88, GREEN, "BELEGE", "Quellen", "Fundstellen bleiben sichtbar.", "doc"),
            n(1080, 312, 150, 88, GREEN, "OUT", "Belegt", "Antwort mit Quellen.", "doc"),
        ],
        "connections": [
            c((255, 356), (285, 356), (278, 227), (310, 227), CYAN, "Frage"),
            c((255, 356), (285, 356), (278, 482), (310, 482), CYAN, "Scope"),
            c((495, 227), (535, 227), (525, 356), (565, 356), GREEN, "Passagen"),
            c((495, 482), (535, 482), (525, 356), (565, 356), BLUE, "Auswahl"),
            c((770, 356), (805, 356), (800, 269), (835, 269), GOLD, "Kontext"),
            c((770, 356), (805, 356), (800, 474), (835, 474), GOLD, "Belege"),
            c((1025, 269), (1060, 269), (1052, 356), (1080, 356), CYAN, "Antwort"),
            c((1025, 474), (1060, 474), (1052, 356), (1080, 356), GREEN, "Quellen"),
        ],
    },
]


def render() -> None:
    for case in CASES:
        frames = [draw_case(case, frame) for frame in range(FRAMES)]
        frames[0].save(
            case["file"],
            save_all=True,
            append_images=frames[1:],
            duration=FPS_MS,
            loop=0,
            optimize=True,
        )
        preview = draw_case(case, 12).convert("RGB")
        preview.save(case["file"].with_suffix(".png"), quality=94)
        print(f"wrote {case['file']}")


if __name__ == "__main__":
    render()
