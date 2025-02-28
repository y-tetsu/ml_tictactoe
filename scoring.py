from tictactoe import TicTacToe, B, O, X, rand


O_WIN = 10
X_WIN = -10
DRAW = 0


class RandomRecords:
    """Class to handle random records and scoring for TicTacToe games."""

    def __init__(self):
        """Initializes the RandomRecords with a TicTacToe game instance."""
        self.t = TicTacToe(rand, rand)

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
    for key, value in records.scoring(1).items():
        print(key, value)
