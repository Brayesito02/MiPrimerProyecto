"""Convierte un PNG en Nine-Patch real (.9.png).
Uso: python make_ninepatch.py imagen.png fondo.9.png [x0 x1 y0 y1]
La zona FIJA (no se deforma) es el rectángulo x0..x1, y0..y1 (en píxeles).
Por defecto está ajustada al fondo del curso (marciano Android + nubes).
"""
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
x0, x1, y0, y1 = (map(int, sys.argv[3:7]) if len(sys.argv) >= 7 else (425, 630, 480, 730))
im = Image.open(src).convert("RGBA")
w, h = im.size
out = Image.new("RGBA", (w + 2, h + 2), (0, 0, 0, 0))
out.paste(im, (1, 1))
B = (0, 0, 0, 255)
for x in range(1, w + 1):           # borde superior = columnas estirables
    if x <= x0 or x > x1: out.putpixel((x, 0), B)
for y in range(1, h + 1):           # borde izquierdo = filas estirables
    if y <= y0 or y > y1: out.putpixel((0, y), B)
out.save(dst)
print("Listo:", dst, out.size)
