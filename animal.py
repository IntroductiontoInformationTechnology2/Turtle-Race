from turtle import Turtle
from random import randint


class Animal:
    """This class is used to describe animal's properties"""
    def __init__(self, name, color, start_x, start_y, speed_min, speed_max, shape):
        self.name = name
        self.color = color
        self.startX = start_x
        self.startY = start_y
        self.speedMin = speed_min
        self.speedMax = speed_max
        self.shape = shape
        self.animal = Turtle()
        self.info = Turtle()
        self.info.speed(0)
        self.info.hideturtle()
        self.animal.color(self.color)
        self.animal.shape(self.shape)
        self.animal.penup()
        self.step = 0
        self.animal.goto(self.startX, self.startY)
        self.show_info()
        self.animal.speed(randint(self.speedMin, self.speedMax))

    def move(self, rotate, step, sign):
        if rotate != 0:
            self.animal.left(rotate)
        self.animal.forward(step)
        if not sign:
            self.step += step
        else:
            self.step -= step
        self.show_info()

    def show_info(self):
        self.info.clear()
        self.info.penup()
        self.info.goto(self.startX + self.step + 20, self.startY)
        self.info.pendown()
        self.info.write(self.name, font=("Roboto", 12))