 ```python
def solve(input): # pylint: disable=invalid-name, missing-docstring, too-many-locals
    rules = [tuple((s1 + s2).split('+') for s1, _, s2 in rule.strip().replace('-', ' ->').split('\n')) 
             for rule in input[:-1]] # split by newlines and tabs; remove whitespaces around "->" symbol (it'll be replaced with '+'); convert to tuple of lists containing colours strings  
    T = int(input[-2])                                                                      # number of test cases    
    tests_cases  = [[int(C)] + [[(k, float(cer)) for k, cer in line.strip().split('\n')[:-1].split('END')]  # split by newlines and tabs; remove whitespaces before "END" (it'll be removed) symbol
                     for _ in range(int(C))]  
                   for C in input[1:-2:T+1]]                                                # the first element is number of tokens, next elements are sequences 
    results = []                                                                            # empty list to store final answers    
    
    def get_possible():                                                              # function that returns a set with all possible colours after combining two given ones (accordingly rules)  
        possbile_colours=set()                                                       # create an empty container for the result 
        
        if col1 in rule[0] and col2 in rule[1]:                                      # check whether both inputed tokens are among first pair of colours from some combination: return True/False accordingly  
            possbile_colours.add(rule[2][list(rule[0]).index(col1)] + 
                                rule[2][list(rule[1]).index(col2)])                    # if so, add the corresponding colour to result set (accordingly combination's third column)  
        return possbile_colours                                                       # function returns its container with possible colours as a solution     
    
    for test in tests_cases:                                                           # iterate through all sequences from input data 
         sequence = [tuple(get_possible().pop())                                    # get the first colour (from rule's third column) that can be obtained by combining two given ones  
                 if len(get_possible()) !=0 else 'GAMEOVER']                      # return GAMEOVER in case there are no more possible colours to combine 
         while sequence:                                                             # iterate until all tokens have been combined (or game is over, of course)   
            cer = sum((sequence[i][1]*input2[j]) for i, input2 in enumerate(tests_cases[-len(rules):]))/sum([cer*rule3 
                                                                                                    if rule else 'GAMEOVER'   # calculate certainty by multiplying all tokens certainties and dividing on total one (all rules) or GAMEOVER otherwise   
                     for j, sequence1 in enumerate((sequence[:-2] + [('END', )]))                            # split the result into two parts: first is a list of colours without 'END' element; second just contains it  
                         if any(col.lower() == rule[0][i].lower().strip(', ') for i, col in enumerate([sequence1[-2]] + sequence[:-3] ))])  # check whether some token (from the first part of result) can be combined with 'END' one from next step  
            if cer > sum(cer*rule[0][i].lower() == rule for i, col in enumerate([sequence1[-2]] + sequence[:-3])): break  # check whether some token (from the first part of result) can be combined with 'END' one from next step and return it if so  
            cer = max(cer*rule[0][i].lower() == rule for i, col in enumerate([sequence1[-2]] + sequence[:-3]))  # get maximum certainty among all possible combinations (if there is any) to continue the game   
            
# Generator time: 21.4849 seconds