import pandas as pd
from sklearn.linear_model import LinearRegression

from tictactoe import B, O
from dataset import Patterns
from rand import rand


class Regression:
    """Class to represent the regression model for Tic Tac Toe."""

    def __init__(self, csv, show=True):
        """Initializes the Regression class with a CSV file.

        Args:
            csv: Path to the CSV file.
            show: Boolean to indicate whether to print debug information.
        """
        dataset = pd.read_csv(csv)
        dataset_except_ave = dataset.drop('ave', axis=1)
        x = dataset_except_ave.values
        y = dataset['ave'].values
        self.model = LinearRegression()
        self.model.fit(x, y)
        self.p = Patterns(None)
        self.show = show

    def _print(self, *args):
        """Prints debug information if show is True.

        Args:
            *args: Arguments to print.
        """
        if self.show:
            print(*args)

    def to_x(self, board):
        """Converts the board state to a feature vector.

        Args:
            board: List representing the board state.

        Returns:
            list: Feature vector representing the board state.
        """
        x = []
        for key, value in self.p.patterns.items():
            state = tuple([board[i] for i in value])
            patterns = [0 for _ in range(3**len(value))]
            patterns[self.p.to_index(state)] = 1
            x += patterns
        return [x]

    def move(self, board, turn):
        """Gets the best move based on the regression model.

        Args:
            board: List representing the board state.
            turn: The current player's turn.

        Returns:
            int: The position chosen by the regression model.
        """
        blank = [i for i, cell in enumerate(board) if cell == B]
        index, score = None, 0
        self._print()
        for i in blank:
            board[i] = turn
            predict = self.model.predict(self.to_x(board))[0]
            cond = predict > score if turn == O else predict < score
            if index is None or cond:
                index, score = i, predict
            self._print(i, '=', predict)
            board[i] = B
        self._print('move :', index)
        return index


if __name__ == '__main__':
    from recorder import Recorder
    num = 1000
    for csv in ['rand10.csv', 'rand100.csv', 'rand1000.csv', 'rand10000.csv']:
        regression = Regression(csv, show=False).move
        print(f'\n[{csv}]')
        print('--- O ---')
        Recorder(regression, rand).get_records(num)
        print('--- X ---')
        Recorder(rand, regression).get_records(num)
