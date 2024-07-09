import numpy as np
import math
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
        self.solution_space = list(range(9))
    def player_move(self):
        """
        Implements the min-max algorithm here, returns the move bot decides to go with
        This will also update the bot's board
        """
        def minimax(player_move,board):
            if (self.board.check_winner == 1 or self.board.check_winner == -1):
                return self.board.check_winner()
            
            if (player_move == 1):
                best_value = -math.inf
                for i in range(9):
                    test_board = TicTacToe(board.get_board(),1)
                    if (self.board.spot_empty((i//3,i%3))):
                        test_board.update_board([i//3,i%3])
                        value = minimax(-1,test_board)
                        if (value>best_value):
                            best_value = value
                # Maximize score
            elif (player_move == -1):
                for i in range(9):
                    test_board = TicTacToe(board.get_board(),-1)
                    if (self.board.spot_empty((i//3,i%3))):
                        test_board.update_board([i//3,i%3])
                        minimax(1,test_board)
                        value = minimax(-1,test_board)
                        if (value>best_value):
                            best_value = value
    def get_opp_move(self,move):
        self.board[move[0]][move[1]] = -1
        self.solution_space.pop(3*move[0]+move[1])
    def display_board(self):
        pass
def main():
    moves = 0
    b = TacTreeTracer() #Player/Computer
    board1 = list(np.zeros((4,4)))
    board = TicTacToe(board1,1)
    a = TacTreeTracer(board1)
    b = TacTreeTracer(board1)
    while (board.check_winner() == 0 or moves < 9):
        moves+=1
        a_move = a.player_move()
        b.get_opp_move(a_move)
        b_move = b.player_move()
        a.get_opp_move(b_move)
    print(board.check_winner())
if __name__ == '__main__':
    main()
        