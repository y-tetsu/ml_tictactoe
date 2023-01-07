from tictactoe import TicTacToe, B, O, X, rand


class RandomRecords:
    def __init__(self, num=1000):
        self.num = num

    def convert(self, board, pairs):
        ret = [B] * 9
        for i, j in pairs:
            ret[i] = board[j]
        return ret

    def scoring(self):
        scores = {}
        t = TicTacToe(rand, rand)
        records = t.simulate(self.num)
        rot0 = [
            (0, 0), (1, 1), (2, 2),  # 0 1 2    0 1 2
            (3, 3), (4, 4), (5, 5),  # 3 4 5 -> 3 4 5
            (6, 6), (7, 7), (8, 8),  # 6 7 8    6 7 8
        ]
        rot90 = [
            (0, 6), (1, 3), (2, 0),  # 0 1 2    6 3 0
            (3, 7), (4, 4), (5, 1),  # 3 4 5 -> 7 4 1
            (6, 8), (7, 5), (8, 2),  # 6 7 8    8 5 2
        ]
        rot180 = [
            (0, 8), (1, 7), (2, 6),  # 0 1 2    8 7 6
            (3, 5), (4, 4), (5, 3),  # 3 4 5 -> 5 4 3
            (6, 2), (7, 1), (8, 0),  # 6 7 8    2 1 0
        ]
        rot270 = [
            (0, 2), (1, 5), (2, 8),  # 0 1 2    2 5 8
            (3, 1), (4, 4), (5, 7),  # 3 4 5 -> 1 4 7
            (6, 0), (7, 3), (8, 6),  # 6 7 8    0 3 6
        ]
        sim0 = [
            (0, 6), (1, 7), (2, 8),  # 0 1 2    6 7 8
            (3, 3), (4, 4), (5, 5),  # 3 4 5 -> 3 4 5
            (6, 0), (7, 1), (8, 2),  # 6 7 8    0 1 2
        ]
        sim45 = [
            (0, 0), (1, 3), (2, 6),  # 0 1 2    0 3 6
            (3, 1), (4, 4), (5, 7),  # 3 4 5 -> 1 4 7
            (6, 2), (7, 5), (8, 8),  # 6 7 8    2 5 8
        ]
        sim90 = [
            (0, 2), (1, 1), (2, 0),  # 0 1 2    2 1 0
            (3, 5), (4, 4), (5, 3),  # 3 4 5 -> 5 4 3
            (6, 8), (7, 7), (8, 6),  # 6 7 8    8 7 6
        ]
        sim135 = [
            (0, 8), (1, 5), (2, 2),  # 0 1 2    8 5 2
            (3, 7), (4, 4), (5, 1),  # 3 4 5 -> 7 4 1
            (6, 6), (7, 3), (8, 0),  # 6 7 8    6 3 0
        ]
        for record in records:
            winner = record.pop(0)
            score = 10 if winner == O else -10 if winner == X else 0
            turn, board = O, [B] * 9
            for move in record:
                board[move] = turn
                variations = [rot0, rot90, rot180, rot270,
                              sim0, sim45, sim90, sim135]
                for pairs in variations:
                    key = tuple(self.convert(board, pairs))
                    if key not in scores:
                        scores[key] = {'total': 0, 'count': 0}
                    scores[key]['total'] += score
                    scores[key]['count'] += 1
                turn = X if turn == O else O
        return scores


if __name__ == '__main__':
    records = RandomRecords(10)
    for key, value in records.scoring().items():
        print(key, value)
