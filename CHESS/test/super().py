class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# # LONG CODE:
# class Square:
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length

#     def perimeter(self):
#         return 4 * self.length


# MUCH BETTER
class Square(Rectangle):
    # function: init, area, perimeter
    def __init__(self, length):
        super().__init__(length, length)
        self.name = "square"
        # --> self.length = length
        # --> self.width = length

    def area(self):
        return self.width

testRec = Rectangle(3,4)
test = Square(5)
print(test.name)
print(test.area())