def find_safe(positions):
    # We can't place a queen in a square that is already occupied. 
    # Therefore, we need to make sure that each new position does not 
    # collide with any existing positions. We will check the row, column, and diagonal of each new position. 
    
    safe_positions = [] 
    for i in range(len(positions)): 
        x, y = positions[i]
        
        # Check if current position is valid by iterating through all other queens  
        valid = True
        for j in range(len(positions)): 
            if i != j:
                x2, y2 = positions[j]
                if (x == x2) or (y == y2):
                    # Collision detected! Set to False. 
                    valid = False
                    break
        if valid:
            safe_positions.append((x, y))
    
    return len(safe_positions)
# Generator time: 7.1714 seconds