import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when 
    the cycles collide with its segments, or they run into the other cycles segments,
    or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self.grow_tail_player_one(cast)
            self.grow_tail_player_two(cast)
            self._handle_segment_collision(cast)
            self._handle_player_collision(cast)
            self._handle_game_over(cast)

    def grow_tail_player_one(self, cast):
        point = 1
        cycle_one = cast.get_first_actor("cycle_ones")
        cycle_one.grow_tail(point)
        
    def grow_tail_player_two(self, cast):
        point = 1
        cycle_two = cast.get_first_actor("cycles_two")
        cycle_two.grow_tail(point)
        
        
        
        
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if player one collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score_two = cast.get_first_actor("score_twos")
        score = cast.get_first_actor("scores")
        cycle_one = cast.get_first_actor("cycle_ones")
        cycle_two = cast.get_first_actor("cycles_two")
        head_1 = cycle_one.get_head()
        head_2 = cycle_two.get_head()
        segments = cycle_one.get_segments()[1:]
        segments_twos = cycle_two.get_segments()[1:]
        
        for segment in segments:
            if head_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                point = -1
                score.add_points(point)
                
        for segment in segments_twos:
            if head_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                point = -1
                score_two.add_points(point)
                
    def _handle_player_collision(self, cast):
        """Sets the game over flag if a player collides with another players segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score_two = cast.get_first_actor("score_twos")
        score = cast.get_first_actor("scores")
        cycle_one = cast.get_first_actor("cycle_ones")
        cycle_two = cast.get_first_actor("cycles_two")
        head_1 = cycle_one.get_head()
        head_2 = cycle_two.get_head()
        segments = cycle_one.get_segments()[1:]
        segments_twos = cycle_two.get_segments()[1:]
        
        for segment in segments:
            if head_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                point = 1
                score.add_points(point)
                
        for segment in segments_twos:
            if head_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                point = 1
                score_two.add_points(point)
                
    
                
                
    
                
                
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns both cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_ones")
            cycle_two = cast.get_first_actor("cycles_two")
            segments = cycle_one.get_segments()
            segment_two = cycle_two.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segment_two:
                segment.set_color(constants.WHITE)
            