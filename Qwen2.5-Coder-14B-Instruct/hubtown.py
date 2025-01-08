import sys

def main():
    import sys
    import math
    import bisect
    
    def angle(x, y):
        return math.atan2(y, x)
    
    n, m = map(int, input().split())
    
    citizens = []
    for i in range(n):
        x, y = map(int, input().split())
        citizens.append((x, y))
    
    trains = []
    for i in range(m):
        x, y, c = map(int, input().split())
        a = angle(x, y)
        trains.append((a, c))
    
    # Sort the citizens by their angular distance from the origin
    citizens.sort(key=lambda p: (angle(p[0], p[1]), p[0], p[1]))
    
    # Sort the trains by their angles
    trains.sort()
    
    # Initialize the available capacities of each train line
    available_capacities = [c for _, c in trains]
    
    # Priority queue to keep track of citizens that can go by train
    import heapq
    pq = []
    
    # Iterate over each citizen and determine their closest train line
    for i, (x, y) in enumerate(citizens):
        a = angle(x, y)
        
        # Find the range of train lines that are closest to this citizen
        left = bisect.bisect_left(trains, (a, 0))
        right = bisect.bisect_right(trains, (a, float('inf')))
        
        found = False
        
        # Check if the leftmost or rightmost train line is available
        if left < m and available_capacities[left] > 0:
            heapq.heappush(pq, (-1, i, left))
            found = True
        elif right > 0 and available_capacities[right-1] > 0:
            heapq.heappush(pq, (-1, i, right-1))
            found = True
        
        # If no train line is available, check the middle train lines
        if not found:
            for j in range(left, min(right, m)):
                if available_capacities[j] > 0:
                    heapq.heappush(pq, (-1, i, j))
                    break
    
    # Now we need to assign the citizens to the trains using a greedy approach
    assigned_citizens = []
    
    while pq:
        _, i, j = heapq.heappop(pq)
        
        if available_capacities[j] > 0:
            assigned_citizens.append((i, j))
            available_capacities[j] -= 1
    
    # Output the result
    print(len(assigned_citizens))
    for i, j in assigned_citizens:
        print(i, j)

if __name__ == "__main__":
    main()
# Generator time: 76.4663 seconds