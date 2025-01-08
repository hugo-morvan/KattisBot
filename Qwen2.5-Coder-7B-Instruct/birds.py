def max_additional_birds():
    # Read input values
    input_data = input().split()
    l = int(input_data[0])
    d = int(input_data[1])
    n = int(input_data[2])

    # Read positions of the birds already sitting on the wire
    bird_positions = [int(input()) for _ in range(n)]
    
    # Sort the bird positions to facilitate calculation
    bird_positions.sort()
    
    # Initialize variables to keep track of additional birds that can sit
    additional_birds = 0
    
    # Check how many birds can sit between existing birds
    for i in range(1, n):
        if (bird_positions[i] - bird_positions[i-1]) > d:
            additional_birds += (bird_positions[i] - bird_positions[i-1]) // d - 1
    
    # Check the space before the first bird
    if bird_positions[0] > 6:
        additional_birds += (bird_positions[0] - 6) // d
    
    # Check the space after the last bird
    if l - bird_positions[-1] > 6:
        additional_birds += (l - bird_positions[-1] - 6) // d
    
    # Output the result
    print(additional_birds)

# Call the function to execute
max_additional_birds()
# Generator time: 9.3076 seconds