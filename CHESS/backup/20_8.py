WHITE = "⬜"
BLACK = "⬛"
KNIW, KNIB = "♞ ", "♘ "
BISW, BISD = "♝ ", "♗ "
ROOW, ROOB = "♜ ", "♖ "
QUEW, QUEB = "♛ ", "♕ "
KINW, KINB = "♚ ", "♔ "
PAWW, PAWB = "♟ ", "♙ "

# # WHITE, BLACK = "⊡", "▩"
# WHITE, BLACK = "W", "B"
# KNIW, KNIB = "♞", "♘"
# BISW, BISD = "♝", "♗"
# ROOW, ROOB = "♜", "♖"
# QUEW, QUEB = "♛", "♕"
# KINW, KINB = "♚", "♔"
# PAWW, PAWB = "♟", "♙"

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
            value += f"  {x_axis} "

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
            value += f"  {x_axis} "

        # _______________________________________
        value += "\n"
        return value


class Rook():
    def __init__(self, location, destination=None):
        y = location[1]
        x = location[0]

        # MOVE mode:
        if destination != None:
            self.move(location, destination)
            print(board1)

        # SETUP mode:
        else:
            board1.data[y][x].value = ROOW

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải xe:
        if board1.data[y_lo][x_lo].value != ROOW:
            print(
                f'Wrong boy, this boy is {board1.data[y_lo][x_lo].value}, not Rook'
            )
            return False

        x = x_des - x_lo
        y = y_des - y_lo

        test1 = location

        if x != 0 and y != 0:  # cả 2 đều thay đổi
            print(f'Error 1!')
            return False

        else:  # xét trên đường đi có quân nào k:
            while test1 != destination:
                if x != 0:  # thay đổi theo phương x
                    test1[0] += int(x / abs(x))  # 1 or -1
                else:  # thay đổi theo phương y
                    test1[1] += int(y / abs(y))
                
                if board1.data[test1[1]][test1[0]].value == None or test1 == destination:
                    continue
                else:
                    print(f'Error 2!')
                    return False

        board1.data[y_lo][x_lo].value = None
        board1.data[y_des][x_des].value = ROOW
        return True


# class Boy():
#     def __init__(self, board):
#         self.board = board
#         print(board)

class Bishop():
    def __init__(self, location, destination = None):
        # self.board
        y = location[1]
        x = location[0]
        # MOVE MODE:
        if destination != None:
            self.move(location, destination)
            print(board1)
        # SETUP MODE:
        else:
            board1.data[y][x].value = BISW
        

    def move(self,location,destination):
        x_lo, y_lo = map(int,location)
        x_des, y_des = map(int,destination)

        # move
        if board1.data[y_lo][x_lo].value != BISW:
            print(f'Wrong boy, this boy is {board1.data[y_lo][x_lo].value}, not Bishop')
            return False
        
        x_length = x_des - x_lo
        y_length = y_des - y_lo

        x,y = x_lo, y_lo

        if (abs(x_length) != abs(y_length)):
            print("error: not adjacent movement")
            return False

        while abs(x_length) != 0:

            x += int(x_length/abs(x_length))
            y += int(y_length/abs(y_length))
            
            x_length = abs(x_length) - 1
            if (board1.data[y][x].value == None or x == x_des):
                continue
            else:
                print("error: move is blocked")
                return False

        # print(f"{x_lo} and {y_lo}")
        # print(f"{x_des} and {y_des}")        
        board1.data[y_des][x_des].value = BISW
        board1.data[y_lo][x_lo].value = None
        return True

class Knight():
    def __init__(self, location, destination=None):
        y = location[1]
        x = location[0]

        # MOVE mode:
        if destination != None:
            self.move(location, destination)
            print(board1)

        # SETUP mode:
        else:
            board1.data[y][x].value = KNIW

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải knight:
        if board1.data[y_lo][x_lo].value != KNIW:
            print(
                f'Wrong boy, this boy is {board1.data[y_lo][x_lo].value}, not Knight'
            )
            return False

        x = abs(x_des - x_lo)
        y = abs(y_des - y_lo)

        if (x == 2 and y == 1) or (x == 1 and y == 2):
            board1.data[y_lo][x_lo].value = None
            board1.data[y_des][x_des].value = KNIW
            return True
        else:
            print(f'Error Move')
            return False


class Pawn():
    def __init__(self, location, destination=None):
        y = location[1]
        x = location[0]

        # MOVE mode:
        if destination != None:
            self.move(location, destination)
            print(board1)

        # SETUP mode:
        else:
            board1.data[y][x].value = PAWW

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)
        
        # nếu vị trí đó k phải xe:
        if board1.data[y_lo][x_lo].value != PAWW:
            print(
                f'Wrong boy, this boy is {board1.data[y_lo][x_lo].value}, not Pawn'
            )
            return False

        x = x_des - x_lo
        y = y_des - y_lo
        #Pawn di chuyen
        if x == 0:
            if board1.data[y_des][x_des].value == None:
                if y_lo == 1:
                    #with White and 6 with Black
                    if y > 2:
                        print(f'Invalid move 1')
                        return False
                else:
                    if y != 1:
                        print(f'Invalid move 2')
                        return False
            else:
                print(f'Error')
                return False

        #Pawn an cheo
        elif abs(x) == 1:
            if board1.data[y_des][x_des].value == None:
                print(f'Invalid move 3')
                return

        board1.data[y_lo][x_lo].value = None
        board1.data[y_des][x_des].value = PAWW
        return True

        #Phong cap
        if y_des == 7:
            changes = [QUEW, ROOW, KNIW, BISW]
            inp = int(input("1:Queen, 2:Rook, 3:Knight, 4:Bishop: "))
            board1.data[y_des][x_des].value = changes[inp - 1]

class O_O():
    def move(self):
        if board1.data[1][4].value == KINW and board1.data[1][7].value == ROOW:
            board1.data[1][4].value = ''
            board1.data[1][6].value = KINW
            board1.data[1][7].value = ''
            board1.data[1][5].value = ROOW

class O__O():
    def move(self):
        if board1.data[0][4].value == KINW and board1.data[0][0].value == ROOW:
            board1.data[0][4].value = ''
            board1.data[0][2].value = KINW
            board1.data[0][0].value = ''
            board1.data[0][3].value = ROOW


def Setup():
    pieces=[Rook,Knight,Bishop,Pawn]
    for i in range(0,3):
        pieces[i]([i,0])
        pieces[i]([i,7])
    for i in range(7,4,-1):
        pieces[0]([i,0])
        pieces[0]([i,7])
        pieces.pop(0)
    for x in range(8):
        Pawn([x, 1])
        Pawn([x, 6])
    board1.data[0][3].value = QUEW
    board1.data[0][4].value = KINW
    board1.data[7][3].value = QUEB
    board1.data[7][4].value = KINB
    
board1 = Board()
print("new game ******************************\n")
# set up bàn cờ
Setup()
print(board1)

#di chuyển
# Pawn([3,1],[3,3])
# Pawn([0,1], [0,3])

# Bishop([2,0],[4,2])
# Knight([1,0],[2,2])
# Rook([0,0], [0,2])


for i in range(0,100):
    inp=input("Your next move: ")
    if inp=='end':
        break
    else:
        inp=inp.split()
        x=int(inp[0]),int(inp[1])
        y=int(inp[2]),int(inp[3])
        eval(f"board1.data[{y[0]}][{x[0]}]([{x[0],y[0]}],[{x[1],y[1]}])")
