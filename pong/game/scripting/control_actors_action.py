import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        paddle1 = cast.get_first_actor("paddle1")
        # # up
        if self._keyboard_service.is_key_down('a'):
            paddle1.move_up()
           
        
        # # down
        elif self._keyboard_service.is_key_down('z'):
            paddle1.move_down()
            
        else:
            paddle1.stop_moving()
        
        paddle2 = cast.get_first_actor("paddle2")
        # # up
        if self._keyboard_service.is_key_down('k'):
            paddle2.move_up()
            
        
        # # down
        elif self._keyboard_service.is_key_down('m'):
            paddle2.move_down()
           
        else:
            paddle2.stop_moving()