def max_pyramid_height(blocks):
    height = 0
    while True:
        blocks -= (height + 1) ** 2
        if blocks < 0:
            break
        height += 1
    return height

# Read input
blocks = int(input())

# Compute and print the maximum pyramid height
print(max_pyramid_height(blocks))