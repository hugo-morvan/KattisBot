def find_strengths(n):
    # Initialize a list to store the estimated strengths
    strengths = [0] * n
    
    # Step 1: Find the maximum strength
    for i in range(1, n):
        print(f"? {i} {n}")
        response = int(input())
        strengths[i-1] = response
    max_strength = max(strengths)
    
    # Step 2: Determine the second maximum strength
    second_max_strength = -1
    for i in range(n-1):
        if strengths[i] != max_strength:
            if second_max_strength == -1 or strengths[i] > second_max_strength:
                second_max_strength = strengths[i]
    
    # Step 3: Adjust the estimates
    for i in range(n-1):
        if strengths[i] != max_strength and strengths[i] != second_max_strength:
            print(f"? {i+1} {n}")
            response = int(input())
            if response > strengths[i]:
                strengths[i] = response
    
    # Step 4: Print the final estimates
    estimated_strengths = [second_max_strength if x == max_strength else x for x in strengths]
    print("!" + " ".join(map(str, estimated_strengths)))

# Read input
n = int(input())
find_strengths(n)
# Generator time: 38.8909 seconds