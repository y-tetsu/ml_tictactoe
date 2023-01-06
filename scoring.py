from tictactoe import TicTacToe, B, O, X, rand


class RandomRecords:
    def __init__(self, num=1000):
        self.num = num

    def scoring(self):
        scores = {}
        t = TicTacToe(rand, rand)
        records = t.simulate(self.num)
        for record in records:
            winner = record.pop(0)
            score = 10 if winner == O else -10 if winner == X else 0
            turn, board = O, [B] * 9
            for move in record:
                board[move] = turn
                funcs = [list, rot90, rot180, rot270,
                         sym0, sym45, sym90, sym135]
                for func in funcs:
                    key = tuple(func(board))
                    if key not in scores:
                        scores[key] = {'total': 0, 'count': 0}
                    scores[key]['total'] += score
                    scores[key]['count'] += 1
                turn = X if turn == O else O
        return scores


# 0 1 2    6 3 0
# 3 4 5 -> 7 4 1
# 6 7 8    8 5 2
def rot90(board):
    ret = [B] * 9
    ret[0] = board[6]
    ret[1] = board[3]
    ret[2] = board[0]
    ret[3] = board[7]
    ret[4] = board[4]
    ret[5] = board[1]
    ret[6] = board[8]
    ret[7] = board[5]
    ret[8] = board[2]
    return ret


# 0 1 2    8 7 6
# 3 4 5 -> 5 4 3
# 6 7 8    2 1 0
def rot180(board):
    ret = [B] * 9
    ret[0] = board[8]
    ret[1] = board[7]
    ret[2] = board[6]
    ret[3] = board[5]
    ret[4] = board[4]
    ret[5] = board[3]
    ret[6] = board[2]
    ret[7] = board[1]
    ret[8] = board[0]
    return ret


# 0 1 2    2 5 8
# 3 4 5 -> 1 4 7
# 6 7 8    0 3 6
def rot270(board):
    ret = [B] * 9
    ret[0] = board[2]
    ret[1] = board[5]
    ret[2] = board[8]
    ret[3] = board[1]
    ret[4] = board[4]
    ret[5] = board[7]
    ret[6] = board[0]
    ret[7] = board[3]
    ret[8] = board[6]
    return ret


# 0 1 2    6 7 8
# 3 4 5 -> 3 4 5
# 6 7 8    0 1 2
def sym0(board):
    ret = [B] * 9
    ret[0] = board[6]
    ret[1] = board[7]
    ret[2] = board[8]
    ret[3] = board[3]
    ret[4] = board[4]
    ret[5] = board[5]
    ret[6] = board[0]
    ret[7] = board[1]
    ret[8] = board[2]
    return ret


# 0 1 2    0 3 6
# 3 4 5 -> 1 4 7
# 6 7 8    2 5 8
def sym45(board):
    ret = [B] * 9
    ret[0] = board[0]
    ret[1] = board[3]
    ret[2] = board[6]
    ret[3] = board[1]
    ret[4] = board[4]
    ret[5] = board[7]
    ret[6] = board[2]
    ret[7] = board[5]
    ret[8] = board[8]
    return ret


# 0 1 2    2 1 0
# 3 4 5 -> 5 4 3
# 6 7 8    8 7 6
def sym90(board):
    ret = [B] * 9
    ret[0] = board[2]
    ret[1] = board[1]
    ret[2] = board[0]
    ret[3] = board[5]
    ret[4] = board[4]
    ret[5] = board[3]
    ret[6] = board[8]
    ret[7] = board[7]
    ret[8] = board[6]
    return ret


# 0 1 2    8 5 2
# 3 4 5 -> 7 4 1
# 6 7 8    6 3 0
def sym135(board):
    ret = [B] * 9
    ret[0] = board[8]
    ret[1] = board[5]
    ret[2] = board[2]
    ret[3] = board[7]
    ret[4] = board[4]
    ret[5] = board[1]
    ret[6] = board[6]
    ret[7] = board[3]
    ret[8] = board[0]
    return ret


if __name__ == '__main__':
    records = RandomRecords(10)
    for key, value in records.scoring().items():
        print(key, value)
