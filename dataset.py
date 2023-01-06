import itertools

from tictactoe import B, O, X
from scoring import RandomRecords


class Patterns:
    def __init__(self, scores):
        self.scores = scores
        pattern3 = enumerate(itertools.product([B, O, X], repeat=3))
        self.to_index = {j: i for i, j in pattern3}
        self.num = len(self.to_index.keys())


if __name__ == '__main__':
    scores = RandomRecords(10).scoring()
    patterns = Patterns(scores)
