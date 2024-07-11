import unittest
from tictactoe import TicTacToe

# class TestTicTacToe(unittest.TestCase):
#     def setUp(self):
#          board = [[1,0,1],[1,0,0],[-1,-1,-1]]
#          tac = TicTacToe(board, -1)
#     def test_board():
#            pass     
#     def testing123(self):
#          self.assertEquals(1,1)

class Test_Backend(unittest.TestCase):
    def setUp(self) -> None:
        array1 = [1,0,-1]
        array2 = [0,1,-1]
        array3 = [1,-1,0]
        array = [array1,array2,array3]
        self.board = TicTacToe(array,1)
    def tearDown(self) -> None:
        pass
        # self.board.dispose() 
    def test_get_board(self):
        array1 = [1,0,-1]
        array2 = [0,1,-1]
        array3 = [1,-1,0]
        array = [array1,array2,array3]
        self.assertEqual(self.board.get_board(), array)
    def test_get_move(self):
        self.assertEqual(self.board.get_move(),1)
    def test_check_winner(self):
        self.assertEqual(self.board.check_winner(),0)
        self.board.update_board([1,0])
        self.assertEqual(self.board.check_winner(),1)
        self.assertEqual(self.board.get_move(),-1)

    # This test is designed to fail for demonstration purposes.


if __name__ == '__main__':
    unittest.main()