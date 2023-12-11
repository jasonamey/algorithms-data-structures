# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. 
# The rules of Tic-Tac-Toe are:

# Players take turns placing characters into empty squares ' '.

# The first player A always places 'X' characters, while the second 
# player B always places 'O' characters.

# 'X' and 'O' characters are always placed into empty squares,
# never on filled ones.

# The game ends when there are three of the same (non-empty) character
# filling any row, column, or diagonal.

# The game also ends if all squares are non-empty.

# No more moves can be played if the game is over.

# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates 
# that the ith move will be played on grid[rowi][coli]. return the winner 
# of the game if it exists (A or B). In case the game ends in a draw 
# return "Draw". If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), 
# the grid is initially empty, and A will play first.

class Solution:
    def check_rows(self, b, player):
        for i in range(0, 3):
            if b[i][0] == b[i][1] == b[i][2] == player: 
                return True
        return False
    
    def check_cols(self, b, player):
        for i in range(0,3):
            if b[0][i] == b[1][i] == b[2][i] == player: 
                return True
        return False
    
    def check_diagonal(self, b, player): 
        return (b[0][0] == b[1][1] == b[2][2] == player) or (b[0][2] == b[1][1] == b[2][0] == player)
    
    def check_board(self, b, player): 
        if self.check_rows(b,player) or self.check_cols(b,player) or self.check_diagonal(b,player):
            return player
        return None 
    
    def tictactoe(self, moves):
        board = [[0,0,0] for _ in range(0,3)]
        for i in range(0,len(moves)):
            move = 'A' if i % 2 == 0 else 'B'
            board[moves[i][0]][moves[i][1]] = move
        winner = self.check_board(board, 'A') or self.check_board(board, 'B') 
        if winner: 
            return winner
        return 'Draw' if len(moves) == 9 else 'Pending'
  
s = Solution()

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
assert s.tictactoe(moves) == 'A'

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
assert s.tictactoe(moves) == 'B'

moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
assert s.tictactoe(moves) == 'Draw'

moves = [[0,0],[1,1]]
assert s.tictactoe(moves) == 'Pending'