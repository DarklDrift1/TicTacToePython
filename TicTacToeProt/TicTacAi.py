import random
import time


class Ai:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def __repr__(self):
        return(f'AI:= {self.rows}'
               f'{self.cols}')

    def calc(self):
        heatList = []
        heatMatrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        totalVal = self.rows * self.cols
        uniqueNums = random.sample(range(101), totalVal)
        i = 0
                                                            #Creates the HeatMatrix
        for x in range(self.rows):
            for y in range(self.cols):
                heatMatrix[x][y] = uniqueNums[i]
                i+=1

                                                            #Converts the HeatMatrix data into a coordinate list
        for i in range(10):
            for j in range(10):
                heatList.append((i, j, heatMatrix[i][j]))

        heatList.sort(key=lambda x: x[2], reverse=True)     #Sorts the HeatList from 100-0

        heatList = [(i, j) for i, j, _ in heatList]         #Converts the heatlist data into a different a form like this: (cols,rows)

        #time.sleep(5)
        for i in range(0,10):
            print(heatMatrix[i], heatList[i])
        print('Working')
        return(heatList)