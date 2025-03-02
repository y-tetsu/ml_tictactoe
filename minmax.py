from tictactoe import B, O, X, D, SIZE


def minmax(board, turn):
    """Gets the best move based on the Minimax algorithm.

    Args:
        board: List representing the board state.
        turn: The current player's turn.

    Returns:
        int: The position chosen by the Minimax algorithm.
    """
    def score(board, depth):
        winner = judge(board)
        if winner == O:
            return 10 - depth
        elif winner == X:
            return depth - 10
        elif winner == D:
            return 0
        return None

    def judge(board):
        patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                    (0, 4, 8), (2, 4, 6)]             # diagonal
        for c1, c2, c3 in patterns:
            if board[c1] and board[c1] == board[c2] == board[c3]:
                return board[c1]
        return B if B in board else D

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
            TicTacToe(p1, p2).play()
            break
