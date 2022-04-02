import constants 
from game.casting.point import Point
from game.scripting.action import Action

class MoveActorsAction(Action):
# Implement MoveActorsAction class here! 
    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
    
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
        cast (Cast): The cast of Actors in the game.
        script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._move_ball(cast)
            self._move_paddles(cast)

    def _move_ball(self, cast):
        ball = cast.get_first_actor("ball")
        position = ball.get_position()
        velocity = ball.get_velocity()
        position = position.add(velocity)
        ball.set_position(position)

    def _move_paddles(self, cast):    
        #move paddle 1     
        paddle1 = cast.get_first_actor("paddle1")

        velocity = paddle1.get_velocity()
        position = paddle1.get_position()
        y = position.get_y()
        
        position = position.add(velocity)

        paddle_limit  = constants.SCREEN_HEIGHT - 60

        if y < 0:
            position = Point(position.get_x(), 0)
        elif y > (paddle_limit):
            position = Point(position.get_x(), paddle_limit)
            
        paddle1.set_position(position)
        #move paddle 2
        paddle2 = cast.get_first_actor("paddle2")
        
        velocity = paddle2.get_velocity()
        position = paddle2.get_position()
        y = position.get_y()
        
        position = position.add(velocity)

        if y < 0:
            position = Point(position.get_x(), 0)
        elif y > (paddle_limit):
            position = Point(position.get_x(), paddle_limit)
            
        paddle2.set_position(position)