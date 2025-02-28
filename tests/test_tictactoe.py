import unittest
from tictactoe import TicTacToe, B, O, X, D, KEY


class TestTicTacToe(unittest.TestCase):
    """Unit tests for the TicTacToe class."""

    def test_init(self):
        """Tests the initialization of the TicTacToe class."""
        expected = {O: 'player1', X: 'player2'}
        t = TicTacToe('player1', 'player2')
        self.assertEqual(t.move, expected)
        self.assertEqual(B, 0)
        self.assertEqual(O, 1)
        self.assertEqual(X, 2)
        self.assertEqual(D, 3)
        self.assertEqual(KEY, ' OX')

    def test_judge(self):
        """Tests the judge method of the TicTacToe class."""
        t = TicTacToe('player1', 'player2')
        # B
        board = [B for _ in range(9)]
        self.assertEqual(t.judge(board), B)
        # O
        board = [O, O, O,
                 B, B, B,
                 B, B, B]
        self.assertEqual(t.judge(board), O)
        board = [B, B, B,
                 O, O, O,
                 B, B, B]
        self.assertEqual(t.judge(board), O)
        board = [B, B, B,
                 B, B, B,
                 O, O, O]
        self.assertEqual(t.judge(board), O)
        board = [O, B, B,
                 B, O, B,
                 B, B, O]
        self.assertEqual(t.judge(board), O)
        # X
        board = [X, B, B,
                 X, B, B,
                 X, B, B]
        self.assertEqual(t.judge(board), X)
        board = [B, X, B,
                 B, X, B,
                 B, X, B]
        self.assertEqual(t.judge(board), X)
        board = [B, B, X,
                 B, B, X,
                 B, B, X]
        self.assertEqual(t.judge(board), X)
        board = [B, B, X,
                 B, X, B,
                 X, B, B]
        self.assertEqual(t.judge(board), X)
        # D
        board = [X, O, X,
                 X, O, O,
                 O, X, O]
        self.assertEqual(t.judge(board), D)
