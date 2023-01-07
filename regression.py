import pandas as pd
from sklearn.linear_model import LinearRegression

from tictactoe import TicTacToe, B, O, rand, user
from dataset import Patterns


class Regression:
    def __init__(self, csv, show=True):
        dataset = pd.read_csv(csv)
        dataset_except_rate = dataset.drop('rate', axis=1)
        x = dataset_except_rate.values
        y = dataset['rate'].values
        self.model = LinearRegression()
        self.model.fit(x, y)
        self.p = Patterns(None)
        self.show = show

    def get_pattern(self, board):
        dataset = []
        for key, value in self.p.patterns.items():
            pattern = tuple([board[i] for i in value])
            data = [0 for _ in range(3**len(value))]
            data[self.p.to_index(pattern)] = 1
            dataset += data
        return [dataset]

    def put(self, board, turn):
        blank = [i for i, cell in enumerate(board) if cell == B]
        index, score = None, 0
        if self.show:
            print()
        for i in blank:
            board[i] = turn
            predict = self.model.predict(self.get_pattern(board))[0]
            cond = predict > score if turn == O else predict < score
            if index is None or cond:
                index, score = i, predict
            if self.show:
                print(i, '=', predict)
            board[i] = B
        if self.show:
            print('put :', index)
        return index


if __name__ == '__main__':
    num = 1000
    for name in ['rand10.csv', 'rand100.csv', 'rand1000.csv']:
        model = Regression(name, show=False)
        print(f'\n[{name}]')
        print('--- O ---')
        TicTacToe(model.put, rand).simulate(num)
        print('--- X ---')
        TicTacToe(rand, model.put).simulate(num)