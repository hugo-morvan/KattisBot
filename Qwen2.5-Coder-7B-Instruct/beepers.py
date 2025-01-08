import sys

def find_min_distance(x_size, y_size, start_x, start_y, num_beeper, beeper_positions):
    def manhattan_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    total_distance = 0
    for i in range(num_beeper):
        for j in range(i + 1, num_beeper):
            distance = manhattan_distance(beeper_positions[i][0], beeper_positions[i][1],
                                           beeper_positions[j][0], beeper_positions[j][1])
            total_distance += distance

    # Distance from starting position to each beeper and back
    for i in range(num_beeper):
        distance_to_beeper = manhattan_distance(start_x, start_y, beeper_positions[i][0], beeper_positions[i][1])
        total_distance += 2 * distance_to_beeper

    return total_distance

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    results = []

    while index < len(data):
        num_scenarios = int(data[index])
        index += 1

        for _ in range(num_scenarios):
            x_size = int(data[index])
            y_size = int(data[index + 1])
            start_x = int(data[index + 2])
            start_y = int(data[index + 3])
            num_beeper = int(data[index + 4])
            beeper_positions = []

            for i in range(num_beeper):
                beeper_x = int(data[index + 5 + 2 * i])
                beeper_y = int(data[index + 6 + 2 * i])
                beeper_positions.append((beeper_x, beeper_y))
            
            index += 5 + num_beeper * 2

            result = find_min_distance(x_size, y_size, start_x, start_y, num_beeper, beeper_positions)
            results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 16.7316 seconds