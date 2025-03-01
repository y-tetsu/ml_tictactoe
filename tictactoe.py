from random import randint


B = 0
O = 1
X = 2
D = 3
KEY = ' OX'


class TicTacToe:
    """Class to represent the Tic Tac Toe game."""

    def __init__(self, player1, player2):
        """Initializes the TicTacToe class with two players.

        Args:
            player1: Function representing player 1's move.
            player2: Function representing player 2's move.
        """
        self.move = {O: player1, X: player2}

    def show(self, board):
        """Displays the current state of the board.

        Args:
            board: List representing the board state.
        """
        print('\n' + '\n -+-+-\n'.join(
            ' ' + '|'.join(KEY[board[i * 3 + j]] for j in range(3)) for i in range(3)
        ) + '\n')

    def judge(self, board):
        """Judges the current state of the board.

        Args:
            board: List representing the board state.

        Returns:
            int: The winner (O or X), D for draw, or B for ongoing game.
        """
        patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                    (0, 4, 8), (2, 4, 6)]             # diagonal
        for c1, c2, c3 in patterns:
            if board[c1] and board[c1] == board[c2] == board[c3]:
                return board[c1]
        return B if B in board else D

    def play(self):
        """Starts the Tic Tac Toe game for two players."""
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
                    move = self.move[turn](board, turn)
                    board[move] = turn
                    turn = X if turn == O else O

        except KeyboardInterrupt:
            pass

    def simulate(self, num=100):
        """Simulates multiple games of Tic Tac Toe.

        Args:
            num: Number of games to simulate.

        Returns:
            list: List of game records.
        """
        count, ret, records = 0, [0 for _ in range(4)], []
        while count < num:
            turn, board, record = O, [B for _ in range(9)], []
            while True:
                if winner := self.judge(board):
                    ret[winner] += 1
                    count += 1
                    records.append([winner] + record)
                    break
                move = self.move[turn](board, turn)
                board[move] = turn
                record.append(move)
                turn = X if turn == O else O
        print(f'O = {ret[O]} / {num} ({ret[O] / num * 100:.1f}%)')
        print(f'X = {ret[X]} / {num} ({ret[X] / num * 100:.1f}%)')
        print(f'D = {ret[D]} / {num} ({ret[D] / num * 100:.1f}%)')
        return records


def rand(board, turn):
    """Gets a random move.

    Args:
        board: List representing the board state.
        turn: The current player's turn.

    Returns:
        int: The position chosen randomly.
    """
    blank = [i for i, cell in enumerate(board) if cell == B]
    rand_index = randint(0, len(blank) - 1)
    return blank[rand_index]


if __name__ == '__main__':
    tictactoe = TicTacToe(rand, rand)
    for record in tictactoe.simulate(10):
        print(record)
    tictactoe.play()
