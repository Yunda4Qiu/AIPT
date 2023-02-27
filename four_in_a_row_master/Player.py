# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:53:00 2023

@author: QiuYunda
"""

class Player:
    """
    The `Player` class represents a player in a game.

    Args:
        symbol (str): The symbol used to represent the player on the game board.

    Methods:
        set_name(): A method that sets the name of the player. 
        Must be implemented by a subclass.
        get_name(): A method that returns the name of the player.
        __str__(): A method that returns the string representation of the player (i.e., the symbol).
        __eq__(other): A method that returns True 
        if the `other` object is an instance of the `Player` class 
        and has the same symbol as the current player.
    """
    # The constructor
    def __init__(self, playerID, symbol):
        """
        The constructor of the 'Player' class.

        Args:
            symbol (str): a choice from "x", "o".

        Returns:
            None
        """
        self.ID = playID
        self.symbol = symbol
        self.set_name()

    def set_name(self):
        """
        An empty method for the interface class to set players' name.
        
        Returns:
            None.
        """
        pass

    def get_name(self):
        """
        Get the name of the player.
        
        Returns:
            (str): The name of the player.
        """
        return self.name

    def __str__(self):
        """
        Return the symbol representation of the player.
        
        Returns:
            (str): The symbol representation of the player.
        """
        return f"{self.symbol}"
    
    def __eq__(self, other):
        """
        Compare two player objects based on their symbols.
        
        Args:
            other (Player): The other player to compare to.
        
        Returns:
            (bool): True if the symbols of the players are equal, 
            False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False
        return self.symbol == other.symbol
    