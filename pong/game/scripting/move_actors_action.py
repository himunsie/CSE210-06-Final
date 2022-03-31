import constants 
from game.casting.point import Point
from game.scripting.action import Action

class MoveActorsAction(Action):
# Implement MoveActorsAction class here! 
    def __init__(self):
        pass
    
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
        cast (Cast): The cast of Actors in the game.
        script (Script): The script of Actions in the game.
        """
        ball = cast.get_first_actor("ball")
        position = ball.get_position()
        velocity = ball.get_velocity()
        position = position.add(velocity)
        ball.set_position(position)

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