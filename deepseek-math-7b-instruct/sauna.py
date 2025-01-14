 def count_happy_temps(temp_ranges):
    # Create a set to store the available temps in millidegrees Celsius; initially it contains all integers from 1 to max of bi's (inclusive)
    happy_temps = {i for range in temp_ranges for i in range[0] + list(range(range[0]+1, range[1]))}    
    # If there are available temps then return the number and minimum; else "bad news" 
    if len(happy_temps) > 0:        
        min_temp = min(happy_temps)                
        count = len(happy_temps)            
    else:                        
        return 'bad news'    
    # Return number of temps and minimum temp which all people are happy with     
    return str(count)+','+str(min_temp)
# Generator time: 6.7257 seconds