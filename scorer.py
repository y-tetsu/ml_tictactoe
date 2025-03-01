from tictactoe import B, O, X, SIZE
from recorder import Recorder


class Scorer:
    """Class to handle scoring for TicTacToe games."""

    def __init__(self, o_win=10, x_win=-10, draw=0):
        """Initializes the Scorer with custom weights.

        Args:
            o_win (int): Weight for O win.
            x_win (int): Weight for X win.
            draw (int): Weight for draw.
        """
        self.o_win = o_win
        self.x_win = x_win
        self.draw = draw

    def scoring(self, records):
        """Calculates scores for each board state from the given records.

        Args:
            records (list): The list of game records.

        Returns:
            dict: A dictionary with board states as keys and their scores as values.
        """
        scores = {}
        for record in records:
            winner = record.pop(0)
            score = self.o_win if winner == O else self.x_win if winner == X else self.draw
            turn, board = O, [B] * SIZE
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
    records = Recorder().get_records(10)
    for key, value in Scorer().scoring(records).items():
        print(key, value)
