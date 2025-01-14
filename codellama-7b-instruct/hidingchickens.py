def min_distance(roost, hiding_spots):
    # Calculate the distance between roost and every hiding spot.
    distances = [((x - roost[0]) ** 2 + (y - roost[1]) ** 2) ** 0.5 for x, y in hiding_spots]
    # Get the minimum distance.
    return min(distances)
# Generator time: 4.5199 seconds