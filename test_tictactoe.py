import unittest
from backend import tictactoe

# class TestTicTacToe(unittest.TestCase):
#     def setUp(self):
#          board = [[1,0,1],[1,0,0],[-1,-1,-1]]
#          tac = TicTacToe(board, -1)
#     def test_board():
#            pass     
#     def testing123(self):
#          self.assertEquals(1,1)

class Test_Backend(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(2+2.0000000000000001, 4)

if __name__ == '__main__':
    unittest.main()