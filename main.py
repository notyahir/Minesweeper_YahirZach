import random

# Board
# Worked with Jyle
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
def print_rows(game_board):
    for i in range(len(game_board)):
        print("  ".join(game_board[i]))

def random_bombs():
    for value in range(len(bomb_Board)):
        random_row = random.randint(0, len(bomb_Board) - 1)
        random_element = random.randint(0, len(bomb_Board) - 1)
        bomb_Board[random_row][random_element] = "Bb"

bombHit = False
value_in_board = False

# Defines the coordinates the user can select (1-25), if they hit a bomb ton the board.hey lose (5 bombs), user is
# prompted to enter a new coordinate if they input one that is not listed
# Worked with Jyle
def flag_place(play):
    global bombHit, value_in_board
    if play == "Yes":
        choices = 5
        while not bombHit:
            while choices > 0:
                if bombHit == True:
                    break
                print()
                print("You have " + str(choices) + " choices left!")
                row_coordinate = input("Please choose a spot on the board. ")
                print()
                row_coordinate_single = row_coordinate + " "
                # Worked with Jyle
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

                choices -= 1
            # Defines a win function if the user successfully avoids all bombs by the end of their moves
            if choices == 0:
                print("No more choices so you win!")
                break

        if bombHit:
            print("You hit a bomb, you lose")
            # print_rows(bomb_Board)
        else:
            print("You win!")
    elif play == "No":
        print("Rerun Program to try again")

# Worked with Jyle
if __name__ == "__main__":
    print_rows(board)
    print()
    random_bombs()
    play_game = str(input("Do you want to play the game? Yes or No: "))
    # Calls place_flag function
    flag_place(play_game)
