WHITE = "⬜"
BLACK = "⬛"
KNIW, KNIB = "♞ ", "♘ "
BISW, BISB = "♝ ", "♗ "
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
        alphabet = list(map(chr, range(65, 73)))

        for x_axis in range(self.size):
            value += f" {alphabet[x_axis]}  "

        # clearer look
        value += "\n" + INITIAL
        for i in range(self.size):
            value += f"----"

        # y-axis:
        value += "\n"
        for row in range(self.size):
            value += f"{row + 1} |"

            for col in range(self.size):
                #print(f"{row} and {col}")
                #print(self.data[row])
                value += f" {self.data[row][col]} "

            # repeat y-axis for clearer look
            value += f"| {row + 1} \n"

        # repeat x-axis for clearer look
        value += INITIAL
        for i in range(self.size):
            value += f"----"
        value += "\n" + INITIAL
        for x_axis in range(self.size):
            value += f" {alphabet[x_axis]}  "

        # _______________________________________
        value += "\n"
        return value


class Boy():
    # set color
    def __init__(self, location, name, color):
        x, y = map(int, location)
        board1.data[y][x].value = globals()[name.upper() + color]


class Rook(Boy):
    def __init__(self):
        self.name = "ROO"

    def setup(self, location, color):
        super().__init__(location, self.name, color)

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải xe:
        lo = board1.data[y_lo][x_lo].value
        if lo != eval(f"{self.name}W") and lo != eval(f"{self.name}B"):
            print(f'Wrong boy, this is {lo}, not {self.name}')
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

        board1.data[y_des][x_des].value = board1.data[y_lo][x_lo].value
        board1.data[y_lo][x_lo].value = None

        return True


class Bishop(Boy):
    def __init__(self):
        self.name = "BIS"

    def setup(self, location, color):
        super().__init__(location, self.name, color)

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        # move
        lo = board1.data[y_lo][x_lo].value
        if lo != eval(f'{self.name}W') and lo != eval(f'{self.name}B'):
            print(f'Wrong boy, this boy is {lo}, not {self.name}')
            return False

        x_length = x_des - x_lo
        y_length = y_des - y_lo

        x, y = x_lo, y_lo

        if (abs(x_length) != abs(y_length)):
            print("error: not adjacent movement")
            return False

        #while abs(x_length) != 0:
        for i in range( abs(x_length), 0, -1):
            #[5,0] -> [1,4]
            x += int(x_length / abs(x_length))
            y += int(y_length / abs(y_length))

            # x_length = abs(x_length) - 1

            print(f"test: {x_length} {x}")
            if (board1.data[y][x].value == None or x == x_des):
                continue
            else:
                print("error: move is blocked")
                return False

        board1.data[y_des][x_des].value = board1.data[y_lo][x_lo].value
        board1.data[y_lo][x_lo].value = None
        return True


class Knight(Boy):
    def __init__(self):
        self.name = "KNI"

    def setup(self, location, color):
        super().__init__(location, self.name, color)

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải knight:
        lo = board1.data[y_lo][x_lo].value
        if lo != KNIW and lo != KNIB:
            print(
                f'Wrong boy, this boy is {board1.data[y_lo][x_lo].value}, not Knight'
            )
            return False

        x = abs(x_des - x_lo)
        y = abs(y_des - y_lo)

        if (x == 2 and y == 1) or (x == 1 and y == 2):
            board1.data[y_des][x_des].value = board1.data[y_lo][x_lo].value
            board1.data[y_lo][x_lo].value = None
            return True
        else:
            print(f'Error Move')
            return False


class Pawn(Boy):
    def __init__(self):
        self.name = "PAW"

    def setup(self, location, color):
        super().__init__(location, self.name, color)

    def move(self, location, destination):
        x_lo, y_lo = map(int, location)
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải tot:
        lo = board1.data[y_lo][x_lo].value
        if lo != PAWW and lo != PAWB:
            print(
                f'Wrong boy, this boy is {lo}, not Pawn'
            )
            return False

        x = x_des - x_lo
        y = y_des - y_lo
        #Pawn di chuyen
        if x == 0:
            if board1.data[y_des][x_des].value == None:

                if y_lo == 1 or y_lo == 6:
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

        board1.data[y_des][x_des].value = board1.data[y_lo][x_lo].value
        board1.data[y_lo][x_lo].value = None
        return True

        #Phong cap
        if y_des == 7:
            changes = [QUEW, ROOW, KNIW, BISW]
            inp = int(input("1:Queen, 2:Rook, 3:Knight, 4:Bishop: "))
            board1.data[y_des][x_des].value = changes[inp - 1]


