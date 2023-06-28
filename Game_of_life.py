"""
This is an experiment in using GitHub Copilot, by testing how quickly I can
make a module that plays Conway's Game of Life on a toroidal grid. It prints
the board out using spaces to denote dead squares and asterisks to denote live
ones.
"""

import numpy as np
import time

def iterate(board):
    rows, cols = board.shape
    new_board = np.zeros(board.shape, dtype=int)
    neighbours_sum = np.zeros(board.shape, dtype=int)
    neighbours_sum += np.roll(board, 1, axis=0)
    neighbours_sum += np.roll(board, -1, axis=0)
    neighbours_sum += np.roll(board, 1, axis=1)
    neighbours_sum += np.roll(board, -1, axis=1)
    neighbours_sum += np.roll(np.roll(board, 1, axis=0), 1, axis=1)
    neighbours_sum += np.roll(np.roll(board, 1, axis=0), -1, axis=1)
    neighbours_sum += np.roll(np.roll(board, -1, axis=0), 1, axis=1)
    neighbours_sum += np.roll(np.roll(board, -1, axis=0), -1, axis=1)
    new_board[(board == 1) & (neighbours_sum == 2)] = 1
    new_board[(board == 1) & (neighbours_sum == 3)] = 1
    new_board[(board == 0) & (neighbours_sum == 3)] = 1
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
        time.sleep(0.4)
        print_board(board)
        board = iterate(board)
    return

def generate_glider(rows, cols):
    board = np.zeros((rows, cols), dtype=int)
    board[0, 2] = 1
    board[1, 3] = 1
    board[2, 1:4] = 1
    return board