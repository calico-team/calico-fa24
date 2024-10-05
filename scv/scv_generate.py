import random
from calico_lib import make_sample_test, make_secret_test, make_data

def generate_square(length: int, width: int, side_min = 2, margin = 1) -> str:
    """
    Generate an ascii art of . and #, where the # form a square
    The output is a string with rows separated by /n
    
    length: number of rows in the ascii art
    width: the number of symbols in each row
    side_min: minimum side length of the square inside
    margin: minimum number of . that line the border of the ascii
    """
    assert length >= margin * 2 + side_min
    assert width >= margin * 2 + side_min

    buffer = margin * 2

    side_length = random.randint(side_min, min(length, width) - buffer)

    buffer = side_length + margin

    upper_left_y = random.randint(margin, length - buffer)
    upper_left_x = random.randint(margin, width - buffer)

    art = ("." * width + "\n") * upper_left_y
    art += ("." * upper_left_x + "#" * side_length + "." * (width - upper_left_x - side_length) + "\n") * side_length
    art += ("." * width + "\n") * (length - upper_left_y - side_length)

    return art

def generate_triangle(length: int, width: int, x_min = 2, y_min = 2, margin = 1) -> str:
    """
    Generate an ascii art of . and #, where the # form a right triangle.
    Its two sides are parallel to the x and y axis.
    The output is a string with rows separated by /n
    
    length: number of rows in the ascii art
    width: the number of symbols in each row
    x_min: minimum base length of the triangle 
    y_min: minimum height of the triangle
    margin: minimum number of . that line the border of the ascii
    """
    assert length >= margin * 2 + y_min
    assert width >= margin * 2 + x_min

    buffer = margin * 2

    side_x = random.randint(x_min, width - buffer)
    side_y = random.randint(y_min, length - buffer)

    buffer_x = side_x + margin
    buffer_y = side_y + margin

    upper_left_y = random.randint(margin, length - buffer_y)
    upper_left_x = random.randint(margin, width - buffer_x)

    skip_x = random.randint(0, 1)
    skip_y = random.randint(0, 1)

    art = ("." * width + "\n") * upper_left_y
    for index in range(side_y):
        art += "." * upper_left_x 

        top_down = int((side_y - index - 1) / (side_y - 1) * (side_x - 1)) + 1
        bottom_up = int(index / (side_y - 1) * (side_x - 1)) + 1

        art += ("." * (side_x - bottom_up) + "#" * (bottom_up)) * ((1 - skip_x) * (1 - skip_y))
        art += ("." * (side_x - top_down) + "#" * (top_down)) * ((1 - skip_x) * skip_y)
        art += ("#" * (bottom_up) + "." * (side_x - bottom_up)) * (skip_x * (1 - skip_y))
        art += ("#" * (top_down) + "." * (side_x - top_down)) * (skip_x * skip_y)

        art += "." * (width - upper_left_x - side_x) + "\n"

    art += ("." * width + "\n") * (length - upper_left_y - side_y)

    return art
    
