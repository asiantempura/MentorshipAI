from itertools import * 
from functools import *

Board = list[list[str]]


def generateBoardF(nums: list[int]):
    #print(nums)
    '''match nums:
        case []:
            return []
        case [x, y, z]:
            return [x, y, z]
        case [x, y, z, *a]:
            return [[x, y, z]] + generateBoardF(a)'''
    if nums == []:
        return 
    elif len(nums) == 3:
        return [nums]
    else:
        return [nums[0:3]] + generateBoardF(nums[3:])
  
#print(generateBoardF(list(range(0, 9))))
  
def if_then_else(cond, out1, out2):
    if cond:
        return out1
    else:
        if hasattr(out2, '__call__'):
            return out2()
        else:
            return out2
    
def isListEmpty(l):
    return not l

def isLenThis(l, num):
    return len(l) == num

def seeBoard(l):
    return if_then_else(isListEmpty(l), 
                            [], 
                            if_then_else(isLenThis(l, 3),
                                [l],
                                partial(appendPartial, [l[0:3]], partial(seeBoard, l[3:]))))
    
def appendPartial(out1, out2):
    return out1 + out2()
    

print(seeBoard(list(range(0, 9))))


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

    printBoard()
    printGameOver()

#main()

        

