# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:52:30 2023

@author: QiuYunda
"""

import numpy as np


class Board():
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.reset_board()
        
    def reset_board(self):
        self.board = np.zeros((self.height, self.width))
        
    def __str__(self):
        s = ""
        s_dash = " ---" * 7
        s += s_dash
        s += "\n"
        for row in range(self.height-1, -1, -1):
            for col in range(self.width):
                if col < self.width - 1:
                    if self.board[row][col] == 0:
                        s += "|   "
                    else:
                        s += "| " + str(int(self.board[row][col])) + " "
                else:
                    if self.board[row][col] == 0:
                        s += "|   |"
                    else:
                        s += "| " + str(int(self.board[row][col])) + " |"
            s += "\n"
            if row > 0:
                s += s_dash
                s += "\n"
        s_two_dash = " ===" * 7
        s += s_two_dash
        s += "\n"
        s_col = "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |"
        s += s_col
        
        return s


    def play(self, row, col, playerID):
        self.board[row][col] = playerID.symbol
    
    def is_valid_column(self, col):
        return self.board[self.height-1][col] == 0
    
    def select_next_row(self, col):
        for row in range(self.height):
            if self.board[row][col] == 0:
                return row
            
    def is_full(self):
        for row in range(self.board):
            if 0 in row:
                return False
        return True
                
  
    


if __name__ == "__main__":
    board = Board()
    # Print a new board
    print(board)
    
    # Print the board
    board.board[0][4] = 3
    print(board)