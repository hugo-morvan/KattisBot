from collections import deque

def main():
    m, n = map(int, input().split())
    map1 = [input().strip() for _ in range(n)]
    map2 = [input().strip() for _ in range(m)]

    # Initialize a queue to process the maps
    queue = deque([(0, 0)])  # (index in map1, index in map2)
    visited = set((0, 0))  # Set to keep track of visited indices

    while queue:
        i, j = queue.popleft()

        # If both maps have reached the end, all maps coincide
        if i == n and j == m:
            break

        # Check if the current indices are valid
        if i < n and j < m and (i, j) not in visited:
            visited.add((i, j))

            # Check if the current instructions match or are both "?"
            if map1[i] == map2[j] or (map1[i][0] == "?" or map2[j][0] == "?"):
                # Move to the next instruction in map1
                if i + 1 < n:
                    queue.append((i + 1, j))
                # Move to the next instruction in map2
                if j + 1 < m:
                    queue.append((i, j + 1))

    # The number of indices where the maps coincide is the size of the visited set
    print(len(visited))

if __name__ == "__main__":
    main()
# Generator time: 15.8351 seconds