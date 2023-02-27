# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:54:33 2023

@author: QiuYunda
"""
import Player
import Board

class HumanPlayer(Player):
    def __init__(self, playerID, symbol, heuristic):
        super().__init__(playerID, symbol)
        self.heuristic = heuristic
    
    def play(self):
        if (self.heuristic):
            print("Heuristic: " + heuristic + " calculated the best move is: " 
                  + (heuristic.getBestAction(playerId, board) + 1));
        
        print(f"Player {self.symbol}")
        column = input("Which column would you like to play in? ")
        
        return column - 1
    
        
    