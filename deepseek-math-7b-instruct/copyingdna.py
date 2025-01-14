 def min_copies(s, t):
    s = list(reversed(list(s))) # reverse string so we can append and pop without having any issues with the indexes in O (1) time complexity as per requirement 2 &3 mentioned above . Also it will save a lot of space for large inputs.  
    t_copy=[]    
    count =0      
    while(len(t)!= len(s)): # loop until the length becomes equal to T's i/e we have copied all characters in required order and number 4 mentioned above .         for letter in reversed (list(t)) :   # iterate through each character of t from last index onwards as per requirement1            if s:              
                  c = s.pop()         
                  count+=1            
                  while True :                    
                    try:                        
                      b= letter <c  and (letter in ['A','C'] or not(s[-2:]==['G', 'T'])) # check the conditions mentioned above ,if all are true then break out of loop to copy . else pop last element from s.                    
                    except :                        
                      b=False            
                  if (b and letter in ['A','C']):# when we got a match push that character into t_copy as per requirement 2 mentioned above ,also increment count by one for the copy operation .                            
                        s.append(c)                    
                        c =t[len(t)-1]                      
                        letter=letter[:-1] # remove last element from T after matching so that we can check next character of t without any issues and also follow requirement 3 mentioned above for saving space .                     
                        count+=1;                    
                  elif not b:                   s.pop()           else :   break      if letter == '':    # when all characters are matched then comes this condition to pop out from while loop as per line number no -26 of python documentation i/e "The statements for and while will never reach the end if the condition is always false". 
                  t_copy.append(c)   break       return count        else:            print("impossible")
# Generator time: 12.6046 seconds