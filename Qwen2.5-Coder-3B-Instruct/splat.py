import math

def get_color(x, y, color):
    # Return the color as a string
    return color

def drop_paint(canvas, x, y, v):
    # Calculate the radius of the paint drop
    r = math.sqrt(v / math.pi)
    
    # Determine the range of points to update
    min_x = max(0, x - r)
    max_x = min(1000, x + r)
    min_y = max(0, y - r)
    max_y = min(1000, y + r)
    
    # Update the canvas with the new color
    for i in range(int(min_x), int(max_x) + 1):
        for j in range(int(min_y), int(max_y) + 1):
            if math.sqrt((i - x)**2 + (j - y)**2) <= r:
                canvas[i][j] = get_color(x, y, color)

def process_painting(painting):
    canvas = [['' for _ in range(1001)] for _ in range(1001)]
    
    for _ in range(painting['n']):
        x, y, v, color = map(float, input().split())
        drop_paint(canvas, x, y, v)
    
    return canvas

def process_queries(canvas, queries):
    results = []
    for x, y in queries:
        results.append(canvas[int(x)][int(y)])
    return results

def main():
    c = int(input())
    paintings = []
    
    for _ in range(c):
        n = int(input())
        painting = {
            'n': n,
            'drops': []
        }
        
        for _ in range(n):
            x, y, v, color = map(float, input().split())
            painting['drops'].append((x, y, v, color))
        
        paintings.append(painting)
    
    m = int(input())
    queries = []
    
    for _ in range(m):
        x, y = map(float, input().split())
        queries.append((x, y))
    
    for painting in paintings:
        canvas = process_painting(painting)
        results = process_queries(canvas, queries)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
# Generator time: 32.2786 seconds