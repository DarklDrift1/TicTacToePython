import random
import time
import math
from threading import Thread


def aiGen():
    global heatMatrix
    heatList = []
    rows, cols = 10, 10
    heatMatrix = [[0 for _ in range(cols)] for _ in range(rows)]
    totalVal = rows * cols
    uniqueNums = random.sample(range(101), totalVal)
    i = 0
    for x in range(rows):
        for y in range(cols):
            heatMatrix[x][y] = uniqueNums[i]
            i+=1
    for i in range(10):
        for j in range(10):
            heatList.append((i, j, heatMatrix[i][j]))

    heatList.sort(key=lambda x: x[2], reverse=True)

    heatList = [(i, j) for i, j, _ in heatList]

    time.sleep(3)
    for i in range(0,10):
        print(heatMatrix[i], heatList[i])
    


def TicTacToe():
    rows, cols = 10, 10
    global gameboard
    gameboard = [[random.choice('O' 'X') for _ in range(cols)] for _ in range(rows)]
    winThread = Thread(target=WinCheck, args=(gameboard,))
    winThread.start()
    for i in range(0,10):
        print(gameboard[i])

def WinCheck(board):
    global WonBool
    WonBool = ''
    time.sleep(1)
    # Rows
    for row in board:
      if 'O' * 5 in ''.join(row) or 'X' * 5 in ''.join(row):
        WonBool = 'O' if 'O' * 5 in ''.join(row) else 'X'
        return()

    # Colums
    for col in range(10):
      columnstr = ''.join([board[row][col] for row in range(10)])
      if 'O' * 5 in columnstr or 'X' * 5 in columnstr:
        WonBool = 'O' if 'O' * 5 in columnstr else 'X'
        return()

    # TL to BR Diagonals
    for i in range(6):
      diagonalstr = ''.join([board[i + j][j] for j in range(10 - i)])
      if 'O' * 5 in diagonalstr or 'X' * 5 in diagonalstr:
        WonBool = 'O' if 'O' * 5 in diagonalstr else 'X'
        return()

    # TR to BL Diagonals
    for i in range(6):
      diagonalstr = ''.join([board[i + j][9 - j] for j in range(10 - i)])
      if 'O' * 5 in diagonalstr or 'X' * 5 in diagonalstr:
        WonBool = 'O' if 'O' * 5 in diagonalstr else 'X'
        return()

    print('')


aiThread = Thread(target=aiGen, args=())
gameThread = Thread(target=TicTacToe, args=())
gameThread.start()
aiThread.start()
gameThread.join()
aiThread.join()

boardChunkStart = '''
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(*gameboard[0])

print(boardChunkStart)
for i in range(1,9):
        boardChunkMid = '''│ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(*gameboard[i])
        print(boardChunkMid)

boardChunkEnd = '''│ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'''.format(*gameboard[9])



print(boardChunkEnd)
print(f'{WonBool} WON' if WonBool != '' else 'DRAW')





#for i in range(0,10):
#        strboardVer = ''
#        strboardCro = ''
#        strboardHor = '{}{}{}{}{}{}{}{}{}{}'.format(*board[i])
#        if strboardHor.count('O'*5) > 0:
#            print('Won Hor O', i)
#            WonBool = 'O'
#            return()
#        elif strboardHor.count('X'*5) > 0:
#            print('Won Hor X', i)
#            WonBool = 'X'
#            return()
#        for j in range(0,10):
#            strboardVer += '{}'.format(board[j][i])
#            if strboardVer.count('O'*5) > 0:
#                print('Won Ver O', i,j)
#                WonBool = 'O'
#                return()
#            elif strboardVer.count('X'*5) > 0:
#                print('Won Ver X', i,j)
#                WonBool = 'X'
#                return()
#        for v in range(0,10):
#            for y in range(0,10):
#                strboardCro += '{}'.format(board[v+i][y+i])
#                if strboardCro.count('O'*5) > 0:
#                    print('Won Cro O', i+v,i+y)
#                    WonBool = 'O'
#                    return()
#                elif strboardCro.count('X'*5) > 0:
#                    print('Won Cro X', i+v,i+y)
#                    WonBool = 'X'
#                    return()
#        print(strboardVer)