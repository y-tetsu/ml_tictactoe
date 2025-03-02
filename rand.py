from random import randint
from tictactoe import B


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
    from tictactoe import TicTacToe
    TicTacToe(rand, rand).game()
