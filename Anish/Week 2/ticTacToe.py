# int -> [[str]]
def generateBoard(numRows):
    #return [[''] * numRows] * numRows
    b = []

    for _ in range(numRows):
        for _ in range(numRows):
            b.append('')

    return b
        

# [[str]], int, int, str -> [[str]]
def play(board, row, col, player):
    board[row][col] = player 

    return board

# [[str]] -> None
def printBoard(board):
    for i in board:
        print(i)

# str -> str
def printSeperator(sep):
    print(sep * 10)

# [[str]], [str] -> bool
def isHorizontalWin(board):
    for i in board:
        #if all(i == board[0] for i in board):
        #if board.count(len(i) == i[0]) != len(i):
            #return False 

        if len(set(board)) == 1:
            return True

    return False


# [[str]], str
def isVerticalWin(board):
    for i in range(len(board)):
        for j in range(len(board)):
            return 

# [[str]] -> bool
def isNegDiagonalWin(board):
    return len(set([board[i][i] for i in range(len(board))])) == 1

# [[str]] -> bool
def isPosDiagonalWin(board):
    return len(set([board[len(board)-1-i][i] for i in range(len(board))])) == 1
    #return [board[len(board)-1-i][i] for i in range(len(board))]

def isDiagonalWin(board):
    return isPosDiagonalWin(board) or isNegDiagonalWin(board)




b = [
    ['x', 'o', ' '], 
    [' ', 'x', ' '], 
    ['o', 'o', 'x']
]

print(isDiagonalWin(b))
