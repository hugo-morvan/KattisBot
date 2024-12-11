def convert_vertical_to_horizontal():
    # Read the input
    input_lines = [input().strip() for _ in range(2)]
    
    # Split each line by '|' and concatenate them in reverse order
    horizontal_writing = ''.join(line.split('|')[::-1] for line in input_lines)
    
    # Print the result
    print(horizontal_writing)

# Call the function to process the input
convert_vertical_to_horizontal()