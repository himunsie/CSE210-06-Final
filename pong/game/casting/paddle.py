from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Paddle(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Paddle.
        
        Args:Args:
            body: A new instance of Body.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation #Do we need this?

    def get_animation(self): #Does the paddle have animation???
        """Gets the paddles's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the paddle's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the paddle using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_up(self):
        """Moves the paddle up"""
        
        velocity = Point(-PADDLE_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_down(self):
        """Moves the paddle down"""
        
        velocity = Point(PADDLE_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the paddle from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)