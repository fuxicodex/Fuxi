#!/usr/bin/env python3
"""Generate the FuXi social preview card (1280x640) for GitHub."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
HELV = "/System/Library/Fonts/Helvetica.ttc"
HELV_BOLD = "/System/Library/Fonts/Helvetica.ttc"
PINGFANG = "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"

BRAND = (10, 111, 231)        # #0a6fe7
DARK = (9, 14, 28)            # #090e1c
WHITE = (255, 255, 255)
SOFT = (170, 190, 220)

img = Image.new("RGB", (W, H), DARK)
d = ImageDraw.Draw(img)

# Diagonal brand-blue glow in the top-left corner.
for i in range(420, 0, -2):
    alpha = i / 420
    r = int(BRAND[0] * alpha + DARK[0] * (1 - alpha))
    g = int(BRAND[1] * alpha + DARK[1] * (1 - alpha))
    b = int(BRAND[2] * alpha + DARK[2] * (1 - alpha))
    d.ellipse([-260 - i, -260 - i, -260 + i, -260 + i], fill=(r, g, b))

# Soft blue band under the baseline.
d.rectangle([0, H - 96, W, H], fill=(13, 22, 44))

f_logo = ImageFont.truetype(HELV_BOLD, 128)
f_tag = ImageFont.truetype(PINGFANG, 40)
f_dom = ImageFont.truetype(HELV, 32)

# "FUXI" wordmark.
word = "FUXI"
d.text((72, 150), word, font=f_logo, fill=WHITE)
# Accent underline.
d.rectangle([76, 290, 76 + d.textlength(word, font=f_logo) - 6, 298], fill=BRAND)

# Tagline.
d.text((78, 340), "The model is the engine.", font=f_tag, fill=SOFT)
d.text((78, 396), "FuXi is the vehicle.", font=f_tag, fill=WHITE)

# Domain.
d.text((W - 78 - d.textlength("fuxicode.com", font=f_dom), H - 70),
       "fuxicode.com", font=f_dom, fill=SOFT)

out = "/private/var/folders/z3/9wtwrkrx5b79h1zrvlqtk8z80000gn/T/fuxi-501/-Users-aivenue/1dbe5528-35de-47ab-ab2a-c328a1541024/scratchpad/fuxi-x/docs/social-preview.png"
img.save(out, "PNG")
print("saved", out)
