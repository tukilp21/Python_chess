import CHESS.function as f

WHITE = "⬜"
BLACK = "⬛"
# WHITE, BLACK = "⊡", "▩"
# WHITE, BLACK = "W", "B"

KNIW, KNIB = "♞ ", "♘ " 
BISW, BISB = "♝ ", "♗ " 
ROOW, ROOB = "♜ ", "♖ "
QUEW, QUEB = "♛ ", "♕ "
KINW, KINB = "♚ ", "♔ "
PAWW, PAWB = "♟ ", "♙ "




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
        b1.data[y][x].value = globals()[name.upper() + color]


class Rook(Boy):
    def __init__(self):
        self.name = "ROO"
        self.check_move = False
        

    def setup(self, location, color, board):
        super().__init__(location, self.name, color)

        self.x, self.y = map(int, location)
        self.board = board


    def move(self, destination):

        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải xe:
        lo = self.board.data[self.y][self.x].value
        if lo != eval(f"{self.name}W") and lo != eval(f"{self.name}B"):
            print(f'Wrong boy, this is {lo}, not {self.name}')
            return False

        x = x_des - self.x
        y = y_des - self.y

        # test1 = location
        test1 = [self.x, self.y]

        if x != 0 and y != 0:  # cả 2 đều thay đổi
            print(f'Error 1!')
            return False

        else:  # xét trên đường đi có quân nào k:
            while test1 != destination:
                if x != 0:  # thay đổi theo phương x
                    test1[0] += int(x / abs(x))  # 1 or -1
                else:  # thay đổi theo phương y
                    test1[1] += int(y / abs(y))

                if self.board.data[test1[1]][test1[0]].value == None or test1 == destination:
                    continue
                else:
                    print(f'Error 2!')
                    return False


        self.board.data[y_des][x_des].value = self.board.data[self.y][self.x].value
		# self.check_move = True
        self.board.data[self.y][self.x].value = None

        # tự set up lại tọa độ bản thân:
        self.check_move = True
        self.x, self.y = map(int, destination)
        
        return True


class Bishop():
    ...
class Knight():
    ...
class Queen():
    ...
class King():
    ...
class Pawn(Boy):
    ...


def Play(board):
    # pieces = [Rook, Knight, Bishop, Queen, King]
    # for i in range(0, 5):
    #     pieces[i]().setup([i, 0], "W", board)
    #     pieces[i]().setup([i, 7], "B", board)
    # for i in range(7, 4, -1):
    #     pieces[0]().setup([i, 0], "W", board)
    #     pieces[0]().setup([i, 7], "B", board)
    #     pieces.pop(0) # pop first ind,boardex of array pieces
    # for x in range(8):
    #     Pawn().setup([x, 1], "W", board)
    #     Pawn().setup([x, 6], "B", board)
    
    '''SET UP'''
    ROOW1 = Rook()
    ROOB2 = Rook()

    ROOW1.setup([0,0], "W", board)
    ROOB2.setup([7,7], "B", board)
    
    print(board)


    '''MOVE'''
    W_ICON = (ROOW, PAWW, BISW, KNIW, QUEW, KINW)
    B_ICON = (ROOB, PAWB, BISB, KNIB, QUEB, KINB)
    # BOY = {"white": WHITE, "black": BLACK} # Dictionary
    # # func = (Rook, Pawn, Bishop, Knight, Queen, King)

    Quan_Co_W = {
        "♜ ": ["ROOW", 2],
        "♞ ": ["KNIW", 2],
        "♝ ": ["BISW", 2],
        "♛ ": ["KINW", 1],
        "♚ ": ["QUEW", 1],
        "♟ ": ["PAWW", 8],
        }
                
    Quan_Co_B = {
        "♖ ": ["ROOB", 2],
        "♘ ": ["KNIB", 2],
        "♗ ": ["BISB", 2],
        "♕ ": ["KINB", 1],
        "♔ ": ["QUEB", 1],
        "♙ ": ["PAWB", 8],
        }

    Quan_Co = {
        "white": [Quan_Co_W, W_ICON],
        "black": [Quan_Co_B, B_ICON],
        }

    color = "white"
    while True:
        try:
            # Get user's data
            print(f"{color.upper()} turn:")
            inp = input("--> Enter your move: ").split()
            if len(inp) == 2:
                
                # create location & destination:
                lo = f.inp2coor(inp[0])
                des = f.inp2coor(inp[1])
                print("Here")
                # move specific quân cờ (lo):
                x_lo, y_lo = map(int, lo)
                boy_lo = board.data[y_lo][x_lo].value
                x_des, y_des = map(int, des)
                boy_des = board.data[y_des][x_des].value

                # Bóc con cần đi:
                boy_lo = board.data[x_lo][y_lo].value

                # Quan_Co[color][0] = Quan_Co_W / B
                name = Quan_Co[color][0][boy_lo][0]
                total_num = Quan_Co[color][0][boy_lo][1] 
                 
                print(f"{name} {total_num}") # debugggggggg
                
                for i in range(1,total_num + 1):
                    real_name = eval(f'{name}{i}')
                    # --> "ROOW1"

                    if real_name.x == x_lo and real_name.y == y_lo:
                        print("I found u boi") # debugggggggg
                        break


                # xét màu:
                # --> dùng color để sử dụng dict BOY
                # --> xét target trong l
                if boy_lo in Quan_Co[color][1][color]:

                    # nếu ăn cùng màu:
                    if boy_des in Quan_Co[color][1][color]:
                        print("u dumb ass ?\n")
                        continue

                    # move:
                    tmp = real_name.move(des)
                    print(board)

                    print(f"{ROOW1.x} {ROOW1.y} {real_name.check_move}") # debuggg:

                    # unsuccessful move:
                    if tmp == False:
                        continue
                        
                    # END game condition:
                    elif boy_des == KINW or boy_des == KINB:
                        print(f'That is the end for {boy_des}')
                        break
                        
                # wrong color
                else:
                    print("It not your turn man !\n")
                    continue

                color = f.colorSwap(color)

            # end game: 
            elif inp[0] == 'exit' or inp[0] == "surrender":
                print(f'{color.upper()} {inp[0]}ed')
                break

        except:
            print("* Error in Move()\n")
            continue
            



b1 = Board()
print("new game ******************************\n")
# set up bàn cờ
Play(b1)


