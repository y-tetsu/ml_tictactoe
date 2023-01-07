import itertools
import csv

from tictactoe import B, O, X
from scoring import RandomRecords


class Patterns:
    def __init__(self, scores):
        self.scores = scores
        self.patterns = {
            'h1': (0, 1, 2),
            'h2': (3, 4, 5),
            'h3': (6, 7, 8),
            'v1': (0, 3, 6),
            'v2': (1, 4, 7),
            'v3': (2, 5, 8),
            'd1': (0, 4, 8),
            'd2': (2, 4, 6),
        }
        self.indexs = {}

    def to_index(self, cells):
        repeat = len(cells)
        if repeat not in self.indexs:
            product = enumerate(itertools.product([B, O, X], repeat=repeat))
            self.indexs[repeat] = {j: i for i, j in product}
        return self.indexs[repeat][cells]

    def get_header(self):
        header = ['rate']
        for key, value in self.patterns.items():
            header += [key + '-' + str(i) for i in range(3**len(value))]
        return header

    def get_dataset(self, board, score):
        dataset = {'rate': score['total'] / score['count']}
        for key, value in self.patterns.items():
            pattern = tuple([board[i] for i in value])
            if key not in dataset:
                dataset[key] = [0 for _ in range(3**len(value))]
            dataset[key][self.to_index(pattern)] = 1
        return dataset

    def to_csv(self, name):
        with open(name, 'w', newline='') as f:
            w = csv.writer(f)
            header = self.get_header()
            w.writerow(header)
            scores = sorted(self.scores.items(),
                            key=lambda x: x[1]['total'] / x[1]['count'])
            for board, score in scores:
                dataset = self.get_dataset(board, score)
                line = [dataset['rate']]
                for key in self.patterns.keys():
                    line += dataset[key]
                w.writerow(line)


if __name__ == '__main__':
    for num in [10, 100, 1000, 10000]:
        name = 'rand' + str(num) + '.csv'
        print(f'\n[{name}]')
        scores = RandomRecords(num).scoring()
        patterns = Patterns(scores)
        patterns.to_csv(name)
