import math

def calculate_radius(volume):
    return math.sqrt(volume / math.pi)

def paint_canvas(paint_drops):
    canvas = {}
    
    for x, y, v, color in paint_drops:
        r = calculate_radius(v)
        for dx in range(-int(math.ceil(r)), int(math.floor(r)) + 1):
            for dy in range(-int(math.ceil(r)), int(math.floor(r)) + 1):
                if dx**2 + dy**2 <= r**2:
                    canvas[(x + dx, y + dy)] = color
    
    return canvas

def get_color(canvas, query_points):
    colors = []
    for x, y in query_points:
        if (x, y) in canvas:
            colors.append(canvas[(x, y)])
        else:
            colors.append("white")
    return colors

def main():
    c = int(input())
    
    results = []
    for _ in range(c):
        n = int(input())
        paint_drops = [tuple(map(float, input().split())) for _ in range(n)]
        
        m = int(input())
        query_points = [tuple(map(float, input().split())) for _ in range(m)]
        
        canvas = paint_canvas(paint_drops)
        colors = get_color(canvas, query_points)
        
        results.extend(colors)
    
    for color in results:
        print(color)

if __name__ == "__main__":
    main()
# Generator time: 9.6625 seconds