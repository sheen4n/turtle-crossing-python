from turtle import Turtle

STARTING_POSITION = (0, - 200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_forward(self):
        self.forward(distance=MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
