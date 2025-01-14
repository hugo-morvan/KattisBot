if __name__ == "__main__":
    # Number of painting descriptions
    c = int(input())
    
    # Painting description loop
    for i in range(c):
        # Number of paint drops
        n = int(input())
        
        # Create a 2D list to hold the canvas
        canvas = [["W"] * 100 for _ in range(100)]
        
        # Paint drop loop
        for j in range(n):
            # Get input values for paint drop
            x, y, v = map(float, input().split())
            
            # Set radius and diameter of the circle
            r = math.sqrt(v / math.pi)
            d = 2 * r
            
            # Check if the paint drop is inside the canvas bounds
            if x > -1 and y > -1 and x < 100 and y < 100:
                # Calculate center of circle
                cx = int(x)
                cy = int(y)
                
                # Calculate start and end indices for the circle
                start_x = max(cx - d, 0)
                start_y = max(cy - d, 0)
                end_x = min(cx + d, 100)
                end_y = min(cy + d, 100)
                
                # Iterate through all indices within the circle
                for i in range(start_x, end_x):
                    for j in range(start_y, end_y):
                        # Check if index is inside the circle
                        if (i - cx)**2 + (j - cy)**2 <= r**2:
                            canvas[i][j] = input().split()[0]
        
        # Number of queries
        m = int(input())
        
        # Query loop
        for k in range(m):
            # Get query values
            x, y = map(float, input().split())
            
            if canvas[int(x)][int(y)] == "W":
                print("white")
            else:
                print(canvas[int(x)][int(y)])
# Generator time: 13.0354 seconds