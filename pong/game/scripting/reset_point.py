from game.scripting.action import Action
from game.shared.point import Point


class ResetPoint(Action):
# Implement MoveActorsAction class here! 

    # Override the execute(cast, script) method as follows:
    def left(self, cast):
        """Executes the reset actors action.

        Args:
        cast (Cast): The cast of Actors in the game.
        script (Script): The script of Actions in the game.
        """
        paddle1 = cast.get_actors("paddle1")
        paddle2 = cast.get_actors("paddle2")
        ball = cast.get_actors("ball")

        paddle1[0].set_position(Point(15, 260))
        paddle2[0].set_position(Point(885,260))
        ball[0].set_position(Point(30, 280))
        ball[0].set_velocity(Point(8,8))
        
        

    def right(self, cast):
        """Executes the reset actors action.

        Args:
        cast (Cast): The cast of Actors in the game.
        script (Script): The script of Actions in the game.
        """
        paddle1 = cast.get_actors("paddle1")
        paddle2 = cast.get_actors("paddle2")
        ball = cast.get_actors("ball")

        paddle1[0].set_position(Point(14, 260))
        paddle2[0].set_position(Point(886,260))
        ball[0].set_position(Point(870, 280))
        ball[0].set_velocity(Point(8,8))