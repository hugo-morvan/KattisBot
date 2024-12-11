def min_pencil_crayons_to_remove(N, K):
    # Read the input
    boxes = [input().split() for _ in range(N)]
    
    # Create a dictionary to count occurrences of each color
    color_count = {}
    for box in boxes:
        for color in box:
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
    
    # Calculate the minimum number of crayons to remove
    total_colors_needed = N * K
    colors_with_more_than_one = sum(1 for count in color_count.values() if count > 1)
    min_crayons_to_remove = total_colors_needed - colors_with_more_than_one
    
    print(min_crayons_to_remove)

# Read the number of test cases
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    min_pencil_crayons_to_remove(N, K)