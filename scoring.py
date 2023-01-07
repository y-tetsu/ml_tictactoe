from tictactoe import TicTacToe, B, O, X, rand

O_WIN = 10
X_WIN = -10
DRAW = 0


class RandomRecords:
    def __init__(self):
        self.t = TicTacToe(rand, rand)

    def scoring(self, num):
        scores = {}
        records = self.t.simulate(num)
        for record in records:
            winner = record.pop(0)
            score = O_WIN if winner == O else X_WIN if winner == X else DRAW
            turn, board = O, [B] * 9
            for move in record:
                board[move] = turn
                key = tuple(board)
                if key not in scores:
                    scores[key] = {'total': 0, 'count': 0}
                scores[key]['total'] += score
                scores[key]['count'] += 1
                turn = X if turn == O else O
        return scores


if __name__ == '__main__':
    records = RandomRecords()
    for key, value in records.scoring(10).items():
        print(key, value)
