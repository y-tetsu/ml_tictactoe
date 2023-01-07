from random import randint


B = 0
O = 1
X = 2
D = 3
KEY = ' OX'


class TicTacToe:
    def __init__(self, player1, player2):
        self.put = {O: player1, X: player2}

    def show(self, board):
        print()
        for i in range(3):
            print(' ' + '|'.join([KEY[board[i * 3 + j]] for j in range(3)]))
            if i < 2:
                print(' -+-+-')
        print()

    def judge(self, board):
        patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                    (0, 4, 8), (2, 4, 6)]             # diagonal
        for c1, c2, c3 in patterns:
            if board[c1] and board[c1] == board[c2] == board[c3]:
                return board[c1]
        if B not in board:
            return D
        return B

    def play(self):
        try:
            while True:
                turn, board = O, [B for _ in range(9)]
                while True:
                    self.show(board)
                    if winner := self.judge(board):
                        if winner == D:
                            print('--- Draw ---')
                        else:
                            print(f'*** {KEY[winner]} win!! ***')
                        input('\n>>> Press enter to start new game')
                        break
                    print(f'turn : {KEY[turn]}')
                    move = self.put[turn](board, turn)
                    board[move] = turn
                    turn = X if turn == O else O

        except KeyboardInterrupt:
            pass

    def simulate(self, num=100):
        count, ret, records = 0, [0 for _ in range(4)], []
        while True:
            turn, board, record = O, [B for _ in range(9)], []
            while True:
                if winner := self.judge(board):
                    ret[winner] += 1
                    count += 1
                    records += [[winner] + record]
                    break
                move = self.put[turn](board, turn)
                board[move] = turn
                record += [move]
                turn = X if turn == O else O
            if count >= num:
                print(f'O = {ret[O]}/{num} ({ret[O]/num*100:.1f}%)')
                print(f'X = {ret[X]}/{num} ({ret[X]/num*100:.1f}%)')
                print(f'D = {ret[D]}/{num} ({ret[D]/num*100:.1f}%)')
                break
        return records


def user(board, turn):
    while True:
        try:
            move = int(input('> '))
            if move < len(board) and not board[move]:
                return move
        except ValueError:
            pass


def rand(board, turn):
    blank = [i for i, cell in enumerate(board) if cell == B]
    rand_index = randint(0, len(blank) - 1)
    return blank[rand_index]


if __name__ == '__main__':
    tictactoe = TicTacToe(rand, rand)
    for record in tictactoe.simulate(10):
        print(record)
    tictactoe.play()
