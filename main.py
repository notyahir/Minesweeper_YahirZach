import random
print("Hello Jyle!")

#Board

row1 = ["1 ", "2 ", "3 ", "4 ", "5  "]
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
#Prints the board
def print_rows():
    for i in range(len(board)):
        print("  ".join(board[i]))

print_rows()


#Defines the where the user can click, if they hit a bomb they lose (5 bombs)
def place_flag():
    choices = 5
    while choices > 0:
        row_coordinate = input("Please choose a spot on the board. ")
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
        if choices == 0:
            print("You ran out of moves.")
        win()

def win():
    if row1[1] and row2[1] and row3[0] and row3[3] and row4[0] != "X":
        print("You won!")

place_flag()




