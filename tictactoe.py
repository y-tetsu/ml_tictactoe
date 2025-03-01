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
        self.reset()

    def reset(self):
        """Resets the game state."""
        self.turn = O
        self.board = [B for _ in range(9)]
        self.record = []

    def display(self):
        """Displays the current state of the board."""
        print('\n' + '\n -+-+-\n'.join(
            ' ' + '|'.join(KEY[self.board[i * 3 + j]] for j in range(3)) for i in range(3)
        ) + '\n')

    def judge(self):
        """Judges the current state of the board.

        Returns:
            int: The winner (O or X), D for draw, or B for ongoing game.
        """
        patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                    (0, 4, 8), (2, 4, 6)]             # diagonal
        for c1, c2, c3 in patterns:
            if self.board[c1] and self.board[c1] == self.board[c2] == self.board[c3]:
                return self.board[c1]
        return B if B in self.board else D

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
            if winner := self.judge():
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

    def play(self):
        """Starts the Tic Tac Toe game for two players."""
        try:
            while True:
                self.game()
                input('\n>>> Press enter to start new game')

        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    from rand import rand
    TicTacToe(rand, rand).play()
