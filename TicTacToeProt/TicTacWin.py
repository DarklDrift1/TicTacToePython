class win():
    def __init__(self, board, gameRuns):
        self.board = board
        self.gameRuns = gameRuns

    def __repr__(self):
        return(f'{self.board}'
               f'{self.gameRuns}')
    
    def check(self):
        global WonBool
        gameRuns = True
        WonBool = ''
        # Rows
        for row in self.board:
            for i in range(6): 
                if 'O' * 5 in ''.join(row[i:i+5]) or 'X' * 5 in ''.join(row[i:i+5]):
                    WonBool = 'O' if 'O' * 5 in ''.join(row[i:i+5]) else 'X'
                    gameRuns = False
                    return gameRuns

        # Columns
        for col in range(10):
            columnstr = ''.join([self.board[row][col] for row in range(10)])
            for i in range(6):
                if 'O' * 5 in columnstr[i:i+5] or 'X' * 5 in columnstr[i:i+5]:
                    WonBool = 'O' if 'O' * 5 in columnstr[i:i+5] else 'X'
                    gameRuns = False
                    return gameRuns

        # TL to BR Diagonals
        for i in range(6):
            for j in range(6-i):
                diagonalstr = ''.join([self.board[i + j + k][j+k] for k in range(5)])
                if 'O' * 5 in diagonalstr or 'X' * 5 in diagonalstr:
                    WonBool = 'O' if 'O' * 5 in diagonalstr else 'X'
                    gameRuns = False
                    return gameRuns

        # TR to BL Diagonals
        for i in range(6):
            for j in range(6-i):
                diagonalstr = ''.join([self.board[i + j + k][9 - j - k] for k in range(5)])
                if 'O' * 5 in diagonalstr or 'X' * 5 in diagonalstr:
                    WonBool = 'O' if 'O' * 5 in diagonalstr else 'X'
                    gameRuns = False
                return gameRuns

        print('')
        return gameRuns
    
    def WonBool(self):
        return WonBool