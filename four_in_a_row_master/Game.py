# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:31:50 2023

@author: QiuYunda
"""
import Board

class Game():
    def __init__(self):
        self.board = Board()
        
    def start_game(self):
        print("Start game!")
        
        while (!self.isOver()):
            # Print board
            print(board)
            
            self.board.play()
    

    def isOver(self):
        return self.board.is_full() and self.is_winning()
    
    

    def is_winning(self, player):
    	# Check horizontal locations for win
    	for c in range(self.width-3):
    		for r in range(self.height):
    			if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == player.symbol:
    				return True

    	# Check vertical locations for win
    	for c in range(self.width):
    		for r in range(self.height-3):
    			if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == player.symbol:
    				return True

    	# Check positively sloped diaganols
    	for c in range(self.width-3):
    		for r in range(self.height-3):
    			if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == player.symbol:
    				return True

    	# Check negatively sloped diaganols
    	for c in range(self.width-3):
    		for r in range(3, self.height):
    			if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == player.symbol:
    				return True    