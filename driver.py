import sys
from tokped import ScrapperTokopedia

inp = sys.argv
if(len(inp) == 2):
    url = inp[1]
    bl = ScrapperTokopedia(url)
    bl.getPrice()
else:
    print("Harap masukkan link produk")