class odd: # Xe
    def moveOdd(self):
        print("enter move Odd")
        if self.name % 2 == 1:
            print(f"--> i am odd {self.name}")
            return True
        return False

class even: # Tuong
    def moveEven(self):
        print("enter move Even")
        if self.name % 2 == 0:
            print(f"--> i am even {self.name}")
            return True
        return False

# super() sẽ tìm function có tên tương tự ở parent gần nhất
class child(odd, even):
    def __init__(self, value):
        self.name = value
        self.move()

    def move(self):
        if self.moveEven(): #Tuong
            return
        else:
            self.moveOdd() # Xe

#boy = test()
girl = child(int(input("enter value ")))