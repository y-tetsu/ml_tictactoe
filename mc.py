from random import choice
from tictactoe import TicTacToe, B, O, X, D, SIZE


def mc(board, turn):
    """Gets the best move based on the Monte Carlo method.

    Args:
        board: List representing the board state.
        turn: The current player's turn.

    Returns:
        int: The position chosen by the algorithm.
    """
    def simulate(board, turn):
        """Simulates a random game from the current board state.

        Args:
            board: List representing the board state.
            turn: The current player's turn.

        Returns:
            int: The winner of the simulated game.
        """
        current_board = board[:]
        current_turn = turn
        while True:
            winner = TicTacToe.judge(current_board)
            if winner != B:
                return winner
            move = choice([i for i, cell in enumerate(current_board) if cell == B])
            current_board[move] = current_turn
            current_turn = X if current_turn == O else O

    blank = [i for i, cell in enumerate(board) if cell == B]
    best_move = None
    best_score = float('-inf')
    for move in blank:
        wins = 0
        for _ in range(100):  # Number of simulations
            board[move] = turn
            if simulate(board, X if turn == O else O) == turn:
                wins += 1
            board[move] = B
        score = wins / 100
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


if __name__ == '__main__':
    from user import user
    while True:
        turn = input('select your player O or X > ')
        if turn in ['o', 'x', 'O', 'X']:
            p1, p2 = (user, mc) if turn in ['o', 'O'] else (mc, user)
            try:
                TicTacToe(p1, p2).game()
                input('\n>>> Press enter to start new game')
            except KeyboardInterrupt:
                break
