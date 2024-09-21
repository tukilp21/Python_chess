# WHITE = "⬜"
# BLACK = "⬛"
WHITE, BLACK = "⊡", "▩"
KNIW, KNIB = "♞", "♘"
BISW, BISD = "♝", "♗"
ROOW, ROOB = "♜", "♖"
QUEW, QUEB = "♛", "♕"
KINW, KINB = "♚","♔"
PAWW, PAWB = "♟","♙"

SIZE = 8


class Tile:
    def __init__(self):
        self.color = None
        self.value = None

    def __str__(self):
        if self.value:
            return self.value
        else:
            return self.color

    def setColor(self, color):
        self.color = color


class Board:
    def __init__(self):

        self.size = SIZE

        data = []
        color = True  # đổi liên tục trắng đen
        for row in range(self.size):

            color = not (color)
            # set value for each row:
            row_val = []

            for col in range(self.size):
                tmp = Tile()
                row_val.append(tmp)

                if color:
                    tmp.setColor(WHITE)
                    color = False
                else:
                    tmp.setColor(BLACK)
                    color = True

            # put value into each data's "column"
            data.append(row_val)

        self.data = data

    def __str__(self):
        value = ""  # return value to display the Field
        INITIAL = " " * 3

        # _______________________________________
        # x-axis:
        value += INITIAL
        for x_axis in range(self.size):
            value += f" {x_axis} "

        # clearer look
        value += "\n" + INITIAL
        for i in range(self.size):
            value += f"----"

        # y-axis:
        value += "\n"
        for row in range(self.size):
            value += f"{row} |"

            for col in range(self.size):
                #print(f"{row} and {col}")
                #print(self.data[row])
                value += f" {self.data[row][col]} "

            # repeat y-axis for clearer look
            value += f"| {row} \n"

        # repeat x-axis for clearer look
        value += INITIAL
        for i in range(self.size):
            value += f"----"
        value += "\n" + INITIAL
        for x_axis in range(self.size):
            value += f" {x_axis} "

        # _______________________________________
        value += "\n"
        return value
        

class Rook():
    def __init__(self, location, destination = None):
        y = location[1]
        x = location[0]
        
        # MOVE mode:
        if destination != None:
            # nếu vị trí đó k phải xe:
            if board1.data[y][x].value != ROOW:
                print(f'Wrong boy, this boy is {board1.data[y][x].value}, not Rook')
                return
            self.move(location, destination)
            print(board1)
        
        # SETUP mode:
        else:
            board1.data[y][x].value = ROOW

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        x = x_des - x_lo
        y = y_des - y_lo

        test1 = location

        if x != 0 and y != 0:  # cả 2 đều thay đổi
            print(f'Error 1!')
            return
        else: # xét trên đường đi có quân nào k:
            while test1 != destination:
                if x != 0: # thay đổi theo phương x
                    test1[0] += int(x / abs(x))  # 1 or -1
                else: # thay đổi theo phương y
                    test1[1] += int(y / abs(y))
                if board1.data[test1[1]][test1[0]].value == None or test1 == destination:
                    continue
                else:
                    print(f'Error 2!')
                    return

        board1.data[y_lo][x_lo].value = ''
        board1.data[y_des][x_des].value = ROOW


class Knight():
    def __init__(self, location, destination = None):
        y = location[1]
        x = location[0]
        
        # MOVE mode:
        if destination != None:
            # nếu vị trí đó k phải xe:
            if board1.data[y][x].value != KNIW:
                print(f'Wrong boy, this boy is {board1.data[y][x].value}, not Knight')
                return
            self.move(location, destination)
            print(board1)
        
        # SETUP mode:
        else:
            board1.data[y][x].value = KNIW
      
    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        x = abs(x_des - x_lo)
        y = abs(y_des - y_lo)

        if (x==2 and y==1) or (x==1 and y==2):
            board1.data[y_lo][x_lo].value = ''
            board1.data[y_des][x_des].value = KNIW
        else:
            print(f'Error Move')
            return

class Pawn():
    def __init__(self, location, destination = None):
        y = location[1]
        x = location[0]
        
        # MOVE mode:
        if destination != None:
            # nếu vị trí đó k phải xe:
            if board1.data[y][x].value != PAWW:
                print(f'Wrong boy, this boy is {board1.data[y][x].value}, not Pawn')
                return
            self.move(location, destination)
            print(board1)
        
        # SETUP mode:
        else:
            board1.data[y][xx].value = PAWW
    
    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        x = x_des - x_lo
        y = y_des - y_lo
        #Pawn di chuyen
        if y == 0:
            if y_lo == 2: 
            #with White and 7 with Black
                if x < 3:
                    continue
                else:
                    print(f'Invalid move')
                    return
            else:
                if x == 1:
                    continue
                else:
                    print(f'Invalid move')
                    return
        #Pawn an cheo
        elif abs(y) == 1:
            if board1.data[y_des][x_des].value:
                continue
            else:
                print(f'Invalid move')
        board1.data[y_lo][x_lo].value = ''
        board1.data[y_des][x_des].value = PAWW
        


board1 = Board()

# set up bàn cờ
Rook([0,0])
Rook([0,7])
Rook([7,0])
Rook([7,7])
Knight([6,6])
PAWN
# Knight([6,6])
# Knight([6,6])
# Knight([6,6])Nprint((board1)

#di chuyển
Rook([7, 7],[7,4])



