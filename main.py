import random

# Defines circle flags for placement
def flag(x, y):
    circle = Circle(10)
    circle.set_color(Color.red)
    circle.set_position(x, y)
    add(circle)
# Creates the mouse event for clicks
add_mouse_click_handler(flag)