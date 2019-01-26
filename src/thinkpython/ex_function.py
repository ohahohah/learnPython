# Think Python e2 - ch03.Functions exercise


# ex 3-1.
'''
Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the string is in column 70
of the display
'''


def right_justify(s):
    prefix_blank = ' ' * (70 - len(s))
    print(prefix_blank, s)


# ex 3-2
'''
Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four.
'''


def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


# ex 3-3
def print_updown_side(col_size):
    for i in range(col_size):
        print('+', '-' * 4, end='')
    print('+')


def print_middle(col_size):
    for i in range(4):
        for j in range(col_size):
            print('|', ' ' * 4, end='')
        print('|')


def print_two_by_two_lattice():
    print_updown_side(2)
    print_middle(2)

    print_updown_side(2)
    print_middle(2)

    print_updown_side(2)


# ex 3-4
'''
Write a function that draws a similar grid with four rows and four columns.
'''


def print_lattice(row_size, col_size):
    for i in range(row_size):
        print_updown_side(col_size)
        print_middle(col_size)
    print_updown_side(row_size)


# ex 3-4 not using for statement
# hint from http://thinkpython2.com/code/grid.py
def do_two_times(func):
    func()
    func()


def do_four_times(func):
    do_two_times(func)
    do_two_times(func)


def one_four_one(f, g, h):
    f()
    do_four_times(g)
    h()


def print_plus():
    print('+', end='')


def print_dash():
    print('-', end='')


def print_bar():
    print('|', end='')


def print_space():
    print(' ', end='')


def print_newLine():
    print()


def print_space_check():
    print('a', end='')


def do_nothing():
    pass


def print_post_module():
    one_four_one(print_bar, print_space, do_nothing)


def print_4post_one_row():
    one_four_one(do_nothing, print_post_module, print_bar)
    print_newLine()


def print_beam():
    one_four_one(do_nothing, print_dash, print_plus)


def print_4beams():
    one_four_one(print_plus, print_beam, print_newLine)


def print_module():
    one_four_one(do_nothing, print_4post_one_row, do_nothing)
    print_4beams()


def print_four_by_four_square():
    one_four_one(print_4beams, print_module, do_nothing)


if __name__ == "__main__":
    '''
    s = input()
    
    # 3-1
    #    right_justify(s)

    # 3-2
    do_twice(print_twice, s)
    print('')
    do_four(print_twice, s)
    
    # 3-3
    print_two_by_two_lattice()
    '''

    # 3-4
    print_lattice(4, 4)

    # 3-4 not using for statement
    print_four_by_four_square()
