 # define the initial position of pieces on the board
initial_position = [['.', '?', 'w', '.', '-', '-', '-', '.'], ['-', '-', 'b', '-', '-', '-', '-', '-' ], 
                    ['-', '-', '-', '-', '-', '-', '-', '-' ], ['-', '-', '-', '-', '-', '-', '-', '-' ], 
                    ['-', '-', '-', '-', '-', '-', '-', '-' ], ['?', '.', 'w', '.', 'b', 'b', 'b', '.'],  
                    ['.', '?', '?','.', 'B', 'W', 'W', '?' ]  ,['...']] # the last line is used to separate two boards in output format. It can be any random string of three dots '. .' for example)   
# define a function that takes input moves and returns updated positions after each move  
def update_position(initial,moves): 
        position = initial[:] # make copy so changes don’t affect the original list (not required if we want to modify this inplace but not asked here)    for m in range(len(moves)):         currentPosition= moves[m][0];jumpMovesListedAsXs  = [ele for ele in moves[m] if ele == 'x']        # get the simple move or jump list from a single line
        x_index,y_index=[],[]    
        if '-' not in currentPosition:            positionLetterIndex=currentPosition.find('-')  # find index of next empty square   (where we can place new piece)             for jm in range(len(jumpMovesListedAsXs)):                 x,y = jumpMovesListedAsXs[jm].split('x');                if '-' not in position[int(x)-1][positionLetterIndex]:  # check the square to be jumped is empty
                     y_index.append([j for j , ltrn in enumerate(jumpMovesListedAsXs)if int(ltrn)==y])   ; x_index.append(([i+7-int(x), i, positionLetterIndex]for  [positionLetterIndex],row1in zip ([ele - ord('a') for ele in ''.join([str(_).split('.')[0].replace('$', '')[-2:]] + [''] * (4 - len(['$'.join(_.split('-')) if _ != '.' else '' for _ in row1]) ))for  i,row1in enumerate(position)if '-' not in str(row1)] ,range(len(jumpMovesListedAsXs)))); x_index= [item[0] + item[-2:]  
                 if isinstance (item,-1): pass else:x_index.append([j for j,ltrn  in enumerate(['$'.join(_.split('-'))if _ != '.'else ''for _in position])+['']*4]);y_index= [i-7+(ord(jumpMovesListedAsXs[jm].replace('b', 'w').replace ('B' ,'W')[0])) 
                 if isinstance ( i, int) else y for jm in range len([ele.split('-')[-1]for ele _in position])+range(4);i-7+(ord(_))if '.'!=(_else '']*2)); x=x[y]; emptySquareIndex = [index 
                if isinstance ( index, int) else [] for i in range len([ele.split('-')[-1]for ele _in position])+range(4);i-7+(ord(_))if '.'!=(_else '']*2)][0][y].replace('b', 
                "w"). replace("B","W") for y in range len([ele.split('-')[-1]for ele _in position])+range(4);i-7+(ord(_))if '.'!=(_else '']*2)][0]; x=x[:index]+currentPosition [y].replace ('$', '') + 
                currentPostion[(position.index(".") if ".", else -1) or len([ele for ele in position])-1] ; y = max(emptySquareIndex); emptySquareLetter, index2=[chr(_)+str((_+7)-y),"".join(_.split('-')) 
                [0].replace('b', 'w'). replace("B","W") if isinstance ( _ , int) else '' for _,ele in enumerate(['$'. join([_. split ('-')[1]for elein position])if '.'!=(_else ""]*2));index=[(ord(chr(_)+str((_+7)-y)) 
                or -9)]+[i+(int(_.replace('b', 'w'). replace("B","W"))-(abs ( i- ord (_ )) if isinstance ( index, int) else None )or len([ele for ele in position]) *2 +1)];index= [jfor j,_ 
                ,ltrn _in zip ([i+7 -ord(chr(_)+str((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_else '']*4); i,row0 =enumerate (position) if isinstance (_[letter] else ord('a') + row [index]); index. append 
                ((j-1)*8+(i+7-(ord(ele)+int((_+6)-y))if '.'!=(_
# Generator time: 50.1592 seconds