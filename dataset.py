import itertools
import csv

from tictactoe import B, O, X
from scoring import RandomRecords


class Patterns:
    def __init__(self, scores):
        self.scores = scores
        self.patterns = {
            'h1': [0, 1, 2],
            'h2': [3, 4, 5],
            'h3': [6, 7, 8],
            'v1': [0, 3, 6],
            'v2': [1, 4, 7],
            'v3': [2, 5, 8],
            'd1': [0, 4, 8],
            'd2': [2, 4, 6],
        }
        self.indexs = {}

    def to_index(self, cells):
        repeat = len(cells)
        if repeat not in self.indexs:
            product = enumerate(itertools.product([B, O, X], repeat=repeat))
            self.indexs[repeat] = {j: i for i, j in product}
        return self.indexs[repeat][cells]


if __name__ == '__main__':
    scores = RandomRecords(10).scoring()
    patterns = Patterns(scores)
