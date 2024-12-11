def is_point_in_rectangle(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

def is_point_in_circle(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

def count_hits(target_list, shot_x, shot_y):
    hit_count = 0
    for target in target_list:
        shape, *params = target.split()
        if shape == 'rectangle':
            x1, y1, x2, y2 = map(int, params)
            if is_point_in_rectangle(shot_x, shot_y, x1, y1, x2, y2):
                hit_count += 1
        elif shape == 'circle':
            cx, cy, r = map(int, params)
            if is_point_in_circle(shot_x, shot_y, cx, cy, r):
                hit_count += 1
    return hit_count

def main():
    m = int(input())
    targets = []
    for _ in range(m):
        target = input()
        targets.append(target)
    
    n = int(input())
    results = []
    for _ in range(n):
        shot_x, shot_y = map(int, input().split())
        result = count_hits(targets, shot_x, shot_y)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()