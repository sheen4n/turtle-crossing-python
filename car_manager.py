from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def create_car(self):
        car = Car()
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(distance=self.car_speed)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(x=300, y=random.randint(-250, 250))
