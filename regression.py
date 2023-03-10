import pandas as pd
from sklearn.linear_model import LinearRegression

from tictactoe import TicTacToe, B, O, rand
from dataset import Patterns


class Regression:
    def __init__(self, csv, show=True):
        dataset = pd.read_csv(csv)
        dataset_except_ave = dataset.drop('ave', axis=1)
        x = dataset_except_ave.values
        y = dataset['ave'].values
        self.model = LinearRegression()
        self.model.fit(x, y)
        self.p = Patterns(None)
        self.show = show

    def _print(self, *args):
        if self.show:
            print(*args)

    def to_x(self, board):
        x = []
        for key, value in self.p.patterns.items():
            state = tuple([board[i] for i in value])
            patterns = [0 for _ in range(3**len(value))]
            patterns[self.p.to_index(state)] = 1
            x += patterns
        return [x]

    def move(self, board, turn):
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
    num = 1000
    for name in ['rand10.csv', 'rand100.csv', 'rand1000.csv', 'rand10000.csv']:
        model = Regression(name, show=False)
        print(f'\n[{name}]')
        print('--- O ---')
        TicTacToe(model.move, rand).simulate(num)
        print('--- X ---')
        TicTacToe(rand, model.move).simulate(num)
