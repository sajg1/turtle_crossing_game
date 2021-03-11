from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_Y_COORD = [i for i in range(-220, 250, 20)]
STARTING_X_COORD = [i for i in range(300, 3000, 10)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.garage = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.speed(self.move_speed)
        new_car.goto(random.choice(STARTING_X_COORD), random.choice(STARTING_Y_COORD))
        self.garage.append(new_car)

    def ready_cars(self):
        self.generate_car()

    def move_cars(self):
        for car in self.garage:
            car.forward(self.move_speed)

    def green_light(self):
        self.ready_cars()

    def red_light(self):
        for car in self.garage:
            car.hideturtle()
        self.garage = []

    def accelerate(self):
        self.move_speed += MOVE_INCREMENT

    def collision(self, player):
        for car in self.garage:
            if car.distance(player) < 20:
                return True
        return False

    def stop_traffic(self):
        self.move_speed = 0




