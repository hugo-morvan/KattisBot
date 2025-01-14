T = int(input())
for i in range(T):
    N = int(input())
    strng = input()
    strng_reversed = strng[::-1]
    
    if N == 0:
        print(strng)
        
    else:
        counter = 0
        for j in range(len(strng)):
            if strng[j].isupper():
                if (counter+N) > 25:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr((counter+N)-26))
                else:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr(counter+N))
                strng_reversed = temp_val.join(strng_reversed)
            elif strng[j].islower():
                if (counter+N) > 25:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr((counter+N)-26))
                else:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr(counter+N))
                strng_reversed = temp_val.join(strng_reversed)
            elif strng[j] == '_':
                if (counter+N) > 25:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr((counter+N)-26))
                else:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr(counter+N))
                strng_reversed = temp_val.join(strng_reversed)
            elif strng[j] == '.':
                if (counter+N) > 25:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr((counter+N)-26))
                else:
                    temp_val = strng[j] + ''.join(chr(ord(x)+13) for x in chr(counter+N))
                strng_reversed = temp_val.join(strng_reversed)
            counter += 1
        print(strng_reversed)
# Generator time: 14.7895 seconds