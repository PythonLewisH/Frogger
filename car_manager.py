from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):

        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.goto(250, random.randint(-230, 230))
            new_car.setheading(180)
            self.cars.append(new_car)

    def drive(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT


