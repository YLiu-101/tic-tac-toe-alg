import unittest
from backend import TicTacToe

class TestTicTacToe:
    def setUp(self):
         board = [[1,0,1],[1,0,0],[-1,-1,-1]]
         tac = TicTacToe(board, -1)
    def test_board():
           pass     
if __name__ == '__main__':
    unittest.main()
    