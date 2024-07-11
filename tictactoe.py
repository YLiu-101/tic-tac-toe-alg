import numpy as np
import math
import copy
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
                if abs(sum(row)) == 3:
                    return sum(row)/3
            return 0
        def check_cols():
            for row in np.transpose(np.array(self.board)):
                if abs(sum(row)) == 3:
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
        def check_full():
            count = 0
            for row in self.board:
                for j in row:
                    if j==0:
                        return False
            return True
        if check_rows():
            return check_rows()
        if check_cols():
            return check_cols()
        if check_diags():
            return check_diags()
        if check_full():
            return 900
        return 0
    def spot_empty(self, position):
        if self.board[position[0]][position[1]] == 0:
            return True
        return False
    def display_board(self):
        """"
        Used if no frontend is present: displays the tic tac toe board to the terminal
        """
        def num_converter(num):
            if (num == 1):
                return "O"
            elif (num == -1):
                return "X"
            return " " 
        array = self.get_board()
        string = 10*"-" + "\n"
        for i in array:
            for j in i:
                string += str(num_converter(j))
                string += " | "
            string = string[0:-3]
            string += "\n"
            string += 10*"-"
            string += "\n"
        print(string)
class TacTreeTracer:
    def __init__(self,board:TicTacToe):
        self.board = board
        self.solution_space = list(range(9))
    def player_move(self):
        """
        Implements the min-max algorithm here, returns the move bot decides to go with
        This will also update the bot's board
        """
        def submini(sign,board):
            best_value = -sign*math.inf
            best_move = [100,100]
            for i in range(9):
                # print("Testing new one +1")
                if (board.spot_empty((i//3,i%3))):
                    new_array = copy.deepcopy(board.get_board())
                    test_board = TicTacToe(new_array,sign)
                    test_board.update_board([i//3,i%3])
                    value = minimax(-sign,test_board)[0]
                    if ((value>best_value and sign>0) or (value<best_value and sign<0)):
                        best_value = value
                        best_move = [i//3,i%3]
            return (best_value,best_move)
        def minimax(player_move,board): 
            board.display_board()
            if (board.check_winner() == 1 or board.check_winner() == -1 or board.check_winner() == 900):
                if board.check_winner() == 900:
                    print("Tie")
                    return (0,[math.inf,math.inf])
                print("One winner")
                return (board.check_winner(),[math.inf,math.inf])
            if (player_move == 1):
                return submini(1,board)
            elif (player_move == -1):
                return submini(-1,board)

        a = minimax(self.player_position,self.board)
        print(self.board.get_board())
        return a
    def get_opp_move(self,move):
        """"
        Takes in the opponent's move to update its own board

        @return: None
        """
        self.board[move[0]][move[1]] = -1
        self.solution_space.pop(3*move[0]+move[1])
    def display_board(self):
        """"
        Used if no frontend is present: displays the tic tac toe board to the terminal
        """
        array = self.board.get_board()
        string = 10*"-" + "\n"
        for i in array:
            for j in i:
                string += str(num_converter(j))
                string += " | "
            string = string[0:-3]
            string += "\n"
            string += 10*"-"
            string += "\n"
        print(string)
        def num_converter(num):
            if (num == 1):
                return "O"
            elif (num == -1):
                return "X"
            return " "        
        
def main():
    moves = 0
    b = TacTreeTracer() #Player/Computer
    board1 = list(np.zeros((4,4)))
    board = TicTacToe(board1,1)
    a = TacTreeTracer(board1)
    b = TacTreeTracer(board1)
    while (board.check_winner() == 0 and moves < 9):
        moves+=1
        a_move = a.player_move()
        b.get_opp_move(a_move)
        b_move = b.player_move()
        a.get_opp_move(b_move)
    print(f"And the winner is {board.check_winner()}!")
if __name__ == '__main__':
    main()
        