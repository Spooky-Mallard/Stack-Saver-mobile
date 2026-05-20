#!/usr/bin/env python3
from PIL import Image
import os

SOURCE = "/Users/spooky/Spooky/Programming/Projects/Transaction_APP/public/S.png"
DEST   = "/Users/spooky/Spooky/Programming/Projects/Stack-Saver-mobile/app/src/main/res"

SIZES = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}

img = Image.open(SOURCE).convert("RGBA")
w, h = img.size  # 400 x 500

# Center-crop to square
top    = (h - w) // 2
bottom = top + w
img = img.crop((0, top, w, bottom))

for folder, size in SIZES.items():
    out_dir = os.path.join(DEST, folder)
    os.makedirs(out_dir, exist_ok=True)
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(os.path.join(out_dir, "ic_launcher.webp"), "WEBP", quality=95)
    resized.save(os.path.join(out_dir, "ic_launcher_round.webp"), "WEBP", quality=95)
    print(f"  {folder}: {size}x{size}px ✓")

print("Done.")
