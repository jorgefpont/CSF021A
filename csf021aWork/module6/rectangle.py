""" In file rectangle.py.
Homework for Module 6. Create rectangle class and test try/except
blocks to catch value and type errors. Also catch
"""

class Rectangle:
    """One object of  class Rectangle stores one
      rectangle's length and width and has methods
      to calculalte other object attributes"""

    def __init__(self):
        """Class initializer. Automatically executed
        every time a new Rectangle is created"""
        self.height = 0
        self.width = 0

    def setData(self, newHeight, newWidth):
        """To give new values to a new rectangle"""

        # modification to raise a type error if either or both of the parameters
        # are not integers or floats -- non-numeric
        if (type(newHeight) != int) and (type(newHeight) != float):
            raise TypeError("can't set the Rectangle to a non-numeric value")
        if (type(newWidth) != int) and (type(newWidth) != float):
            raise TypeError("can't set the Rectangle to a non-numeric value")

        # modification to raise a value error if either or both of the parameters
        # are negative
        if newHeight < 0 or newWidth < 0:
            raise ValueError("can't set the Rectangle to a negative value")

        self.height = newHeight
        self.width = newWidth

    def area(self):
        """To get the area of the rectangle"""
        area = self.height * self.width
        return area

    def __str__(self):
        """To convert a Rectangle object into a string"""
        return f"height = {self.height}, width = {self.width}"


if __name__ == "__main__":
    """test program"""

    # list of test rectangles
    rectangleList = [['r1', 2, 3], ['r2', -3, 4], ['r3', -3, -4],
                     ['r4', 'x', 4], ['r5', 4, 'x'], ['r6', 'a', 'b'],
                     ['r7', 5.25, 6.50], ['r8', 5, 3.25],['r8', 5.25, 3],
                     ['r9', 0, 0]]

    for rect in rectangleList:
        # print('height, width = ', rect[1], ',', rect[2])
        rect[0] = Rectangle()
        try:
            rect[0].setData(rect[1], rect[2])
        except ValueError:
            print("error handled -- value error. Cannot have negative height/width\n")
        except TypeError:
            print("error handled -- type error. Height/width must be numeric\n")
        else:
            print(rect[0])
            print(rect[0].area())
            print()