class Queen(Bishop, Rook):
    def __init__(self):
        self.name = "QUE"

    def setup(self, location, color):
        Boy.__init__(self, location, self.name, color)

    def move(self, location, destination):
        if Bishop.move(self, location, destination):
            pass
        elif Rook.move(self, location, destination):
            pass
        else:
            return False
        return True


class King(Queen):
    def __init__(self):
        self.name = "KIN"

    def setup(self, location, color):
        Boy.__init__(self, location, self.name, color)

    def move(self, location, destination):
        Queen.move(location, destination)


def castle():

    return


class O_O(Boy):
    def move(self, color):
        if board1.data[1][4].value == KINW and board1.data[1][7].value == ROOW:
            Rook([1, 7], [1, 5])
            board1.data[1][4].value = ''
            board1.data[1][6].value = KINW
            # King([1,4],[1,6])
            # board1.data[1][7].value = ''
            # board1.data[1][5].value = ROOW


class O__O(Boy):
    def move(self, color):
        if board1.data[0][4].value == KINW and board1.data[0][0].value == ROOW:
            board1.data[0][4].value = ''
            board1.data[0][2].value = KINW
            board1.data[0][0].value = ''
            board1.data[0][3].value = ROOW


def Setup():
    pieces = [Rook, Knight, Bishop, Queen, King]
    for i in range(0, 5):
        pieces[i]().setup([i, 0], "W")
        pieces[i]().setup([i, 7], "B")
    for i in range(7, 4, -1):
        pieces[0]().setup([i, 0], "W")
        pieces[0]().setup([i, 7], "B")
        pieces.pop(0)
    for x in range(8):
        Pawn().setup([x, 1], "W")
        Pawn().setup([x, 6], "B")
    print(board1)


def Move():
    WHITE = (ROOW, PAWW, BISW, KNIW, QUEW, KINW)
    BLACK = (ROOB, PAWB, BISB, KNIB, QUEB, KINB)
    BOY = {"white": WHITE, "black": BLACK}
    func = (Rook, Pawn, Bishop, Knight, Queen, King)

    def colorSwap(input):
        if input == "white":
            return "black"
        else:
            return "white"

    def inp2coor(input_str):
        x, y = input_str[0], int(input_str[1]) - 1  # minus 1 for y

        alphabet = list(map(chr, range(65, 73)))
        x = alphabet.index(x)

        return [x, y]  #return coordination as a list

    color = "white"
    while True:
        print(f"{color.upper()} turn:")
        inp = input("--> Enter your move: ").split()
        if len(inp) == 2:
            # create location & destination:
            lo = inp2coor(inp[0])
            des = inp2coor(inp[1])

            # move specific quân cờ (lo):
            x_lo, y_lo = map(int, lo)
            boy_lo = board1.data[y_lo][x_lo].value
            x_des, y_des = map(int, des)
            boy_des = board1.data[y_des][x_des].value
            
            # xét màu
            # --> dùng color để sử dụng dict BOY
            # --> xét target trong list WHITE/ BLACK
            if boy_lo in BOY[color]:

                target_idx = BOY[color].index(boy_lo)

                # ăn khác màu:
                if boy_des in BOY[color]:
                    print("u dumb ass ?\n")
                    continue

                # move:
                tmp = func[target_idx]().move(lo, des)
                print(board1)

                # unsuccessful move:
                if tmp == False:
                    continue
            # wrong color
            else:
                print("It not your turn man !")
                continue

            color = colorSwap(color)

        # end game:
        else: 
            if inp[0] == 'exit' or inp[0] == "surrender":
                break
            if boy_des == KINW or boy_des == KINB:
                print(f'That is the end')
                break



# def End_game():

board1 = Board()
print("new game ******************************\n")
# set up bàn cờ
Setup()
Move()
