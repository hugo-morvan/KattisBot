from itertools import combinations

def min_distance(roost, spots):
    roost_x, roost_y = roost
    total_distance = 0
    
    for spot in spots:
        spot_x, spot_y = spot
        total_distance += abs(spot_x - roost_x) + abs(spot_y - roost_y)
    
    return total_distance

def main():
    # Input reading
    roost_input = input().split()
    roost_x = float(roost_input[0])
    roost_y = float(roost_input[1])
    
    n = int(input())
    spots = []
    for _ in range(n):
        spot_input = input().split()
        spot_x = float(spot_input[0])
        spot_y = float(spot_input[1])
        spots.append((spot_x, spot_y))
    
    # Calculate minimum distance
    min_dist = min_distance(roost, spots)
    print(min_dist)

if __name__ == "__main__":
    main()
# Generator time: 8.5868 seconds