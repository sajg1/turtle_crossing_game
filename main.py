import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')


game_is_on = True


while game_is_on:

    level_is_on = True
    while level_is_on:
        car_manager.green_light()
        time.sleep(0.1)
        screen.update()
        car_manager.move_cars()
        if 270 < player.ycor() < 300:
            player.reset_position()
            scoreboard.levelup()
            car_manager.red_light()
            car_manager.accelerate()
            level_is_on = False
        if car_manager.collision(player):
            car_manager.stop_traffic()
            scoreboard.game_over_message()
            screen.onkey(player.stop, 'Up')
            game_is_on = False

screen.exitonclick()
