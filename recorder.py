from tictactoe import TicTacToe
from rand import rand


class Recorder:
    """Class to handle random records and scoring for TicTacToe games."""

    def __init__(self, player1=rand, player2=rand):
        """Initializes the Recorder with a TicTacToe game instance and custom weights.

        Args:
            player1 (callable): Function to determine player 1's moves.
            player2 (callable): Function to determine player 2's moves.
        """
        self.tictactoe = TicTacToe(player1, player2)

    def get_records(self, num):
        """Simulates games and returns the records.

        Args:
            num (int): The number of games to simulate.

        Returns:
            list: A list of game records.
        """
        count, winner, records = 0, [0 for _ in range(len([0, 1, 2, 3]))], []
        while count < num:
            record = self.tictactoe.game(show=False)
            records.append(record)
            winner[record[0]] += 1
            count += 1
        print(f'O = {winner[1]} / {num} ({winner[1] / num * 100:.1f}%)')
        print(f'X = {winner[2]} / {num} ({winner[2] / num * 100:.1f}%)')
        print(f'D = {winner[3]} / {num} ({winner[3] / num * 100:.1f}%)')
        return records


if __name__ == '__main__':
    print(Recorder().get_records(5))
