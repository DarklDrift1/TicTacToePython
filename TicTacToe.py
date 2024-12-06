import random
import time
import math
from threading import Thread


def aiGen():
    global heatMatrix
    rows, cols = 10, 10
    heatMatrix = [[0 for _ in range(cols)] for _ in range(rows)]
    totalVal = rows * cols
    uniqueNums = random.sample(range(101), totalVal)
    i = 0
    for x in range(rows):
        for y in range(cols):
            heatMatrix[x][y] = uniqueNums[i]
            i+=1
    


def TicTacToe():
    rows, cols = 10, 10
    gameboard = [[random.choice('O' 'X') for _ in range(cols)] for _ in range(rows)]
    for i in range(0,10):
        print(gameboard[i])
    return(gameboard)
    


aiThread = Thread(target=aiGen, args=())
aiThread.start()
gameboard = TicTacToe()
aiThread.join()

boardChunkStart = f'''
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ {gameboard[0][0]}   {gameboard[0][1]}   {gameboard[0][2]}   {gameboard[0][3]}   {gameboard[0][4]}   {gameboard[0][5]}   {gameboard[0][6]}   {gameboard[0][7]}   {gameboard[0][8]}   {gameboard[0][9]} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''

print(boardChunkStart)
j = 0
for i in range(1,9):
        boardChunkMid = '''│ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(gameboard[i][j], gameboard[i][j+1], gameboard[i][j+2], gameboard[i][j+3], gameboard[i][j+4], gameboard[i][j+5], gameboard[i][j+6], gameboard[i][j+7], gameboard[i][j+8], gameboard[i][j+9])
        print(boardChunkMid)

boardChunkEnd = f'''│ {gameboard[9][0]}   {gameboard[9][1]}   {gameboard[9][2]}   {gameboard[9][3]}   {gameboard[9][4]}   {gameboard[9][5]}   {gameboard[9][6]}   {gameboard[9][7]}   {gameboard[9][8]}   {gameboard[9][9]} │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'''



print(boardChunkEnd)

#├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
