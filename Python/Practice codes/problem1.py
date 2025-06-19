# import turtle
# my_pen = turtle.Turtle()
# for i in range(4):
#     my_pen.forward(50)
#     my_pen.left(90)
# turtle.done()


# rhombus 
# my_pen.speed(1)
# for _ in range(2):
#     my_pen.forward(100)
#     my_pen.left(45)
#     my_pen.forward(100)
#     my_pen.left(135)
# turtle.done()

# star
# import turtle library
# for i in range(5):
    
#     my_pen.forward(50)
#     my_pen.right(144)
# turtle.done()


# sides = 6
# angle = 360 / sides 
# for i in range(sides):
#     my_pen.forward(100)
#     my_pen.right(angle)
# turtle.done()



#print the letter M 
# my_pen.penup()
# my_pen.goto(-200, 0)
# my_pen.pendown()
# my_pen.left(90)
# my_pen.forward(100)
# my_pen.right(135)
# my_pen.forward(50)
# my_pen.left(90)
# my_pen.forward(50)
# my_pen.right(135)
# my_pen.forward(100)
# my_pen.left(135)
# turtle.done()


# my_pen.penup()
# my_pen.goto(-200, 0)
# my_pen.pendown()
# my_pen.left(60)
# my_pen.forward(100)
# my_pen.right(120)
# my_pen.forward(100)
# my_pen.right(120)
# my_pen.forward(100)
# my_pen.right(120)
# my_pen.penup()



# def form_sq(side):

#     for i in range(4):
#         my_pen.fd(side)
#         my_pen.left(90)
#         side -= 5

# tut = turtle.Screen()
# tut.bgcolor("green")
# tut.title("Turtle")
# my_pen.color("yellow")
# for _ in range(4):
#     form_sq(100)


# import pandas as pd 
# data_frame = pd.DataFrame()
# data_frame['Name'] = ['John', 'Steve', 'Sarah']
# print(data_frame.shape)


# import random
# import numpy as np
# import matplotlib.pyplot as plt
# # Probability to move up or down
# prob = [0.05, 0.95]
# # statically defining the starting position
# start = 2
# positions = [start]
# # creating the random points
# rr = np.random.random(1000)  # [.62, .60, .54, .51, .46, .45, .43, .42, .39, .38]
# downp = rr < prob[0]
# upp = rr > prob[1]

# for idownp, iupp in zip(downp, upp):
#     down = idownp and positions[-1] > 1
#     up = iupp and positions[-1] < 4
#     positions.append(positions[-1] - down + up)

# # plotting down the graph of the random walk in 1D
# plt.plot(positions)
# plt.show()

import numpy as nmp
from skimage import data
import matplotlib.pyplot as mplot
image1 = data.camera()
print(type(image1))
#Image is a NumPy array:
mask = image1 < 87
image1[mask] = 255
mplot.imshow(image1, cmap ='gray')
mplot.show()



cclass Person(object):
# __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


class Employee(Person):
    def __init__(self, name ,idnumber, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

if __name__ == "__main__":
    a = Employee('Rahul', 886012, 200000,"intern")
    a.details()
    a.display()



# abstraction 

from abc import ABC, abstractmethod
# Creating an abstract class called 'Shape'
class Shape(ABC): #subclass of ABC from abc module
    @abstractmethod
    def area(self): #abstract method impolemented by the subclass of Shape
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Implementation for circle area
