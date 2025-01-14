 ```python
def emoticon_to_emoji(text):
    # Define a dictionary to map each emoticon/expression to its corresponding emoji representation (empty string if not found)
    mappings = {":-)":"", ":-(":"", ";-)":"", "xD":""}  # Add more mapping as required, but keep the order consistent with other solutions too!
    
    min_length= len(text)   # Initialize minimum and maximum length to be equal to text's current (unmodified/original by Emma) size. This will get updated if we find a shorter or longer string after emoticons are replaced wth their emoji equivalents, respectively  - see below
    max_length = len(text)   # Initialize minimum and maximum length with the same value as per above explanation for min_value    
     
    current=0; previous=-1       # initialize counters. These will be used to track where we are in mapping, if any (to avoid going beyond text's valid range), or when a space character is encountered - see below  
 
    while(current<len(text)):       
            for i in mappings:         
                # If the current sequence of characters matches an emoticon/expression, replace it with its corresponding emoji representation. Also track where we are so as to avoid going beyond text's valid range - see above explanations around 'previous', and note how this is done below  (also notice that since these mappings have been sorted in increasing length order by their keys i-e the emoticons/expressions, it would skip any longer matches if a shorter one has already replaced some characters)  
                # Also ensure we do not replace spaces or other such special chars with empty string - see below for handling of them   
                
                pos=text.find(i,previous+1); previous=pos 
                while (current<len(text)-2 and text[current:current+3]== i):   # check that we are not going beyond valid range - see above explanations around 'previous'     
                    current+= len(i)                               
                    if pos!=-1 : min_length-=  (pos-(len(text)-2))    ; max_length -=3     else: break                        # update counters accordingly   text = text[:current] + mappings[ i ]+ text[current:]          current+= len(mappings[i])       
            if ''.join(sorted([x for x in set('!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') &set(text)])) =='': break  # If all characters are of the same type (say, punctuation), there will be no emoticon/expression to replace. In this case just return original text size as it is minimum and maximum possible lengths  
    if ''.join(sorted([x for x in set('!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') &set(text)])) =='!': min_length = 0; max_length= len ( text )-1 # If all characters are of the same type and punctuation, then there is no way to replace any character with another one. In this case return a pair where minimum length could be zero if it's possible for an empty string i e : '!' or maximum otherwise  
    else: min_length = 0; max_length= len ( text )-1 # If all characters are of the same type but not punctuation, then there is some way to replace a character with another one. In this case return minimum zero and length -2 as it's always possible for at least '!' or an empty string respectively 
    if min_length == max_length: print(int((min_value+max_value)/2)); else :print(' '.join([str(i)for i in [min_length, max_length]])) # If minimum and maximum lengths are equal just return their average as integer otherwise 
    if min_length ==0 or len ( text )-1: print("invalid input")
# Generator time: 21.7696 seconds