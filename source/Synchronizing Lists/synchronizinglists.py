while True:
    n = int(input())
    if n == 0:
        break
    
    list1 = [int(input()) for _ in range(n)]
    list2 = [int(input()) for _ in range(n)]
    
    # Create a dictionary to map elements from list1 to their indices
    index_map = {num: i for i, num in enumerate(list1)}
    
    # Reorder list2 based on the index map
    reordered_list2 = [list1[index_map[num]] for num in list2]
    
    # Print the reordered list2
    print(*reordered_list2)
    
    # Print a blank line between lists
    print()