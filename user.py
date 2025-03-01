def user(board, turn):
    """Gets the user's move.

    Args:
        board: List representing the board state.
        turn: The current player's turn.

    Returns:
        int: The position chosen by the user.
    """
    while True:
        try:
            move = int(input('> '))
            if 0 <= move < len(board) and not board[move]:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")


if __name__ == '__main__':
    from tictactoe import TicTacToe
    TicTacToe(user, user).play()
