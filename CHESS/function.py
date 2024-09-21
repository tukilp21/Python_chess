# Swapping the color "string" 
def colorSwap(input):
    if input == "white":
        return "black"
    else:
        return "white"

# From input (ex: A1) to coordination (x,y)
def inp2coor(input_str):
    # if input is lower case:
    input_str = input_str.upper()
    x, y = input_str[0], int(input_str[1]) - 1  # minus 1 for y

    alphabet = list(map(chr, range(65, 73)))
    x = alphabet.index(x)
    #return coordination as a list
    return [x, y]  


KNIW, KNIB = "♞ ", "♘ " 
BISW, BISB = "♝ ", "♗ " 
ROOW, ROOB = "♜ ", "♖ "
QUEW, QUEB = "♛ ", "♕ "
KINW, KINB = "♚ ", "♔ "
PAWW, PAWB = "♟ ", "♙ "

W_ICON = (ROOW, PAWW, BISW, KNIW, QUEW, KINW)
B_ICON = (ROOB, PAWB, BISB, KNIB, QUEB, KINB)
# BOY = {"white": WHITE, "black": BLACK} # Dictionary
# # func = (Rook, Pawn, Bishop, Knight, Queen, King)

Quan_Co_W = {
    "♜ ": ["ROOW", 2],
    "♞ ": ["KNIW", 2],
    "♝ ": ["BISW", 2],
    "♛ ": ["QUEW", 1],
    "♚ ": ["KINW", 1],
    "♟ ": ["PAWW", 8],
    }
            
Quan_Co_B = {
    "♖ ": ["ROOB", 2],
    "♘ ": ["KNIB", 2],
    "♗ ": ["BISB", 2],
    "♕ ": ["QUEB", 1],
    "♔ ": ["KINB", 1],
    "♙ ": ["PAWB", 8],
    }

Quan_Co = {
    "white": [Quan_Co_W, W_ICON],
    "black": [Quan_Co_B, B_ICON],
    }