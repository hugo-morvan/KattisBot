def assign_staff():
    n = int(input())
    staff_members = [input().strip() for _ in range(n)]
    
    # Find the relative's name to avoid
    relative_name = next(member for member in staff_members if "relative" in member)
    
    # Filter out relatives and shuffle the remaining members
    non_relatives = [member for member in staff_members if member != relative_name]
    
    import random
    random.shuffle(non_relatives)
    
    # Add the relative back at the end to ensure they do not get picked first
    non_relatives.append(relative_name)
    
    # Print the order of staff members
    for member in non_relatives:
        print(member)

# Call the function to execute the code
assign_staff()
# Generator time: 6.5663 seconds