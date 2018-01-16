
num_raw = 4
num_cls = 4;

sub_line = "+ - - - - "


def draw_plus_line():
    line = sub_line * (num_cls - 1) + "+"
    print(line)

def draw_regular_line():
    line = "|" + " " * 9 
    line = line * (num_cls)
    print(line)

def do_four(f):
    f()
    f()
    f()
    f()

def draw_4_regular_lines():
    do_four(draw_regular_line)

def do_three(f, g):
    f()
    g()
    f()
    g()
    f()
    g()

def do_square_4():
    do_three(draw_plus_line, draw_4_regular_lines)
    draw_plus_line()

do_square_4()
