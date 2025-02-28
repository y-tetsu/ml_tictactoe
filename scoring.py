from tictactoe import TicTacToe, B, O, X, rand


class RandomRecords:
    """Class to handle random records and scoring for TicTacToe games."""

    def __init__(self, o_win=10, x_win=-10, draw=0):
        """Initializes the RandomRecords with a TicTacToe game instance and custom weights.

        Args:
            o_win (int): Weight for O win.
            x_win (int): Weight for X win.
            draw (int): Weight for draw.
        """
        self.t = TicTacToe(rand, rand)
        self.o_win = o_win
        self.x_win = x_win
        self.draw = draw

    def scoring(self, num):
        """Simulates games and calculates scores for each board state.

        Args:
            num (int): The number of games to simulate.

        Returns:
            dict: A dictionary with board states as keys and their scores as values.
        """
        scores = {}
        records = self.t.simulate(num)
        for record in records:
            winner = record.pop(0)
            score = self.o_win if winner == O else self.x_win if winner == X else self.draw
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
    for key, value in records.scoring(1).items():
        print(key, value)
