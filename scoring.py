from tictactoe import TicTacToe, B, O, X, rand


class RandomRecords:
    def __init__(self):
        self.t = TicTacToe(rand, rand)

    def scoring(self, num):
        scores = {}
        records = self.t.simulate(num)
        for record in records:
            winner = record.pop(0)
            score = 10 if winner == O else -10 if winner == X else 0
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
