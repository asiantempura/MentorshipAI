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
        if board.count(len(i) == i[0]) != len(i):
            return False 

    return True


# [[str]], str
#def isVerticalWin():



b = generateBoard(3)
printBoard(b)

printSeperator('-')

play(b, 0, 2, 'x')
printBoard(b)
