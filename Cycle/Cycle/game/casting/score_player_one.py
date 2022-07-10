from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points of player one has earned.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        x = 1
        y = 0
        position = Point(x,y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
         
        self._points += points
        self.set_text(f"Player 1: {self._points}")