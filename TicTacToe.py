import random
import time
from threading import Thread


def aiGen():
    global heatMatrix
    global heatList
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

    time.sleep(5)
    #for i in range(0,10):
    #    print(heatMatrix[i], heatList[i])
    


def TicTacToe():
    rows, cols = 10, 10
    global gameboard
    global gameRuns
    gameRuns = True
    legal = True
    loaded = False
    gameboard = [['E' for _ in range(cols)] for _ in range(rows)]

    spinner = ['-', '\\', '|', '/']
    n = 0
    while aiThread.is_alive():
        print(f'\r|Project Amőba 2024| Betöltés...{spinner[n]}', end='')
        n+=1
        if n >= len(spinner):
            n=0
        time.sleep(0.2)
    print('')
    for i in range(1,4):
      print(f'Játék inditása... {i}')
      time.sleep(0.4)


    for i, (row, col) in enumerate(heatList):
      if gameRuns != True:
         print('DONE')
         return gameboard
      if i < rows * cols:
            moved = False
            while moved == False:
              rowinput = int(input('Kérem adja meg melyik sorba szeretné tenni az X-et (1-10): \t')) - 1
              colinput = int(input('Kérem adja meg melyik oszlopba szeretné tenni az X-et (1-10): \t')) - 1
              if 0 < rowinput+1 <= 10 and 0 < colinput+1 <= 10:
                if gameboard[rowinput][colinput] == 'E':
                    gameboard[rowinput][colinput] = 'X'
                    moved = True
                else:
                    print('A lépés nem legális!')
                    print('------')
                    moved = False
                    legal = False
              else:
                  moved = False
                  print('A megadott koordináta nem létezik!')

            if legal == True:
              if gameboard[row][col] != 'E':
                legal = False
              else:
                gameboard[row][col] = 'O'
                legal = True

      print(boardChunk(gameboard))
      gameRuns = WinCheck(gameboard, gameRuns)

def boardChunk(gameboard):
  visualBoard = ''
  Start = '''
     1   2   3   4   5   6   7   8   9  10
   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
1  │ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(*gameboard[0])

  visualBoard += Start
  for i in range(1,9):
    Mid = '''
{col}  │ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(*gameboard[i], col=i+1)
    visualBoard += Mid


  End = '''
10 │ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
   └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'''.format(*gameboard[9])
  visualBoard += End
  return visualBoard
        

def WinCheck(board, gameRuns):
    global WonBool
    WonBool = ''
    time.sleep(1)

    # Rows
    for row in board:
        for i in range(6): 
            if 'O' * 5 in ''.join(row[i:i+5]) or 'X' * 5 in ''.join(row[i:i+5]):
                WonBool = 'O' if 'O' * 5 in ''.join(row[i:i+5]) else 'X'
                gameRuns = False
                return gameRuns

    # Columns
    for col in range(10):
        columnstr = ''.join([board[row][col] for row in range(10)])
        for i in range(6):
            if 'O' * 5 in columnstr[i:i+5] or 'X' * 5 in columnstr[i:i+5]:
                WonBool = 'O' if 'O' * 5 in columnstr[i:i+5] else 'X'
                gameRuns = False
                return gameRuns

    # TL to BR Diagonals
    for i in range(6):
        for j in range(6-i):
            diagonalstr = ''.join([board[i + j + k][j+k] for k in range(5)])
            if 'O' * 5 in diagonalstr or 'X' * 5 in diagonalstr:
                WonBool = 'O' if 'O' * 5 in diagonalstr else 'X'
                gameRuns = False
                return gameRuns

    # TR to BL Diagonals
    for i in range(6):
        for j in range(6-i):
            diagonalstr = ''.join([board[i + j + k][9 - j - k] for k in range(5)])
            if 'O' * 5 in diagonalstr or 'X' * 5 in diagonalstr:
                WonBool = 'O' if 'O' * 5 in diagonalstr else 'X'
                gameRuns = False
                return gameRuns

    print('')
    return gameRuns


aiThread = Thread(target=aiGen, args=())
gameThread = Thread(target=TicTacToe, args=())
aiThread.start()

gameThread.start()
gameThread.join()


print(f'{WonBool} WON' if WonBool != '' else 'DRAW')