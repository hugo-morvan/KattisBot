 def pascals_row(n):
    if n == 0:
        return [1]
    row = pascals_row(n - 1)
    next_row = [x + y for x, y in zip([0]+row, row+[0])]
    return next_row
def count():    
	count=0   #initialize counter variable to keep track of number multiples with k     
	for i in range(10**3): 	#iterate through the possible values for N (from given constraints)                if ((i%K)==0 ):         		        	    	    j = pascals_row[int](i)[j]       #accessing value of pascal row using index    
				if((pascalsRow( i ) [ int ]  % K ==  0 )):   	count +=1     	return count
# Generator time: 6.7281 seconds