#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @property
    def height(self):
        """get the height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get the y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setting the value of width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setting the value of height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setting the value of x"""
        if type(value) is not int:
            raise TypeError("X must be an integer")
        if value <= 0:
            raise ValueError("X must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setting the value of y"""
        if type(value) is not int:
            raise TypeError("Y must be an integer")
        if value <= 0:
            raise ValueError("Y must be > 0")
        self.__y = valueR

    def area(self):
        """Rectangle area function"""
        return self.width * self.__height

    def display(self):
        """function for display"""
        if self.__y > 0:
            print("\n" * (self.__y), end="")
        for c in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """output of strings"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        """instance attributes"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """attributes to rectangle dictionary"""
        """output"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return {'x':x, 'y':y, 'id': id, 'height': h, 'width': w}
