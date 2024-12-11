def merge_lists(ann_list, ben_list):
    # Merge the two lists while maintaining alphabetical order
    merged_list = sorted(ann_list + ben_list)
    return ''.join(merged_list)

# Read input lists
ann_list = input()
ben_list = input()

# Merge the lists and print the result
result = merge_lists(ann_list, ben_list)
print(result)