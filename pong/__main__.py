import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.ball import Ball
from game.casting.paddle import Paddle
from game.casting.point import Point
from game.casting.sound import Sound
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.reset_set import ResetActors
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.play_sound_action import PlaySoundAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.shared.color import Color
from game.casting.actor import Actor
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("paddle1", Paddle(Point(14, 260), constants.PADDLE))
    cast.add_actor("paddle2", Paddle(Point(886,260), constants.PADDLE))
    cast.add_actor("score1", Score(Point(100,5),"Player 1"))
    cast.add_actor("score2", Score(Point(550,5),"Player 2"))
    cast.add_actor("ball", Ball(constants.BALL_IMAGE))
    position = Point(int(constants.MAX_X / 2)-60, int(constants.MAX_Y / 2))
    cast.add_actor("message", Actor("", position, Point(10,10), Point(0,0)))


    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    #audio_service = AudioService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    #script.add_action("output", PlaySoundAction(audio_service))
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("reset", ResetActors())
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()