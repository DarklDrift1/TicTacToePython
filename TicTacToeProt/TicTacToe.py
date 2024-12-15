import random
import time
import TicTacAi
import TicTacBoard
import TicTacWin

def TicTacToe():
    rows, cols = 10, 10
    gameRuns = True
    global WonBool
    gameboard = [[' ' for _ in range(cols)] for _ in range(rows)]
    AiModule = TicTacAi.Ai(rows, cols)
    BoardModule = TicTacBoard.board(gameboard)
    WinModule = TicTacWin.win(gameboard, gameRuns)
    heatList = AiModule.calc()

    #spinner = ['-', '\\', '|', '/']
    #n = 0
    #while aiThread.is_alive():
    #    print(f'\r|Project Amőba 2024| Betöltés...{spinner[n]}', end='')
    #    n+=1
    #    if n >= len(spinner):
    #        n=0
    #    time.sleep(0.2)
    #print('')
    #for i in range(1,4):
    #  print(f'Játék inditása... {i}')
    #  time.sleep(0.4)


    for i, (row, col) in enumerate(heatList):
      if gameRuns != True:
         return (gameboard,WonBool)
      if i < rows * cols:
            moved = False
            while moved == False:
              rowinput = int(input('Kérem adja meg melyik sorba szeretné tenni az X-et (1-10): \t')) - 1
              colinput = int(input('Kérem adja meg melyik oszlopba szeretné tenni az X-et (1-10): \t')) - 1
              if 0 < rowinput+1 <= 10 and 0 < colinput+1 <= 10:
                if gameboard[rowinput][colinput] == ' ':
                    gameboard[rowinput][colinput] = 'X'
                    moved = True
                else:
                    print('A lépés nem legális!')
                    print('------')
                    moved = False
              else:
                  moved = False
                  print('A megadott koordináta nem létezik!')

            if gameboard[row][col] != ' ':
              moved = False
            else:
              gameboard[row][col] = 'O'

      print(BoardModule.create())
      gameRuns = WinModule.check()
      WonBool = WinModule.WonBool()



        


TicTacToe()

print(f'{WonBool} WON' if WonBool != '' else 'DRAW')

