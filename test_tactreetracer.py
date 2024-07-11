import unittest
from tictactoe import TicTacToe
from tictactoe import TacTreeTracer


class Test_Backend(unittest.TestCase):
    def setUp(self) -> None:
        array1 = [1,0,-1]
        array2 = [0,1,-1]
        array3 = [1,-1,0]
        array = [array1,array2,array3]
        self.board = TicTacToe(array,1)
        self.tracer = TacTreeTracer(self.board)
    def tearDown(self) -> None:
        pass
        # self.board.dispose() 
    def test_get_opp_move(self):
        self.tracer.get_opp_move([0,1])
        self.assertEqual([[1,-1,-1],[0,1,-1],[1,-1,0]],self.tracer.get_board().get_board())




if __name__ == '__main__':
    unittest.main()