from tictactoe import TicTacToe
from regression import Regression as r
from user import user

if __name__ == '__main__':
    """Main function to start the Tic Tac Toe game with a regression model."""
    dataset = 'rand10000.csv'
    while True:
        turn = input('select your player O or X > ')
        if turn in ['o', 'x', 'O', 'X']:
            p1, p2 = (user, r(dataset).move) if turn in ['o', 'O'] else (r(dataset).move, user)
            tictactoe = TicTacToe(p1, p2)
            try:
                tictactoe.game()
                input('\n>>> Press enter to start new game')
            except KeyboardInterrupt:
                break
