import math

def calculate_angle(x, y):
    # Calculate the angle in radians
    angle = math.atan2(y, x)
    # Convert to degrees for easier comparison
    angle_degrees = math.degrees(angle)
    return angle_degrees

def main():
    n, m = map(int, input().split())
    
    # Read citizen coordinates
    citizens = []
    for _ in range(n):
        x, y = map(int, input().split())
        citizens.append((x, y))
    
    # Read train line information
    train_lines = []
    for _ in range(m):
        x, y, c = map(int, input().split())
        train_lines.append((x, y, c))
    
    # Calculate angles for each citizen
    angles = [(calculate_angle(x, y), i) for i, (x, y) in enumerate(citizens)]
    
    # Sort citizens by angle, then by x-coordinate
    angles.sort()
    
    # Initialize variables to track assigned citizens and train capacities
    assigned = set()
    train_assignments = [-1] * n
    
    for angle, i in angles:
        for j, (tx, ty, capacity) in enumerate(train_lines):
            if j not in assigned and capacity > 0:
                # Check if the current train line is the best fit
                if train_assignments[i] == -1 or abs(calculate_angle(tx, ty) - angle) < abs(calculate_angle(tx, ty) - train_assignments[i]):
                    train_assignments[i] = j
                    assigned.add(j)
                    capacity -= 1
                    break
    
    # Output the result
    print(len(assigned))
    for i, line in enumerate(train_assignments):
        if line != -1:
            print(i, line)

if __name__ == "__main__":
    main()
# Generator time: 30.3789 seconds