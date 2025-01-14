def solve(spots):
    # Find min and max x and y values in array
    min_x = min([coord[0] for coord in spots])
    max_x = max([coord[0] for coord in spots])
    min_y = min([coord[1] for coord in spots])
    max_y = max([coord[1] for coord in spots])
    
    # Find midpoint of bounding box
    mid_x = (max_x + min_x) / 2.0
    mid_y = (max_y + min_y) / 2.0
    
    # Calculate distance from each spot to midpoint
    distances = [(coord[0] - mid_x) ** 2 + (coord[1] - mid_y) ** 2 for coord in spots]
    
    return min([distance for distance in distances if distance > 0.0])
# Generator time: 20.2704 seconds