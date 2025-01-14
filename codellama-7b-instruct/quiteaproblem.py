def solve(input_string):
    words = input_string.split()
    
    for word in words:
        if word.lower().find('problem') != -1 or \
           word.upper().find('PROBLEM') != -1:
            return 'yes'
        
    return 'no'
# Generator time: 9.9913 seconds