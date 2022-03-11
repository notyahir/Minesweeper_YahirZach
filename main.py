import random

# Note: Found bug that you can use the same coordinate more than one time 6 times in a row to win the game
# Board
row1 = ["1 ", "2 ", "3 ", "4 ", "5 "]
row2 = ["6 ", "7 ", "8 ", "9 ", "10"]
row3 = ["11", "12", "13", "14", "15"]
row4 = ["16", "17", "18", "19", "20"]
row5 = ["21", "22", "23", "24", "25"]

board = [
    row1,
    row2,
    row3,
    row4,
    row5
]

# Bomb board that is going to be altered to determine where the bombs should be randomized.

rowB1 = ["1 ", "2 ", "3 ", "4 ", "5 "]
rowB2 = ["6 ", "7 ", "8 ", "9 ", "10"]
rowB3 = ["11", "12", "13", "14", "15"]
rowB4 = ["16", "17", "18", "19", "20"]
rowB5 = ["21", "22", "23", "24", "25"]

bomb_Board = [
    rowB1,
    rowB2,
    rowB3,
    rowB4,
    rowB5
]


# Prints the board after every move
def print_rows(gameBoard):
    for i in range(len(gameBoard)):
        print("  ".join(gameBoard[i]))


print_rows(board)

print()


def random_bombs():
    for value in range(len(bomb_Board)):
        random_row = random.randint(0, len(bomb_Board) - 1)
        random_element = random.randint(0, len(bomb_Board) - 1)
        bomb_Board[random_row][random_element] = "Bb"


random_bombs()

print_rows(bomb_Board)
print()

bombHit = False
value_in_board = False


def flag_place():
    global bombHit, value_in_board
    x = 0
    while not bombHit:
        row_coordinate = input("Please choose a spot on the board. ")
        print()
        row_coordinate_single = row_coordinate + " "
        for elements in bomb_Board:
            if row_coordinate_single in elements:
                board[bomb_Board.index(elements)][elements.index(row_coordinate_single)] = "X "
                value_in_board = True
            elif row_coordinate in elements:
                board[bomb_Board.index(elements)][elements.index(row_coordinate)] = "X "
                value_in_board = True
            else:
                continue
        if not value_in_board:
            bombHit = True
            continue
        else:
            value_in_board = False
            print_rows(board)

    if bombHit:
        print("You hit a bomb, you lose")
        # print_rows(bomb_Board)

# Defines the coordinates the user can select (1-25), if they hit a bomb they lose (5 bombs), user is
# prompted to enter a new coordinate if they input one that is not listed on the board.
def place_flag():
    choices = 5
    while choices > -1:
        row_coordinate = input("Please choose a spot on the board. ")
        if choices == 0:
            print("You ran out of moves.")
            win()
            break
        if row_coordinate == "1":
            print()
            row1[0] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "2":
            row1[1] = "B"
            print_rows()
            print("You hit a bomb, you lose")
            break
        elif row_coordinate == "3":
            row1[2] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "4":
            row1[3] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "5":
            row1[4] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "6":
            row2[0] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "7":
            row1[1] = "B"
            print_rows()
            print("You hit a bomb, you lose")
            break
        elif row_coordinate == "8":
            row1[2] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "9":
            row1[3] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "10":
            row1[4] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "11":
            row1[0] = "B"
            print_rows()
            print("You hit a bomb, you lose")
            break
        elif row_coordinate == "12":
            row1[1] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "13":
            row1[2] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "14":
            row1[3] = "B"
            print_rows()
            print("You hit a bomb, you lose")
            break
        elif row_coordinate == "15":
            row1[4] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "16":
            row1[0] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "17":
            row1[1] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "18":
            row1[2] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "19":
            row1[3] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "20":
            row1[4] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "21":
            row1[0] = "B"
            print_rows()
            print("You hit a bomb, you lose")
            break
        elif row_coordinate == "22":
            row1[1] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "23":
            row1[2] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "24":
            row1[3] = "X"
            print_rows()
            choices = choices - 1
            continue
        elif row_coordinate == "25":
            row1[4] = "X"
            print_rows()
            choices = choices - 1
            continue
        else:
            print("That wasn't a valid choice")


# Defines a win function if the user successfully avoids all bombs by the end of their moves
def win():
    if row1[1] and row2[1] and row3[0] and row3[3] and row4[0] != "X":
        print("You won!")


# Calls place_flag function
flag_place()
