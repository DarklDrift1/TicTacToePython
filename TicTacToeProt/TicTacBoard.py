class board:
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def __repr__(self):
       return(f'Board:= {self.gameboard}')
    
    def create(self):
        visualBoard = ''
        Start = '''
             1   2   3   4   5   6   7   8   9  10
           ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
        1  │ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
           ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(*self.gameboard[0])

        visualBoard += Start
        for i in range(1,9):
            Mid = '''
        {col}  │ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
           ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'''.format(*self.gameboard[i], col=i+1)
            visualBoard += Mid


        End = '''
        10 │ {}   {}   {}   {}   {}   {}   {}   {}   {}   {} │
           └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'''.format(*self.gameboard[9])
        visualBoard += End
        return visualBoard