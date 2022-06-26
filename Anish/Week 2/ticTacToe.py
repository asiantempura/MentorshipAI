# int -> [[str]]
def generateBoard(numRows):
    return [[str(i) for i in range(j * numRows, j * numRows + numRows)] for j in range(numRows)]
    #return [[''] * numRows] * numRows
    '''b = []

    for _ in range(numRows):
        for _ in range(numRows):
            b.append('')

    return b'''
        

# [[str]], int, int, str -> [[str]]
def playMove(board, boardPosition, player):
    board[boardPosition / len(board)][boardPosition % len(board)] = player 

    return board

# [[str]] -> None
def printBoard(board):
    for i in board:
        print(i)

# str -> None
def printSeperator(sep):
    print(sep * 10)

# [[str]], [str] -> bool
def isHorizontalWin(board):
    for i in board:
        #if all(i == board[0] for i in board):
        #if board.count(len(i) == i[0]) != len(i):
            #return False 

        if len(set(i)) == 1:
            return True

    return False


# [[str]], str
def isVerticalWin(board):
    for i in range(len(board)):
        if len(set([board[j][i] for j in range(len(board))])) == 1:
            return True 

    return False


# [[str]] -> bool
def isNegDiagonalWin(board):
    return len(set([board[i][i] for i in range(len(board))])) == 1

# [[str]] -> bool
def isPosDiagonalWin(board):
    return len(set([board[len(board)-1-i][i] for i in range(len(board))])) == 1
    #return [board[len(board)-1-i][i] for i in range(len(board))]

# [[str]] -> bool
def isDiagonalWin(board):
    return isPosDiagonalWin(board) or isNegDiagonalWin(board)

# [[str]], int -> bool
def isDraw(board, numMoves):
    return numMoves == len(board) ** 2

# [[str]], int -> bool
def isGameOver(board, numMoves):
    return isHorizontalWin(board) or isVerticalWin(board) or isDiagonalWin(board) or isDraw(board, numMoves)

# _ -> int
def takeInput():
    return int(raw_input("Move: "))

# [[str]], int -> bool
def checkInput(board, input):
    return 0 <= input and input < len(board) ** 2

# _ -> None
def printGameOver():
    print('Game over!')

# _ -> str
def playerChar(numMoves):
    if numMoves % 2 == 0:
        return 'x'
    else:
        return 'o'

# _ -> None
def main():
    board = generateBoard(3)
    numMoves = 0

    while not isGameOver(board, numMoves):
        printBoard(board)
        printSeperator('-') 

        move = takeInput()
        
        if checkInput(board, move):
            playMove(board, move, playerChar(numMoves))
            numMoves += 1

    printGameOver()

main()
        

