Board = list[list[str]]

def generateBoard(numRows: int) -> Board: 
    return [[str(i) for i in range(j * numRows, j * numRows + numRows)] for j in range(numRows)]
    #return [[''] * numRows] * numRows
    '''b = []

    for _ in range(numRows):
        for _ in range(numRows):
            b.append('')

    return b'''
        

def playMove(board: Board, boardPosition: int, player: str) -> Board:
    board[boardPosition // len(board)][boardPosition % len(board)] = player 

    return board

def printBoard(board: Board) -> None:
    for i in board:
        print(i)

def printSeperator(sep: str) -> None:
    print(sep * 10)

def isHorizontalWin(board: Board) -> bool:
    for i in board:
        #if all(i == board[0] for i in board):
        #if board.count(len(i) == i[0]) != len(i):
            #return False 

        if len(set(i)) == 1:
            return True

    return False


def isVerticalWin(board: Board) -> str:
    for i in range(len(board)):
        if len(set([board[j][i] for j in range(len(board))])) == 1:
            return True 

    return False


def isNegDiagonalWin(board: Board) -> bool:
    return len(set([board[i][i] for i in range(len(board))])) == 1

def isPosDiagonalWin(board: Board) -> bool:
    return len(set([board[len(board)-1-i][i] for i in range(len(board))])) == 1
    #return [board[len(board)-1-i][i] for i in range(len(board))]

def isDiagonalWin(board: Board) -> bool:
    return isPosDiagonalWin(board) or isNegDiagonalWin(board)

def isDraw(board: Board, numMoves: int) -> bool:
    return numMoves == len(board) ** 2

def isGameOver(board: Board, numMoves: int) -> bool:
    return isHorizontalWin(board) or isVerticalWin(board) or isDiagonalWin(board) or isDraw(board, numMoves)

def takeInput() -> int:
    return int(input("Move: "))

def checkInput(board: Board, input: int) -> bool:
    return 0 <= input and input < len(board) ** 2

def printGameOver() -> None:
    print('Game over!')

def playerChar(numMoves: int) -> str:
    if numMoves % 2 == 0:
        return 'x'
    else:
        return 'o'

def main() -> None:
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
        

