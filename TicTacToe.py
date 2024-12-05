import random
import time
import math
from threading import Thread

def aiGen():
    rows, cols = 10, 10
    global heatMatrix
    heatMatrix = [[0 for _ in range(cols)] for _ in range(rows)]
    totalVal = rows * cols
    uniqueNums = random.sample(range(101), totalVal)
    i = 0
    for x in range(rows):
        for y in range(cols):
            heatMatrix[x][y] = uniqueNums[i]
            i+=1
    


def TicTacToe():
    gameboard = [[]]


aiThread = Thread(target=aiGen, args=())
aiThread.start()
aiThread.join()
print(heatMatrix)


#┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#│                                       │
#├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
#│                                       │
#└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
