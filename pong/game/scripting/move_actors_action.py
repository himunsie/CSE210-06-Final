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