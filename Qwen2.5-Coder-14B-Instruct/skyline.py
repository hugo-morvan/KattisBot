import sys

def calculate_visible_area(buildings):
    n = len(buildings)
    visible_areas = [1.0] * n
    
    for i in range(n):
        x1, y1, x2, y2 = buildings[i]
        height = y2 - y1
        
        for j in range(i + 1, n):
            x3, y3, x4, y4 = buildings[j]
            if x3 >= x2:
                break
            
            # Calculate the overlapping width
            overlap_width = min(x2, x4) - max(x1, x3)
            
            # Calculate the visible height of building i from j
            visible_height = max(0, min(y1 + (x3 - x1) * (y2 - y1) / (x2 - x1), y2) - y3)
            
            # Update the visible area for building i
            visible_areas[i] -= overlap_width * visible_height / height
    
    return visible_areas

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    buildings = []
    index = 1
    
    for _ in range(n):
        x1 = int(data[index])
        y1 = int(data[index + 1])
        x2 = int(data[index + 2])
        y2 = int(data[index + 3])
        buildings.append((x1, y1, x2, y2))
        index += 4
    
    visible_areas = calculate_visible_area(buildings)
    
    for area in visible_areas:
        print(f"{area:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 46.1446 seconds