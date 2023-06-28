"""
This is an experiment in using GitHub Copilot, by testing how quickly I can
make a module that plays Conway's Game of Life, using spaces to denote dead
squares and asterisks to denote live ones.
"""

import numpy as np

def iterate(board):
    rows, cols = board.shape
    new_board = np.zeros(board.shape, dtype=int)
    for i in range(rows):
        for j in range(cols):
            neighbors = board[max(0, i-1):min(rows, i+2),
                              max(0, j-1):min(cols, j+2)]
            neighbors_sum = np.sum(neighbors) - board[i, j]
            if board[i, j] == 1:
                if neighbors_sum in (2, 3):
                    new_board[i, j] = 1
            else:
                if neighbors_sum == 3:
                    new_board[i, j] = 1
    return new_board

def print_board(board):
    for row in board:
        for z in row:
            if z == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    return

def play_game(board, steps):
    for i in range(steps):
        print_board(board)
        board = iterate(board)
    return

def generate_glider(rows, cols):
    board = np.zeros((rows, cols), dtype=int)
    board[0, 2] = 1
    board[1, 3] = 1
    board[2, 1:4] = 1
    return board