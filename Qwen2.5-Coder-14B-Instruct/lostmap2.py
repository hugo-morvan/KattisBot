def count_coinciding_indices(n, m, map1, map2):
    def parse_map(map_data):
        result = []
        for line in map_data:
            parts = line.split()
            if len(parts) == 1 and parts[0] == "?":
                result.append((None, None))
            else:
                direction = parts[0][0]
                steps = int(parts[0][1:])
                result.append((direction, steps))
        return result

    map1_parsed = parse_map(map1)
    map2_parsed = parse_map(map2)

    def is_coinciding(index):
        for i in range(m):
            if (map1_parsed[index + i][0] != map2_parsed[i][0] and
                    map1_parsed[index + i][0] is not None and
                    map2_parsed[i][0] is not None) or \
               (map1_parsed[index + i][1] != map2_parsed[i][1] and
                    map1_parsed[index + i][1] is not None and
                    map2_parsed[i][1] is not None):
                return False
        return True

    count = 0
    for i in range(n - m + 1):
        if is_coinciding(i):
            count += 1

    return count

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
map1 = data[1:n+1]
map2 = data[n+1:]

# Output the result
print(count_coinciding_indices(n, m, map1, map2))
# Generator time: 44.9806 seconds