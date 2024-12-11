def min_parking_distance(test_cases):
    for _ in range(test_cases):
        n = int(input())
        store_positions = list(map(int, input().split()))
        
        # Sort the store positions to find the median
        store_positions.sort()
        
        # The optimal parking spot is the median of the store positions
        optimal_parking = store_positions[n // 2]
        
        # Calculate the total distance Michael must walk
        total_distance = sum(abs(optimal_parking - pos) for pos in store_positions)
        
        print(total_distance)

# Read the number of test cases
test_cases = int(input())
min_parking_distance(test_cases)