import random
from calico_lib import make_sample_test, make_secret_test, make_data

def generate_square(length: int, width: int, side_min = 2, margin = 0) -> list[str]:
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

    art = art.split("\n")
    art.pop()

    return list(art)

def generate_triangle(length: int, width: int) -> list[str]:
    """
    Generate an ascii art of . and #, where the # form a right triangle.
    Its two sides are parallel to the x and y axis.
    The output is a string with rows separated by /n

    length: number of rows in the ascii art
    width: the number of symbols in each row
    """
    art = ['.'*width]*length

    # side length of triangle
    r = random.randint(2, min(length, width))

    px_max = length - r
    py_max = width - r

    px = random.randint(0, px_max)
    py = random.randint(0, py_max)

    o = random.randint(0, 3) # orientation
    for c1 in range(0, r):
        i = px + c1
        c2 = c1+1
        if o == 0:
            art[i] = '#'*c2 + '.'*(r-c2)
        if o == 1:
            art[i] = '.'*(r-c2) + '#'*c2
        if o == 2:
            art[i] = '#'*(r-c1) + '.'*c1
        if o == 3:
            art[i] = '.'*c1 + '#'*(r-c1)
        art[i] = '.'*py + art[i] + (width-py-r)*'.'

    return art

def generate_rect(length: int, width: int) -> list[str]:
    """
    Generate an ascii art of . and #, where the # form a right triangle.
    Its two sides are parallel to the x and y axis.

    length: number of rows in the ascii art
    width: the number of symbols in each row
    """
    art = ['.'*width]*length

    # side length of triangle
    r1 = random.randint(2, min(length, width))
    r2 = random.randint(2, min(length, width))

    px_max = length - r1
    py_max = width - r2

    px = random.randint(0, px_max)
    py = random.randint(0, py_max)

    for c1 in range(0, r1):
        i = px + c1
        art[i] = '.'*py + '#'*r2 + (width-py-r2)*'.'

    return art

if __name__ == '__main__':
    for i in range(100):
        for x in generate_triangle(10, 10):
            print(x)
        print()

    for i in range(100):
        for x in generate_rect(10, 10):
            print(x)
        print()
