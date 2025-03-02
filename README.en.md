# ml_tictactoe
Creating a Tic Tac Toe AI using Multiple Linear Regression

[English](README.en.md) | [日本語](README.md)

## Overview
This project creates an AI to play the Tic Tac Toe game using multiple linear regression. The AI converts the board state into a feature vector and uses a linear regression model to select the optimal move.

## File Structure
- `ml_tictactoe.py`: Main file to start the Tic Tac Toe game using the regression model.
- `tictactoe.py`: Implements the game logic for Tic Tac Toe. Includes constants `WIDTH` for the board width and `SIZE` for the number of cells.
- `user.py`: Implements a function to handle user input.
- `rand.py`: Implements a function to generate random moves.
- `minmax.py`: Implements a function to determine moves using the Minimax algorithm.
- `mc.py`: Implements a function to determine moves using the Monte Carlo method.
- `recorder.py`: Implements a class to handle game records.
- `scorer.py`: Implements a class to handle game scoring.
- `regression.py`: Implements a class to select the optimal move using a linear regression model.
- `dataset.py`: Manages board patterns and generates datasets.
- `README.md`: This project's description in Japanese.
- `README.en.md`: This project's description in English.

## Usage
1. Install the required libraries.
    ```sh
    pip install pandas scikit-learn
    ```

2. Create the training data (generated from random moves).
    ```sh
    python dataset.py
    ```

3. Run `ml_tictactoe.py` to start the Tic Tac Toe game using the regression model.
    ```sh
    python ml_tictactoe.py
    ```

## Link
For a detailed explanation, please refer to the following article:
https://qiita.com/y-tetsu/items/8fcacea73d58ab692196
