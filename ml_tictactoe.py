from tictactoe import TicTacToe, user
from regression import Regression


if __name__ == '__main__':
    turn = None
    while True:
        turn = input('select your player O or X > ')
        if turn == 'O' or turn == 'X':
            break
    if turn == 'O':
        TicTacToe(user, Regression('rand10000.csv').move).play()
    else:
        TicTacToe(Regression('rand10000.csv').move, user).play()
