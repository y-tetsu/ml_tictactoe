import unittest
from dataset import Patterns
from tictactoe import B, O, X


class TestPatterns(unittest.TestCase):
    """Unit tests for the Patterns class."""

    def test_init(self):
        """Tests the initialization of the Patterns class."""
        scores = 'scores'
        patterns = {
            'h1': (0, 1, 2),
            'h2': (3, 4, 5),
            'h3': (6, 7, 8),
            'v1': (0, 3, 6),
            'v2': (1, 4, 7),
            'v3': (2, 5, 8),
            'd1': (0, 4, 8),
            'd2': (2, 4, 6),
        }
        p = Patterns('scores')
        self.assertEqual(p.scores, scores)
        self.assertEqual(p.patterns, patterns)
        self.assertEqual(p.indexs, {})

    def test_to_index(self):
        """Tests the to_index method of the Patterns class."""
        p = Patterns('scores')
        to_index2 = {(0, 0): 0,
                     (0, 1): 1,
                     (0, 2): 2,
                     (1, 0): 3,
                     (1, 1): 4,
                     (1, 2): 5,
                     (2, 0): 6,
                     (2, 1): 7,
                     (2, 2): 8}
        self.assertEqual(p.to_index((1, 2)), 5)
        self.assertEqual(p.indexs[2], to_index2)

        to_index3 = {(0, 0, 0): 0,
                     (0, 0, 1): 1,
                     (0, 0, 2): 2,
                     (0, 1, 0): 3,
                     (0, 1, 1): 4,
                     (0, 1, 2): 5,
                     (0, 2, 0): 6,
                     (0, 2, 1): 7,
                     (0, 2, 2): 8,
                     (1, 0, 0): 9,
                     (1, 0, 1): 10,
                     (1, 0, 2): 11,
                     (1, 1, 0): 12,
                     (1, 1, 1): 13,
                     (1, 1, 2): 14,
                     (1, 2, 0): 15,
                     (1, 2, 1): 16,
                     (1, 2, 2): 17,
                     (2, 0, 0): 18,
                     (2, 0, 1): 19,
                     (2, 0, 2): 20,
                     (2, 1, 0): 21,
                     (2, 1, 1): 22,
                     (2, 1, 2): 23,
                     (2, 2, 0): 24,
                     (2, 2, 1): 25,
                     (2, 2, 2): 26}
        self.assertEqual(p.to_index((1, 2, 0)), 15)
        self.assertEqual(p.indexs[3], to_index3)

    def test_get_header(self):
        """Tests the get_header method of the Patterns class."""
        header = [
            'ave',
            'h1-0', 'h1-1', 'h1-2', 'h1-3', 'h1-4', 'h1-5', 'h1-6', 'h1-7', 'h1-8', 'h1-9', 'h1-10', 'h1-11', 'h1-12', 'h1-13', 'h1-14', 'h1-15', 'h1-16', 'h1-17', 'h1-18', 'h1-19', 'h1-20', 'h1-21', 'h1-22', 'h1-23', 'h1-24', 'h1-25', 'h1-26',  # noqa: E501
            'h2-0', 'h2-1', 'h2-2', 'h2-3', 'h2-4', 'h2-5', 'h2-6', 'h2-7', 'h2-8', 'h2-9', 'h2-10', 'h2-11', 'h2-12', 'h2-13', 'h2-14', 'h2-15', 'h2-16', 'h2-17', 'h2-18', 'h2-19', 'h2-20', 'h2-21', 'h2-22', 'h2-23', 'h2-24', 'h2-25', 'h2-26',  # noqa: E501
            'h3-0', 'h3-1', 'h3-2', 'h3-3', 'h3-4', 'h3-5', 'h3-6', 'h3-7', 'h3-8', 'h3-9', 'h3-10', 'h3-11', 'h3-12', 'h3-13', 'h3-14', 'h3-15', 'h3-16', 'h3-17', 'h3-18', 'h3-19', 'h3-20', 'h3-21', 'h3-22', 'h3-23', 'h3-24', 'h3-25', 'h3-26',  # noqa: E501
            'v1-0', 'v1-1', 'v1-2', 'v1-3', 'v1-4', 'v1-5', 'v1-6', 'v1-7', 'v1-8', 'v1-9', 'v1-10', 'v1-11', 'v1-12', 'v1-13', 'v1-14', 'v1-15', 'v1-16', 'v1-17', 'v1-18', 'v1-19', 'v1-20', 'v1-21', 'v1-22', 'v1-23', 'v1-24', 'v1-25', 'v1-26',  # noqa: E501
            'v2-0', 'v2-1', 'v2-2', 'v2-3', 'v2-4', 'v2-5', 'v2-6', 'v2-7', 'v2-8', 'v2-9', 'v2-10', 'v2-11', 'v2-12', 'v2-13', 'v2-14', 'v2-15', 'v2-16', 'v2-17', 'v2-18', 'v2-19', 'v2-20', 'v2-21', 'v2-22', 'v2-23', 'v2-24', 'v2-25', 'v2-26',  # noqa: E501
            'v3-0', 'v3-1', 'v3-2', 'v3-3', 'v3-4', 'v3-5', 'v3-6', 'v3-7', 'v3-8', 'v3-9', 'v3-10', 'v3-11', 'v3-12', 'v3-13', 'v3-14', 'v3-15', 'v3-16', 'v3-17', 'v3-18', 'v3-19', 'v3-20', 'v3-21', 'v3-22', 'v3-23', 'v3-24', 'v3-25', 'v3-26',  # noqa: E501
            'd1-0', 'd1-1', 'd1-2', 'd1-3', 'd1-4', 'd1-5', 'd1-6', 'd1-7', 'd1-8', 'd1-9', 'd1-10', 'd1-11', 'd1-12', 'd1-13', 'd1-14', 'd1-15', 'd1-16', 'd1-17', 'd1-18', 'd1-19', 'd1-20', 'd1-21', 'd1-22', 'd1-23', 'd1-24', 'd1-25', 'd1-26',  # noqa: E501
            'd2-0', 'd2-1', 'd2-2', 'd2-3', 'd2-4', 'd2-5', 'd2-6', 'd2-7', 'd2-8', 'd2-9', 'd2-10', 'd2-11', 'd2-12', 'd2-13', 'd2-14', 'd2-15', 'd2-16', 'd2-17', 'd2-18', 'd2-19', 'd2-20', 'd2-21', 'd2-22', 'd2-23', 'd2-24', 'd2-25', 'd2-26',  # noqa: E501
        ]
        p = Patterns('scores')
        self.assertEqual(p.get_header(), header)

    def test_get_dataset(self):
        """Tests the get_dataset method of the Patterns class."""
        p = Patterns('scores')
        p.to_index((0, 0))
        board = [B, B, B,
                 B, B, B,
                 B, B, B]
        score = {'total': 0, 'count': 5}
        dataset = {
            'ave': 0.0,
            'h1': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'h2': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'h3': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'v1': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'v2': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'v3': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'd1': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'd2': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
        }
        self.assertEqual(p.get_dataset(board, score), dataset)

        board = [O, X, B,
                 O, X, B,
                 O, B, B]
        score = {'total': 60, 'count': 5}
        dataset = {
            'ave': 12.0,
            'h1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'h2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'h3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'v1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'v2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # noqa: E501
            'v3': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'd1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
            'd2': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # noqa: E501
        }
        self.assertEqual(p.get_dataset(board, score), dataset)
