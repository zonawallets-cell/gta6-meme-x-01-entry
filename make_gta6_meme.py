#!/usr/bin/env python3
"""GTA 6 meme for make.fun bounty gta6-meme-x-01. Drawn programmatically with PIL.

Concept: Vice City synthwave sunset. Top caption "WAITED 13 YEARS", neon
"GTA VI" over the sun, the make.fun ghost (white, thick black outline, two
black four-pointed sparkle eyes, round little hand holding a magenta coin
with a white star) chilling on the sand, bottom caption "FOR ONE SICK DAY".
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1024
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01-meme.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img, "RGBA")

# ---------- sky gradient ----------
top = (43, 16, 85)      # deep purple
mid = (190, 30, 120)    # magenta
low = (255, 110, 60)    # orange
for y in range(641):
    if y < 320:
        t = y / 320
        c = tuple(int(top[i] + (mid[i] - top[i]) * t) for i in range(3))
    else:
        t = (y - 320) / 320
        c = tuple(int(mid[i] + (low[i] - mid[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

# ---------- stars in the upper sky (edges only, caption sits centre) ----------
import random
random.seed(6)
for _ in range(60):
    x = random.randint(0, W)
    y = random.randint(0, 200)
    if 220 < x < 800 and y < 150:
        continue
    r = random.choice([1, 1, 2])
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, random.randint(90, 200)))

# ---------- retro sun with slits ----------
sun_cx, sun_cy, sun_r = 400, 360, 155
sun = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(sun)
for r in range(sun_r, 0, -1):
    t = 1 - r / sun_r
    c = (255, int(214 - 110 * t), int(90 + 60 * t))
    sd.ellipse([sun_cx - r, sun_cy - r, sun_cx + r, sun_cy + r], fill=c + (255,))
# horizontal slits across the lower half of the sun only (clipped to the disc)
for sy, sh in [(400, 7), (430, 9), (464, 11), (500, 13)]:
    dy = sy + sh / 2 - sun_cy
    half = math.sqrt(max(sun_r * sun_r - dy * dy, 0))
    sd.rectangle([sun_cx - half, sy, sun_cx + half, sy + sh], fill=(43, 16, 85, 255))
img.paste(Image.alpha_composite(img.convert("RGBA"), sun).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

# ---------- ocean ----------
for y in range(641, 801):
    t = (y - 641) / 160
    c = (int(38 + 30 * t), int(16 + 20 * t), int(84 + 40 * t))
    d.line([(0, y), (W, y)], fill=c)
# sun reflection streak: soft vertical glow under the sun, fading down
refl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
rd = ImageDraw.Draw(refl)
for y in range(645, 800):
    t = (y - 645) / 155
    wdt = int(150 - 70 * t)
    rd.line([(sun_cx - wdt // 2, y), (sun_cx + wdt // 2, y)],
            fill=(255, 150, 80, int(170 * (1 - t))))
refl = refl.filter(ImageFilter.GaussianBlur(6))
img.paste(Image.alpha_composite(img.convert("RGBA"), refl).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

# ---------- sand ----------
for y in range(801, H):
    t = (y - 801) / 223
    c = (int(232 - 40 * t), int(164 - 50 * t), int(110 - 30 * t))
    d.line([(0, y), (W, y)], fill=c)

# ---------- palm tree silhouette (left) ----------
palm = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pd = ImageDraw.Draw(palm)
PALM = (26, 10, 46, 255)
# trunk: curved, thick
pts = []
for i in range(41):
    t = i / 40
    x = 150 + 55 * math.sin(t * 1.15) - 10 * t
    y = 800 - t * 520
    pts.append((x, y))
pd.line(pts, fill=PALM, width=26, joint="curve")
# fronds from the crown (205, 285)
crown = (205, 285)
for ang, ln in [(-160, 190), (-120, 210), (-80, 220), (-40, 200), (-5, 180), (30, 150), (155, 170), (115, 190)]:
    a = math.radians(ang)
    tip = (crown[0] + ln * math.cos(a), crown[1] + ln * math.sin(a) * 0.55)
    mid1 = (crown[0] + ln * 0.45 * math.cos(a), crown[1] + ln * 0.45 * math.sin(a) * 0.55 - 28)
    seg = []
    for i in range(21):
        t = i / 20
        x = (1 - t) ** 2 * crown[0] + 2 * (1 - t) * t * mid1[0] + t * t * tip[0]
        y = (1 - t) ** 2 * crown[1] + 2 * (1 - t) * t * mid1[1] + t * t * tip[1] + 26 * t * t
        seg.append((x, y))
    pd.line(seg, fill=PALM, width=13, joint="curve")
# coconuts
pd.ellipse([188, 292, 206, 310], fill=PALM)
pd.ellipse([206, 296, 224, 314], fill=PALM)
img.paste(Image.alpha_composite(img.convert("RGBA"), palm).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

# ---------- neon "GTA VI" ----------
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
f_gta = ImageFont.truetype(BOLD, 128)
txt = "GTA VI"
bbox = gd.textbbox((0, 0), txt, font=f_gta)
tw = bbox[2] - bbox[0]
gd.text(((460 - tw / 2), 500), txt, font=f_gta, fill=(255, 46, 154, 255))
glow = glow.filter(ImageFilter.GaussianBlur(14))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")
d.text(((460 - tw / 2), 500), txt, font=f_gta, fill=(255, 255, 255, 255))

# ---------- make.fun ghost (drawn, worked into the scene on the sand) ----------
ghost = Image.new("RGBA", (400, 360), (0, 0, 0, 0))
gd = ImageDraw.Draw(ghost)
# body outline (black, slightly larger) then white body
body_black = [(200, 18)]
# build ghost silhouette as polygon: top arc + sides + wavy bottom
poly = []
for a in range(180, 361, 6):
    r = math.radians(a)
    poly.append((200 + 105 * math.cos(r), 130 + 112 * math.sin(r)))
# left side down
poly += [(95, 130), (95, 285)]
# wavy bottom: 3 scallops
for i, cx in enumerate([95, 148, 201, 254, 305]):
    pass
scallops = []
for i in range(4):
    x0 = 95 + i * 52.5
    for a in range(0, 181, 10):
        r = math.radians(a)
        scallops.append((x0 + 26.25 + 26.25 * math.cos(r), 285 + 26.25 * math.sin(r)))
poly += scallops
poly += [(305, 285), (305, 130)]
gd.polygon(poly, fill=(0, 0, 0, 255))
# white inner body, inset ~11px
poly2 = []
for a in range(180, 361, 6):
    r = math.radians(a)
    poly2.append((200 + 94 * math.cos(r), 130 + 101 * math.sin(r)))
poly2 += [(106, 130), (106, 283)]
for i in range(4):
    x0 = 106 + i * 47
    for a in range(0, 181, 10):
        r = math.radians(a)
        poly2.append((x0 + 23.5 + 23.5 * math.cos(r), 283 + 23.5 * math.sin(r)))
poly2 += [(294, 283), (294, 130)]
gd.polygon(poly2, fill=(255, 255, 255, 255))


def sparkle(cx, cy, r):
    pts = []
    for i in range(8):
        ang = math.pi / 2 + i * math.pi / 4
        rr = r if i % 2 == 0 else r * 0.22
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return pts


gd.polygon(sparkle(158, 165, 30), fill=(0, 0, 0, 255))
gd.polygon(sparkle(242, 165, 30), fill=(0, 0, 0, 255))
# round little hand on the right side, holding the coin
gd.ellipse([288, 205, 330, 247], fill=(0, 0, 0, 255))
gd.ellipse([293, 210, 325, 242], fill=(255, 255, 255, 255))
# magenta coin with white star, overlapping the hand
gd.ellipse([306, 168, 382, 244], fill=(0, 0, 0, 255))
gd.ellipse([311, 173, 377, 239], fill=(230, 0, 126, 255))


def star5(cx, cy, r_out, r_in):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r_out if i % 2 == 0 else r_in
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return pts


gd.polygon(star5(344, 206, 24, 10), fill=(255, 255, 255, 255))
ghost = ghost.resize((300, 270), Image.LANCZOS)
img.paste(ghost, (690, 610), ghost)
d = ImageDraw.Draw(img, "RGBA")

# small "make.fun" credit on the sand, bottom-left
f_small = ImageFont.truetype(BOLD, 40)
d.text((36, 838), "make.fun", font=f_small, fill=(255, 255, 255, 255),
       stroke_width=2, stroke_fill=(0, 0, 0, 255))

# ---------- captions ----------
f_top = ImageFont.truetype(BOLD, 96)
f_bot = ImageFont.truetype(BOLD, 88)


def centered(y, text, font):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    d.text(((W - tw) / 2, y), text, font=font, fill=(255, 255, 255, 255),
           stroke_width=6, stroke_fill=(0, 0, 0, 255))


centered(28, "WAITED 13 YEARS", f_top)
centered(902, "FOR ONE SICK DAY", f_bot)

img.save(OUT)
print("saved", OUT, img.size)
