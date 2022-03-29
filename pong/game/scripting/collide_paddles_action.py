from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollidePaddleAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor("ball")
        paddle1 = cast.get_first_actor("paddle1")
        paddle2 = cast.get_first_actor("paddle2")

        if self._physics_service.has_collided(ball, paddle1):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    

        if self._physics_service.has_collided(ball, paddle2):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)  