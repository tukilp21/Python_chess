class Board():
    def __init__(self, size):
        self.size = size   
        self.data = [0 for i in range(self.size)]

    def __str__(self):
        return f"{self.data}"

    class Rook():
        def __init__(self):
            self.set()
        
        def set(self):
            print("in")
            Board.data[3] = 100

board1 = Board(5)
print(board1)
test = Board.Rook()
