import itertools
import csv

from tictactoe import B, O, X
from scoring import RandomRecords


class Patterns:
    """The Patterns class manages board patterns and generates datasets.

    Attributes:
        scores (dict): Dictionary of scores.
        patterns (dict): Dictionary representing board patterns.
        indexs (dict): Dictionary caching pattern indices.
    """

    def __init__(self, scores):
        """Constructor for the Patterns class.

        Args:
            scores (dict): Dictionary of scores.
        """
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
        """Converts a pattern of cells to an index.

        Args:
            cells (tuple): Pattern of cells.

        Returns:
            int: Index of the pattern.
        """
        repeat = len(cells)
        if repeat not in self.indexs:
            product = enumerate(itertools.product([B, O, X], repeat=repeat))
            self.indexs[repeat] = {j: i for i, j in product}
        return self.indexs[repeat][cells]

    def get_header(self):
        """Gets the header for the CSV file.

        Returns:
            list: List of header strings.
        """
        header = ['ave']
        for key, value in self.patterns.items():
            header += [key + '-' + str(i) for i in range(3**len(value))]
        return header

    def get_dataset(self, board, score):
        """Generates a dataset from the board and score.

        Args:
            board (list): State of the board.
            score (dict): Dictionary of scores.

        Returns:
            dict: Dictionary representing the dataset.
        """
        dataset = {'ave': score['total'] / score['count']}
        for key, value in self.patterns.items():
            pattern = tuple([board[i] for i in value])
            if key not in dataset:
                dataset[key] = [0 for _ in range(3**len(value))]
            dataset[key][self.to_index(pattern)] = 1
        return dataset

    def to_csv(self, name):
        """Writes the dataset to a CSV file.

        Args:
            name (str): Name of the CSV file.
        """
        with open(name, 'w', newline='') as f:
            w = csv.writer(f)
            header = self.get_header()
            w.writerow(header)
            scores = sorted(self.scores.items(),
                            key=lambda x: x[1]['total'] / x[1]['count'])
            for board, score in scores:
                dataset = self.get_dataset(board, score)
                line = [dataset['ave']]
                for key in self.patterns.keys():
                    line += dataset[key]
                w.writerow(line)


if __name__ == '__main__':
    rand = RandomRecords(o_win=10, x_win=-10, draw=0)  # Set custom weights
    for num in [10, 100, 1000, 10000]:
        name = 'rand' + str(num) + '.csv'
        print(f'\n[{name}]')
        scores = rand.scoring(num)
        patterns = Patterns(scores)
        patterns.to_csv(name)
