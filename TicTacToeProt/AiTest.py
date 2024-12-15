import TicTacAi
import TicTacBoard
import TicTacWin

Ais = TicTacAi.Ai(10,10)
gameboard = [[' ' for _ in range(10)] for _ in range(10)]
boards = TicTacBoard.board(gameboard)

print(Ais.calc())
print(boards.create())