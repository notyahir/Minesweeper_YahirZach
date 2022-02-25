import random

# Defines circle flags for placement
def flag(x, y):
    circle = Circle(10)
    circle.set_color(Color.red)
    circle.set_position(x, y)
    add(circle)
# Creates the mouse event for clicks
add_mouse_click_handler(flag)

# A check on the board places that have been flagged
flag = []
# Idk was hoping this might get rid of the flag if one is already in that position
if [x, y] in flag
    clear()