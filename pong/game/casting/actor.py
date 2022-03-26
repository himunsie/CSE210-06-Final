import constants
from game.shared.color import Color
from game.shared.point import Point


class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.
    Stereotype:
        Information Holder
    Attributes:
        _tag (string): The actor's tag.
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self, position = Point(), size = Point(), velocity = Point()):
        """The Class constructor"""
        self._position = position
        self._size = size
        self._velocity = velocity
    
    def get_position(self):
        """Gets the Actors position.
        
        Returns:
            An instance of Point containing the x and y coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the actor's size.
        
        Returns:
            An instance of Point containing the width and height.
        """
        return self._size

    def get_velocity(self):
        """Gets the actor's velocity.
        
        Returns:
            An instance of Point containing the horizontal and vertical speed.
        """
        return self._velocity

    # def get_rectangle(self):
    #     """Gets the rectangle enclosing the body.
        
    #     Returns:
    #         An instance of Rectangle.
    #     """
    #     return Rectangle(self._position, self._size)
        
    def set_position(self, position):
        """Sets the position to the given value.
        
        Args:
            position: An instance of Point.
        """
        self._position = position

    def set_size(self, size):
        """Sets the size to the given value.
        
        Args:
            size: An instance of Point.
        """
        self._size = size

    def set_velocity(self, velocity):
        """Sets the velocity to the given value.
        
        Args:
            velocity: An instance of Point.
        """
        self._velocity = velocity