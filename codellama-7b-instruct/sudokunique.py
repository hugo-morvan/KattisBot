import sys
def getBoard():
    board=[]
    i=0
    while True:
        line=input()
        if line=='':break
        board.append([int(x) for x in line])
    return board
def solveSudoku(board,row,col):
    rowList=[1,2,3,4,5,6,7,8,9]
    colList=[1,2,3,4,5,6,7,8,9]
    if (row==9)and(col==9):return True
    for i in range(9):
        if board[row][i]!=0:
            rowList.remove(board[row][i])
            colList.remove(board[row][i])
    for i in range(9):
        if board[i][col]!=0:
            rowList.remove(board[i][col])
            colList.remove(board[i][col])
    box=(3*(row//3))+col//3
    for i in range(box,box+3):
        for j in range(box,box+3):
            if (i!=row)and(j!=col)and(board[i][j]!=0):
                rowList.remove(board[i][j])
                colList.remove(board[i][j])
    if len(rowList)==1:
        board[row][col]=rowList[0]
        return solveSudoku(board,row+1,col)
    elif len(colList)==1:
        board[row][col]=colList[0]
        return solveSudoku(board,row,col+1)
    else:
        for i in rowList:
            if (i not in colList)and(board[row][col-1]!=i)and(board[row][col+1]!=i):
                board[row][col]=i
                solveSudoku(board,row,col+1)
        for j in colList:
            if (j not in rowList)and(board[row-1][col]!=j)and(board[row+1][col]!=j):
                board[row][col]=j
                solveSudoku(board,row,col+1)
        return False
def main():
    n=int(input())
    for i in range(n):
        board=getBoard()
        if solveSudoku(board,0,0):
            print(*["".join([str(x)for x in row]) for row in board])
        else:print("Non-unique")
if __name__=="__main__":main()
# Generator time: 15.7501 seconds