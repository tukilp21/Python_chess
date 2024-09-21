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
        # DEBUGGG:
        print(f"Im in Rook class. Hi, I'm {self.name}")
        
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải xe:
        # lo = self.board.data[self.y][self.x].value
        # if lo != eval(f"{self.name}W") and lo != eval(f"{self.name}B"):
        #     print(f'Wrong boy, this is {lo}, not {self.name}')
        #     return False

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
                    print('hi')
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


class Bishop(Boy):
    def __init__(self):
        self.name = "BIS"
        self.check_move = False


    def setup(self, location, color, board):
        super().__init__(location, self.name, color)
        self.x, self.y = map(int, location)
        self.board = board


    def move(self, destination):
        # DEBUG:
        print(f"Im in Bishop class. Hi, I'm {self.name}")
        
        x_des, y_des = map(int, destination)
        # move

        x_length = x_des - self.x
        y_length = y_des - self.y
        
        tmp_y, tmp_x = self.y, self.x

        if (abs(x_length) != abs(y_length)):
            print("error: not adjacent movement")
            return False

        #while abs(x_length) != 0:
        for i in range(abs(x_length), 0, -1):
            #[5,0] -> [1,4]
            tmp_x += int(x_length / abs(x_length))
            tmp_y += int(y_length / abs(y_length))

            # x_length = abs(x_length) - 1

            # DEBUG:
            # print(f"test: {x_length} {x}")
            if (self.board.data[tmp_y][tmp_x].value == None or tmp_x == x_des):
                continue
            else:
                print("error: move is blocked")
                return False

        self.board.data[y_des][x_des].value = self.board.data[self.y][self.x].value
        self.board.data[self.y][self.x].value = None
        
		#set up lai
        self.check_move = True
        self.x, self.y = map(int, destination)
        return True
        

class Knight(Boy):
    def __init__(self):
        self.name = "KNI"
        self.check_move = False


    def setup(self, location, color, board):
        super().__init__(location, self.name, color)
        self.x, self.y = map(int, location)
        self.board = board


    def move(self, destination):
        x_des, y_des = map(int, destination)

        # nếu vị trí đó k phải knight:
        # lo = self.board.data[self.y][self.x].value
        # if lo != KNIW and lo != KNIB:
        #     print(
        #         f'Wrong boy, this boy is {self.board.data[self.y][self.x].value}, not Knight'
        #     )
        #     return False

        x = abs(x_des - self.x)
        y = abs(y_des - self.y)

        if (x == 2 and y == 1) or (x == 1 and y == 2):
            self.board.data[y_des][x_des].value = self.board.data[self.y][self.x].value
            self.board.data[self.y][self.x].value = None
            pass
            
        else:
            print(f'Error Move')
            return False

        # tự set up lại tọa độ bản thân:
        self.check_move = True
        self.x, self.y = map(int, destination)
        return True


class Queen(Rook, Bishop):
    def __init__(self):
        self.name = "QUE"
        self.check_move = False


    def setup(self, location, color, board):
        Boy.__init__(self, location, self.name, color)
        self.x, self.y = map(int, location)
        self.board = board


    def move(self, destination):
        print(f"Im in Queen class, Im {self.name}")

        if Bishop.move(self, destination):
            print(self.name)
            pass
        elif Rook.move(self, destination):
            pass
        else:
            return False
            
		#set up lai
        self.check_move = True
        self.x, self.y = map(int, destination)
        return True


class King(Queen):
    def __init__(self):
        self.name = "KIN"
        self.check_move = False
        

    def setup(self, location, color, board):
        Boy.__init__(self, location, self.name, color)
        self.x, self.y = map(int, location)
        self.board = board


    def nhapthanh():
        ...

    def move(self, destination):
        x_des, y_des = map(int, destination)

        if abs(self.x - x_des) == 1 or abs(self.y - y_des) == 1:
            if Queen.move(self, destination):
                #setup lai
                self.x, self.y = map(int, destination)
                self.check_move = True
            else:
                print("no no")
            
        # if đi ngang 2 bước + xe và vua chưa từng đi bước nào 
            # nhapthanh()
        elif abs(self.x - x_des) == 2 and ~self.check_move:
            # tmp = Rook.get_value()
            self.nhapthanh()
            self.check_move = True
            
        else:
            print("error")
            return False


