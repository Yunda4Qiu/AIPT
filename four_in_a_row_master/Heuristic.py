# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:49:39 2023

@author: QiuYunda
"""


class Heuristic():
    def __init__(self, gameN):
        self.gameN = gameN
        self.evalCount = 0


    def evaluate(self, player, board):
        pass

    def get_eval_count(self):
        return self.evalCount

    def get_best_action(self, player, board):
        utilities = self.eval_actions(player, board)
        best_action = 0
        for i in range(len(utilities)):
            if utilities[i] > utilities[best_action]:
                best_action = i
        return best_action

    def eval_actions(self, player, board):
        utilities = [0] * board.width
        for i in range(board.width):
            utilities[i] = self.evaluate_action(player, i, board)
        return utilities

    def evaluate_action(self, player, action, board):
        if board.is_valid(action):
            self.evalCount += 1
            value = self.evaluate(player, board.get_new_board(action, player))
            return value
        else:
            return float('-inf')

    def evaluate_board(self, player, board):
        self.evalCount += 1
        return self.evaluate(player, board)

    def __str__(self):
        return self.name()

