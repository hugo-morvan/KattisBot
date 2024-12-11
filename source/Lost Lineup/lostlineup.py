def find_lineup(n, distances):
    # Initialize the lineup with Jimmy as the first person
    lineup = [1]
    
    # Iterate over the distances and determine the positions of the other people
    for distance in distances:
        # Find the position where the next person should be placed
        position = lineup[-1] + distance + 1
        lineup.append(position)
    
    # Print the lineup
    print(" ".join(map(str, lineup)))

# Read input
n = int(input())
distances = list(map(int, input().split()))

# Find and print the lineup
find_lineup(n, distances)