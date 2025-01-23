import math


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private instance attribute

    def bark(self):
        return f"{self.name} says Woof!"


# Creating an object
my_dog = Dog("Buddy", 3)


class Circle:
    pi1 = math.pi
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return Circle.pi * self._radius**2


circle = Circle(5)
print(circle.area())
