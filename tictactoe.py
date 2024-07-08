import numpy as np

class TicTacToe:
    """
    Takes care of all the underlying game functionality
    """
    def __init__(self, board, player_move):
        self.board = board
        self.player_move = player_move
    def get_board(self):
        return self.board
    def get_move(self):
        return self.player_move
    def update_board(self, new_move):
        # new_move format is (a,b)
        if self.board[new_move[0]][new_move[1]] != 0:
            raise Exception("Sorry spot is already taken")
        else:
            self.board[new_move[0]][new_move[1]] = self.player_move
        self.player_move = self.player_move*-1
    def check_winner(self):
        def check_rows():
            for row in self.board:
                if abs(sum(row) == 3):
                    return sum(row)/3
            return 0
        def check_cols():
            for row in np.transpose(np.array(self.board)):
                if abs(sum(row) == 3):
                    return sum(row)/3
                return 0
        def check_diags():
            sum1 = self.board[0][0] +self.board[1][1] + self.board[2][2]
            sum2 = self.board[2][0] +self.board[1][1] + self.board[0][2]
            if abs(sum1) == 3:
                return sum1/3
            elif abs(sum2) == 3:
                return sum2/3
            return 0
        if check_rows():
            return check_rows()
        if check_cols():
            return check_cols()
        if check_diags():
            return check_diags()
        return 0
    def spot_empty(self, position):
        if self.board[position[0]][position[1]] == 0:
            return True
        return False

class TacTreeTracer:
    def __init__(self,board:TicTacToe):
        self.board = board
                    
if __name__ == '__main__':
    pass
        