import math

def main():
    W = float(input())
    
    # Time for Agneta to reach a point on her slide
    t_A = W
    
    # Angle that Agneta has traveled by time t_A
    angle_A = t_A * 1
    
    # Position of Agneta at time t_A
    x_A = (math.cos(angle_A) - 1)
    y_A = math.sin(angle_A)
    
    # Time for Beata to reach a point on her slide, starting W seconds after Agneta
    t_B = 0
    
    # Angle that Beata has traveled by time t_B
    angle_B = t_B * 1
    
    # Position of Beata at time t_B
    x_B = (math.cos(angle_B) - 1 + math.cos(2))
    y_B = math.sin(angle_B) + math.sin(2)
    
    # Calculate the Euclidean distance between Agneta and Beata
    distance = math.sqrt((x_A - x_B)**2 + (y_A - y_B)**2)
    
    print(distance)

if __name__ == "__main__":
    main()
# Generator time: 8.3071 seconds