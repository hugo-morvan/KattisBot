import itertools

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_min_path(x_size, y_size, start, beepers):
    total_distance = 0
    for perm in itertools.permutations(beepers):
        current_position = start
        for beeper in perm:
            total_distance += manhattan_distance(current_position, beeper)
            current_position = beeper
        total_distance += manhattan_distance(current_position, start)
    return min(total_distance)

def main():
    scenarios = int(input())
    results = []
    
    for _ in range(scenarios):
        x_size, y_size = map(int, input().split())
        start_x, start_y = map(int, input().split())
        num_beepers = int(input())
        beepers = [tuple(map(int, input().split())) for _ in range(num_beepers)]
        
        min_path_length = calculate_min_path(x_size, y_size, (start_x, start_y), beepers)
        results.append(min_path_length)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 35.3915 seconds