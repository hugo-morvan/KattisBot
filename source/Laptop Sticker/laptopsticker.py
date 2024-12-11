# Read input values
wc, hc, ws, hs = map(int, input().split())

# Check if the sticker fits with one centimeter space on all sides
if wc >= ws + 2 and hc >= hs + 2:
    print(1)
else:
    print(0)