import math

def main():
    c = int(input())
    
    for _ in range(c):
        n = int(input())
        drops = []
        
        for _ in range(n):
            X, Y, V, color = input().split()
            X = float(X)
            Y = float(Y)
            V = float(V)
            r = math.sqrt(V / math.pi)
            drops.append((X, Y, r, color))
        
        m = int(input())
        queries = [tuple(map(float, input().split())) for _ in range(m)]
        
        results = []
        
        for qx, qy in queries:
            found_color = None
            for dx, dy, dr, dcolor in reversed(drops):
                if math.sqrt((qx - dx) ** 2 + (qy - dy) ** 2) <= dr:
                    found_color = dcolor
                    break
            results.append(found_color)
        
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
# Generator time: 29.7997 seconds