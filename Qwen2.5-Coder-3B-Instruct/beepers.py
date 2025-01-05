import sys

def karel_path_length(scenarios):
    for _ in range(scenarios):
        x_size, y_size = map(int, input().split())
        start_x, start_y = map(int, input().split())
        num_beepers = int(input())
        beeper_positions = [tuple(map(int, input().split())) for _ in range(num_beepers)]
        
        total_distance = 0
        
        for beeper in beeper_positions:
            distance_to_beeper = abs(start_x - beeper[0]) + abs(start_y - beeper[1])
            distance_back = abs(beeper[0] - start_x) + abs(beeper[1] - start_y)
            total_distance += distance_to_beeper + distance_back
        
        print(total_distance)

if __name__ == "__main__":
    scenarios = int(sys.stdin.readline())
    karel_path_length(scenarios)
# Generator time: 9.6130 seconds