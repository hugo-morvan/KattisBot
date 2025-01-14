 import re
pattern = 'problem'
while True:
    try:
        text_line=input()        
        x = str(re.search('{}'.format(pattern),str(text_line)))      
        if (x):            
            print("yes")                
        else:                 
          print("no")    
    except EOFError:   #end of file reached 
      break
# Generator time: 4.3725 seconds