def compact_apaxian_name(name):
    # Initialize an empty list to store the compacted characters
    compacted = []
    
    # Iterate over the name
    for i in range(len(name)):
        # If it's the first character or the current character is different from the previous one, add it to the compacted list
        if i == 0 or name[i] != name[i - 1]:
            compacted.append(name[i])
    
    # Join the compacted list into a string and print it
    print(''.join(compacted))

# Read the input name
name = input()

# Call the function to compact the name
compact_apaxian_name(name)