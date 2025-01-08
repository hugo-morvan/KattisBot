import math

def can_reach(A, B, R, l, w):
    def check(r):
        # Check if Alex can reach Bob with radius r
        # The circle's center must be at least r distance away from any obstacle
        # We need to check the clearance around the doors and walls
        
        # Door A clearance
        door_a_x1 = (l / 2) * math.cos(A)
        door_a_y1 = (l / 2) * math.sin(A)
        door_a_x2 = -door_a_x1
        door_a_y2 = -door_a_y1
        
        # Door B clearance
        door_b_x1 = w - (l / 2) * math.cos(B)
        door_b_y1 = (l / 2) * math.sin(B)
        door_b_x2 = w - door_b_x1
        door_b_y2 = -door_b_y1
        
        # Check clearance around the doors and walls
        clearances = [
            R + r - abs(door_a_x1),
            R + r - abs(door_a_x2),
            R + r - abs(door_b_x1),
            R + r - abs(door_b_x2)
        ]
        
        return min(clearances) > 0

    # Binary search for the largest r
    low, high = 0.0, R
    epsilon = 1e-5
    
    while high - low > epsilon:
        mid = (low + high) / 2
        if check(mid):
            low = mid
        else:
            high = mid
    
    return low

# Read input
R, l, w = map(int, input().split())
T = int(input())

for _ in range(T):
    A, B = map(float, input().split())
    result = can_reach(A, B, R, l, w)
    print(f"{result:.5f}")
# Generator time: 53.5187 seconds