WHITE = "⬜"
BLACK = "⬛"
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
        color = True # đổi liên tục trắng đen
        for row in range(self.size):

            color = not(color)
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
        value = "" # return value to display the Field
        INITIAL = " " * 3
        
        # _______________________________________
        # x-axis:
        value += INITIAL
        for x_axis in range(self.size):
            value += f"  {x_axis + 1} "

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
            value += f"  {x_axis + 1} "

        # _______________________________________
        value += "\n"
        return value