class Pawn(Boy):
    def __init__(self):
        self.name = "PAW"
        self.check_move = False


    def setup(self, location, color, board):
        super().__init__(location, self.name, color)
        self.x, self.y = map(int, location)
        self.board = board


    def move(self, destination):
        x_des, y_des = map(int, destination)
        
        # Nếu vị trí đó k phải tot:
        lo = self.board.data[self.y][self.x].value
        if lo != PAWW and lo != PAWB:
            print(f'Wrong boy, this boy is {lo}, not Pawn')
            return False

        x = x_des - self.x
        y = y_des - self.y

        # Pawn di chuyen
        if x == 0:
            if self.board.data[y_des][x_des].value == None:

                if self.y == 1 or self.y == 6:
                    #with White and 6 with Black
                    if y > 2 or y < -2:
                        print(f'Invalid move 1')
                        return False
                else:
                    if (lo == PAWW and y != 1) or (lo == PAWB and y != -1):
                        print(f'Invalid move 2')
                        return False
            else:
                print(f'Error')
                return False

        # Pawn an cheo
        elif abs(x) == 1:
            if self.board.data[y_des][x_des].value == None:
                print(f'Invalid move 3')
                return False

        self.board.data[y_des][x_des].value = self.board.data[self.y][self.x].value
        self.board.data[self.y][self.x].value = None
        
        # Phong cap
        print(y_des)
        if y_des == 7 or y_des == 0:
            changes = [QUEB, ROOB, KNIB, BISB, QUEW, ROOW, KNIW, BISW]
            inp = int(input("1:Queen, 2:Rook, 3:Knight, 4:Bishop\t--> Choose a number: "))
            self.board.data[y_des][x_des].value = changes[round(y_des/2) + inp - 1]
            
            # tạo object quan cờ mới:
            
            # return object này ra ngoài:

		#setup lai
        self.check_move = True
        self.x, self.y = map(int, destination)
        return True


# ______________________________________________________________
def Play(board):

    # SET UP_____________________________________________
    
    types = [Rook, Knight, Bishop, Queen, King]
    pieces = ["ROO", "KNI", "BIS", 'QUE', "KIN"]

    # Đặt cờ từ A đến E (cả 2 bên W B)
    for i in range(0, 5):
        locals()[f'{pieces[i]}W1'] = types[i]()
        locals()[f'{pieces[i]}B1'] = types[i]()
        eval(f'{pieces[i]}W1').setup([i, 0], "W", board)
        eval(f'{pieces[i]}B1').setup([i, 7], "B", board)
        
    # Đặt cờ từ H về E (cả 2 bên W B)
    for i in range(7, 4, -1):
        locals()[f'{pieces[0]}W2'] = types[0]()
        locals()[f'{pieces[0]}B2'] = types[0]()
        eval(f'{pieces[0]}W2').setup([i, 0], "W", board)
        eval(f'{pieces[0]}B2').setup([i, 7], "B", board)
        pieces.pop(0)
        types.pop(0) 
        # pop first index, board of array pieces

    for i in range(8):
        locals()[f'PAWW{i + 1}'] = Pawn()
        locals()[f'PAWB{i + 1}'] = Pawn()
        eval(f'PAWW{i + 1}').setup([i, 1], "W", board)
        eval(f'PAWB{i + 1}').setup([i, 6], "B", board)
        
    print(board)


    # MOVE ______________________________________________

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
                
                
                # move specific quân cờ (lo):
                x_lo, y_lo = map(int, lo)
                boy_lo = board.data[y_lo][x_lo].value
                x_des, y_des = map(int, des)
                boy_des = board.data[y_des][x_des].value


                # Bóc con cần đi
                name = f.Quan_Co[color][0][boy_lo][0]
                total_num = f.Quan_Co[color][0][boy_lo][1] 
                # (function.py: Quan_Co[color][0] = Quan_Co_W / B)
                 
                # print(f"{name} {total_num}") # debugggggggg
                
                for i in range(1, total_num + 1):
                    real_name = eval(f'{name}{i}') # --> "ROOW1"

                    if real_name.x == x_lo and real_name.y == y_lo:
                        # print("I found u boi") # debugggggggg
                        break


                # xét màu:
                # --> dùng color để tìm quân đó trong W/B_ICON
                if boy_lo in f.Quan_Co[color][1]:

                    # nếu ăn cùng màu:
                    if boy_des in f.Quan_Co[color][1]:
                        print("u dumb ass ?\n")
                        continue

                    # move:
                    tmp = real_name.move(des)
                    print(board)

                    # debuggg:
                    # print(f"{real_name.x} {real_name.y} {real_name.check_move} {real_name.name}") 

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


