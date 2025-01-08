def calculate_visible_area(buildings):
    def is_point_inside_polygon(x, y, poly):
        n = len(poly)
        inside = False
        p1x, p1y = poly[0]
        for i in range(1, n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def polygon_area(poly):
        n = len(poly)
        area = 0.5 * abs(sum(x * y for x, y in zip(poly, poly[1:] + poly[:1])) - sum(y * x for x, y in zip(poly[1:] + poly[:1], poly)))
        return area

    def trapezoid_area(base1, base2, height):
        return 0.5 * (base1 + base2) * height

    visible_areas = []
    for i in range(len(buildings)):
        building = buildings[i]
        x1, y1, x2, y2 = building
        trapezoid_height = y2 - y1
        trapezoid_base1 = x2 - x1
        polygon = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        
        visible_area = 0
        for j in range(len(buildings)):
            if i != j:
                other_building = buildings[j]
                other_x1, other_y1, other_x2, other_y2 = other_building
                if is_point_inside_polygon(x1, y1, polygon) or is_point_inside_polygon(x2, y1, polygon):
                    visible_area += trapezoid_area(0, 0, trapezoid_height)
                elif is_point_inside_polygon(other_x1, other_y1, polygon) or is_point_inside_polygon(other_x2, other_y1, polygon):
                    intersection_points = []
                    if x1 == other_x1:
                        intersection_points.append((x1, y1))
                    if x1 == other_x2:
                        intersection_points.append((x1, y2))
                    if x2 == other_x1:
                        intersection_points.append((x2, y1))
                    if x2 == other_x2:
                        intersection_points.append((x2, y2))
                    
                    if len(intersection_points) == 4:
                        visible_area += trapezoid_area(0, 0, trapezoid_height)
                    elif len(intersection_points) == 3:
                        x1, y1 = intersection_points[0]
                        x2, y2 = intersection_points[1]
                        x3, y3 = intersection_points[2]
                        if (x1 != x2 and x1 != x3 and x2 != x3):
                            visible_area += trapezoid_area(0, 0, trapezoid_height)
                    elif len(intersection_points) == 2:
                        x1, y1 = intersection_points[0]
                        x2, y2 = intersection_points[1]
                        if (x1 != x2):
                            visible_area += trapezoid_area(0, 0, trapezoid_height)
        
        relative_visible_area = max(visible_area / trapezoid_area(trapezoid_base1, 0, trapezoid_height), 0)
        visible_areas.append(relative_visible_area)

    return visible_areas

def main():
    N = int(input())
    buildings = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        buildings.append((x1, y1, x2, y2))
    
    visible_areas = calculate_visible_area(buildings)
    for area in visible_areas:
        print(f"{area:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 24.5904 seconds