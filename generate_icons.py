#!/usr/bin/env python3
import io
import os
import cairosvg
from PIL import Image

SOURCE = "/Users/spooky/Spooky/Programming/Projects/Transaction_APP/public/logo.svg"
DEST   = "/Users/spooky/Spooky/Programming/Projects/Stack-Saver-mobile/app/src/main/res"

SIZES = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}

# Render SVG at largest size, then downscale for quality
MAX = 192
png_bytes = cairosvg.svg2png(url=SOURCE, output_width=MAX, output_height=MAX)
base = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

for folder, size in SIZES.items():
    out_dir = os.path.join(DEST, folder)
    os.makedirs(out_dir, exist_ok=True)
    resized = base.resize((size, size), Image.LANCZOS)
    resized.save(os.path.join(out_dir, "ic_launcher.webp"), "WEBP", quality=95)
    resized.save(os.path.join(out_dir, "ic_launcher_round.webp"), "WEBP", quality=95)
    print(f"  {folder}: {size}x{size}px ✓")

print("Done.")
