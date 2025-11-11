#N QUEENS PROBLEMS

#To print the board 
#board taken as input is a 2d list
def printboard(board): 
    for row in board:
        print(" ".join(row))
    print()

def isSafe(board,row,col,n):
    #check in the above location if queen is present
    for i in range(row):
        if board[i][col]=="Q":
            return False
        
    #check in the left upper diagonal portion
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if board[i][j]=="Q":
            return False
        
    for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
        if board[i][j]=="Q":
            return False
    return True

def SolveNQueens(board,row,n):
    if row==n:
        printboard(board)
        return()
    for col in range(n):
        if isSafe(board,row,col,n):
            board[row][col]="Q"
            SolveNQueens(board,row+1,n)
            board[row][col]="."
        

if __name__=="__main__":
    n = 4
    board = [['.' for _ in range(n)] for _ in range(n)]
    SolveNQueens(board, 0, n)

        
    