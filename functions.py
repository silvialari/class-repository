import math
import numpy as np
import pandas as pd


def math_question1(a, b):
    """
    A function that takes two integers (x and y) and returns a list of numbers
    between x and y that are divisible by 5 but not by 7

    :param int  x: first integer in range
    :param int  y: second integer in range
    :return list of numbers between x and y divisible by 5, but not by 7, else None
    """
    try:
        return [number for number in range(a, b) if number % 5 == 0 and number % 7 != 0] or None
    except TypeError:
        return None


def math_question2(a, b):
    """
    A function that takes two numbers (x and y) as input and returns the value to
    the following function:

    f(x) = x * y iff x >= 0, y >= 0, 0 otherwise

    :param int  a: first integer
    :param int  b: second integer
    :return value of function, None if invalid values passed
    """
    l_function = lambda x, y: x * y if x >= 0 and y >= 0 else 0   # noqa: E731
    try:
        return l_function(a, b)
    except TypeError:
        return None


def math_question3(x, b):
    """
    A function that takes two integers (x and b) as inputs and returns a string
    that represents the number x in base b

    Example 1: if x=5 and b=2 then the function will return "101"
    Example 2: if x=5 and b=3 then the function will return "12"

    :param int  x: integer
    :param int  b: base
    :return value of function, None if invalid values passed
    """
    try:
        return int(np.base_repr(x, base=b))
    except TypeError:
        return None


def _is_perfect_square(number):
    """
    Helper function used by oo_question1
    """
    # assuming check for integers only
    return int(math.isqrt(number)) ** 2 == number and number > 0


def oo_question1(n):
    """
    A generator that takes a number N and returns all perfect squares
    less than N. Hint: use yield

    Example 1: N=30 then the generator will give 1, 4, 9, 16, 25 sequentially

    :param int  n: input number
    :yield next perfect square number in range 0 to n
    """
    try:
        for number in range(n):
            if _is_perfect_square(number):
                yield number
    except TypeError:
        return None


def file_question1(text_file, phrase):
    """
    A function that takes a phrase and a text file as inputs.

    Note: Newline characters will not be included in the phrase.P

    :param  str text_file:  input filename
    :param  str phrase:   lookup phrase
    :return True if the phrase is found in the document and returns False otherwise.
    """
    with open(text_file, 'r') as input_file:
        for line in input_file:
            if phrase in line:
                return True

    return False


def file_question2(csv_file, col=0):
    """
    Give a Comma Separated File (csv) and a column number (zero being the left most column)
    return the sum of all the entries in that column Assume that all the entries in the CSV
    are numbers.
    Assume also that there are no column headers.

    :param str csv_file: input csv file
    :param int col: column to sum
    :return sum of all entries in column

    """
    df = pd.read_csv(csv_file, header=None)
    try:
        return df[col].sum(axis=0)
    except KeyError:
        return None


def rook_movement(moves):
    """
    You have a chessboard with only the Rook on it. The Rook can move up, down, left
    or right from your perspective. Write a function (or a class) that takes a
    series of movements and at the end of the sequence of movements prints two numbers:

    a. The distance traveled by the Rook
    b. How far away the Rook is from its starting point

    Assume that the chessboard has no edges (the rook can travel any distance in any direction)

    For example, if the Rook is moved in the following sequence (up 1, left 3, down 2), then the
    Rook as traveled a distance of 6 spaces, and is 4 spaces away from its starting point.

    :params list moves: pass a list of tuples indicating moves:
        [('up', 1), ('right', 3)]
    :returns distance, spaces traveled
    """
    # define movements: space travelled multipliers
    movements = {
            'up': 1,
            'down': -1,
            'left': -1,
            'right': 1
            }

    distance = 0
    spaces_away = 0

    for move in moves:
        direction, spaces = move
        move_distance_multiplier = movements.get(direction)
        spaces_away += spaces * move_distance_multiplier
        distance += spaces

    print('distance', abs(spaces_away))
    print('spaces', distance)


def tests():
    # math question 1
    assert math_question1(1, 100) == [5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 65, 75, 80, 85, 90, 95], "Valid test"  # noqa: E501
    assert math_question1('a', 'b') == None, "Invalid test: two chars"  # noqa: E711
    assert math_question1(-1, 2) == None, "Not in range"  # noqa: E711

    # math question 2
    assert math_question2(0, 5) == 0, "Valid values, x = 0"
    assert math_question2(10, 100) == 1000, "Valid values, x and y >= 0"
    assert math_question2(-1, 10) == 0, "Valid values, x < 0"
    assert math_question2('a', 5) == None, "Invalid input type"  # noqa: E711

    # math question 3
    assert math_question3(5, 3) == 12, "Valid test base 3"
    assert math_question3(5, 2) == 101, "Valid test base 2"
    assert math_question3('a', 3) == None, "Invalid input type"  # noqa: E711

    # oo question
    psquare = oo_question1(30)
    assert next(psquare) == 1, "Valid test. exp 1"
    assert next(psquare) == 4, "Valid test. exp 4"
    assert next(psquare) == 9, "Valid test. exp 9"
    assert next(psquare) == 16, "Valid test. exp 16"
    assert next(psquare) == 25, "Valid test. exp 25"

    # file question 1
    input_file = 'text_file.txt'

    phrase = 'Data Display Debugger'
    assert file_question1(input_file, phrase) == True, "Valid test. Phrase found"  # noqa: E712

    phrase = '1234ABCD #-!'
    assert file_question1(input_file, phrase) == False, "Valid test. Phrase not found"  # noqa: E712

    phrase = 'Eric is an IDE built on PyQt and the Scintilla editing component.'
    assert file_question1(input_file, phrase) == True, "Valid test. Longer phrase"  # noqa: E712

    # file question 2
    csv_file = 'csv_file.csv'

    assert file_question2(csv_file, col=0) == 15, "Valid test col 0"
    assert file_question2(csv_file, col=1) == 18, "Valid test col 1"
    assert file_question2(csv_file, col=2) == 21, "Valid test col 2"
    assert file_question2(csv_file, col=3) == 24, "Valid test col 3"
    assert file_question2(csv_file, col=4) == None, "Valid test non existing col"  # noqa: E711


if __name__ == '__main__':
    tests()
    print("all tests passed")

    print("\nRook movement: [('up', 1), ('left', 3), ('down', 2)]")
    rook_movement([('up', 1), ('left', 3), ('down', 2)])

    print("\nRook movement: [('up', 5), ('left', 3), ('down', 5)]")
    rook_movement([('up', 5), ('left', 3), ('down', 5)])
