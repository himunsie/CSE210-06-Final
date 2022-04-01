import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.reset_set import ResetActors
from game.scripting.reset_point import ResetPoint
from game.casting.score import Score
from game.casting.sound import Sound



#from game.services.audio_service import AudioService
# from game.scripting.restart_game import execute

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        
        #self._audio_service = audio_service   

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ball = cast.get_first_actor("ball")
        positionball = ball.get_position()
        xball = positionball.get_x()
        yball = positionball.get_y()
        paddle1 = cast.get_first_actor("paddle1")
        position_paddle1 = paddle1.get_position()
        xpaddle1 = position_paddle1.get_x()
        ypaddle1 = position_paddle1.get_y()
        paddle2 = cast.get_first_actor("paddle2")
        position_paddle2 = paddle2.get_position()
        xpaddle2 = position_paddle2.get_x()
        ypaddle2 = position_paddle2.get_y()     
        bounce_sound = Sound(constants.BOUNCE_SOUND)
        over_sound = Sound(constants.OVER_SOUND)
                
        if yball < 0:
            ball.bounce_y()
            #self._audio_service.play_sound(bounce_sound)

        elif yball >= (constants.SCREEN_HEIGHT - 10):
            ball.bounce_y()
            #self._audio_service.play_sound(bounce_sound)

        if xball < xpaddle1 and (yball + 10 > ypaddle1 and yball < ypaddle1 + 60) :
            ball.bounce_x()

        elif xball + 10 > xpaddle2 and (yball + 10 > ypaddle2 and yball < ypaddle2 + 60):
            ball.bounce_x()    
        

        if not self._is_game_over:
            self._out_of_bounds(cast)
            self._handle_game_over(cast)
            
                
        
    
    def _out_of_bounds(self, cast):
        """Add points to the player who scores. Reset the game to initial position if one of the players scores 5 pints 

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        ball = cast.get_first_actor("ball")
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        reset_point = ResetPoint()

        if ball.get_position().get_x() <= 0:
            score2.add_points()
            reset_point.right(cast)
            self._winning_set(cast, score1, score2)
            
        elif ball.get_position().get_x()>= 890:    
            score1.add_points()
            reset_point.left(cast)
            self._winning_set(cast, score1, score2)

        
    
    def _winning_set(self, cast, score1, score2):
        """Checks if one of the players won the set (scores 5 points)

        Args:
            cast (Cast): The cast of Actors in the game.
            score1 (Score): The score of player 1.
            score2 (Score): The score of player 2.
        """
        reset = ResetActors()

        if score1.get_points() == 11: #Lossing the set 
                score1.reset_score()
                score2.reset_score()
                score1.win_set()
                
                score1.update_score()
                score2.update_score()
                reset.execute(cast)
        elif score2.get_points() == 11: #Lossing the set 
                score1.reset_score()
                score2.reset_score()
                score2.win_set()
                
                score1.update_score()
                score2.update_score()
                reset.execute(cast)
        if score1.get_set() == 3 or score2.get_set() == 3:
            self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        if self._is_game_over:
            message = cast.get_first_actor("message")
            if score1.get_set() == 3:
                message.set_text("Player 1 wins!")
            else:
                message.set_text("Player 2 wins!")

            ball = cast.get_first_actor("ball")
            ball.set_velocity(Point(0,0))

