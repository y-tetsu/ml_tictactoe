B = 0
O = 1
X = 2
D = 3
KEY = ' OX'
WIDTH = 3
SIZE = WIDTH * WIDTH


class TicTacToe:
    """Class to represent the Tic Tac Toe game."""

    def __init__(self, player1, player2):
        """Initializes the TicTacToe class with two players.

        Args:
            player1: Function representing player 1's move.
            player2: Function representing player 2's move.
        """
        self.move = {O: player1, X: player2}
        self.reset()

    def reset(self):
        """Resets the game state."""
        self.turn = O
        self.board = [B for _ in range(SIZE)]
        self.record = []

    def display(self):
        """Displays the current state of the board."""
        print('\n' + '\n -+-+-\n'.join(
            ' ' + '|'.join(KEY[self.board[i * WIDTH + j]] for j in range(WIDTH)) for i in range(WIDTH)
        ) + '\n')

    @staticmethod
    def judge(board):
        """Judges the current state of the board.

        Args:
            board (list): List representing the board state.

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

    def game(self, show=True):
        """Plays a single game of Tic Tac Toe.

        Args:
            show (bool): Whether to display the game board.

        Returns:
            list: Record of moves and the winner.
        """
        self.reset()
        while True:
            if show:
                self.display()
            if winner := self.judge(self.board):
                if show:
                    if winner == D:
                        print('--- Draw ---')
                    else:
                        print(f'*** {KEY[winner]} win!! ***')
                self.record = [winner] + self.record
                break
            if show:
                print(f'turn : {KEY[self.turn]}')
            move = self.move[self.turn](self.board, self.turn)
            self.board[move] = self.turn
            self.record.append(move)
            self.turn = X if self.turn == O else O
        return self.record


if __name__ == '__main__':
    from rand import rand
    tictactoe = TicTacToe(rand, rand)
    try:
        while True:
            tictactoe.game()
            input('\n>>> Press enter to start new game')
    except KeyboardInterrupt:
        pass
