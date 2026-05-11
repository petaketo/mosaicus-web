from PIL import Image, ImageDraw, ImageFont
import os

SIZE = 1024
img = Image.new("RGB", (SIZE, SIZE), (230, 0, 35))
draw = ImageDraw.Draw(img)

for r in range(SIZE, 0, -4):
    alpha = (SIZE - r) / SIZE
    shade = int(230 - 80 * alpha)
    draw.ellipse([(SIZE - r) // 2, (SIZE - r) // 2, (SIZE + r) // 2, (SIZE + r) // 2],
                 fill=(shade, max(0, 20 - int(20 * alpha)), max(35 - int(20 * alpha), 0)))

text = "LM"
font = None
for candidate in [
    "C:/Windows/Fonts/segoeuib.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/Arial.ttf",
]:
    if os.path.exists(candidate):
        font = ImageFont.truetype(candidate, 480)
        break

bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1] - 20
draw.text((x, y), text, fill=(255, 255, 255), font=font)

out = "icon-1024.png"
img.save(out, "PNG")
print(f"Wrote {out}")
