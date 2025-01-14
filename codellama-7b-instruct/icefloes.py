import math
from itertools import combinations, chain
def area(coords): #calculates the area of a polygon given its vertices as a list of coords
    return abs(sum(x*y for x, y in zip(coords[:-1], coords[1:])))/2.0

def is_in_polygon(point, polygon): #checks if the point is inside the polygon or not
    return (area([p for p in chain((point,), polygon)]) == area(polygon))
    
def find_safe_distance(distances): #finds the safe distance between two points given a list of distances
    return max([d for d in distances if d > dist])
    
def calculate_area(coords, scientist_positions, dist): #calculates the surface area of the smallest ice floe any of the scientists need to pass
    safe = []
    for i,j in combinations(range(len(scientist_positions)),2):
        if is_in_polygon(coords[i], scientist_positions[j]):
            return "Scientists cannot meet"
        else:
            safe.append((math.sqrt((coords[i][0]-scientist_positions[j][0])**2 + (coords[i][1]-scientist_positions[j][1])**2), coords[i]))
    safe = sorted(safe, key=lambda x:x[0]) #sorting the distances from small to large
    distances = [math.sqrt((coord[0]-scientist_positions[i][0])**2 + (coord[1]-scientist_positions[i][1])**2) for coord in coords] #calculating the distances between all the ice floes and a single scientist
    max_dist = max(distances) #the largest distance among all of them
    safe.append((max_dist, None)) #adding the maximum distance as one of the safest distances
    safe = sorted(safe, key=lambda x:x[0]) #sorting the distances from small to large
    smallest = min(coords) #the smallest ice floe
    largest = max(coords) #the largest ice floe
    while True:
        safe_dist = find_safe_distance(safe) #finding the safe distance between the two points
        if safe_dist > dist:
            return "Scientists cannot meet"
        elif area(smallest + largest) == 0.0: #if the two floes are the same size, then they can't be joined to form a smaller one
            return "Scientists cannot meet"
        else:
            smallest += largest #joining the two ice floes into one
            safe.remove((safe_dist, None)) #removing the distance of the largest ice floe
            

def main():
    t = int(input())
    for i in range(t):
        f = int(input())
        d = float(input()) #the maximum distance that the scientists are able to jump
        s1 = [int(x) for x in input().split()] #coordinates of the first scientist
        s2 = [int(x) for x in input().split()] #coordinates of the second scientist
        
        coords = [[[int(y) for y in x.split()] for x in input().split()]] #ice floe descriptions as a list of coordinates
        
        coords1 = [coord[0] + s1 for coord in coords] #the coordinates of the first scientist's ice floes
        coords2 = [coord[0] + s2 for coord in coords] #the coordinates of the second scientist's ice floes
        
        smallest_area = calculate_area(coords1, coords2, d)
        if smallest_area != "Scientists cannot meet":
            print("%.4f" % (smallest_area))
        else:
            print(smallest_area)
            
if __name__ == "__main__":
    main()

# Generator time: 22.9995 seconds