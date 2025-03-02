from tictactoe import TicTacToe, B, O, X, D, SIZE


def minmax(board, turn):
    """Gets the best move based on the Minimax algorithm.

    Args:
        board: List representing the board state.
        turn: The current player's turn.

    Returns:
        int: The position chosen by the Minimax algorithm.
    """
    def score(board, depth):
        winner = TicTacToe.judge(board)
        if winner == O:
            return 10 - depth
        elif winner == X:
            return depth - 10
        elif winner == D:
            return 0
        return None

    def minimax(board, depth, is_maximizing):
        if (s := score(board, depth)) is not None:
            return s

        if is_maximizing:
            best_score = float('-inf')
            for i in range(SIZE):
                if board[i] == B:
                    board[i] = O
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i] = B
            return best_score
        else:
            best_score = float('inf')
            for i in range(SIZE):
                if board[i] == B:
                    board[i] = X
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i] = B
            return best_score

    best_move = None
    best_score = float('-inf') if turn == O else float('inf')
    for i in range(SIZE):
        if board[i] == B:
            board[i] = turn
            current_score = minimax(board, 0, turn == X)
            board[i] = B
            if (turn == O and current_score > best_score) or (turn == X and current_score < best_score):
                best_score = current_score
                best_move = i
    return best_move


if __name__ == '__main__':
    from tictactoe import TicTacToe
    from user import user
    while True:
        turn = input('select your player O or X > ')
        if turn in ['o', 'x', 'O', 'X']:
            p1, p2 = (user, minmax) if turn in ['o', 'O'] else (minmax, user)
            try:
                TicTacToe(p1, p2).game()
                input('\n>>> Press enter to start new game')
            except KeyboardInterrupt:
                break
