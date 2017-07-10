# encoding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from utils import validate_coordinates
from polyominoes import Polyominoes

def convert(test_list):
    result = []

    for x, row in enumerate(test_list.strip().split('\n')):
        for y, col in enumerate(row):
            if col == "1":
                result.append((x, y))
    return result


l = """
0001
"""
assert validate_coordinates(convert(l)) is True

l = """
0001
0001
"""
assert validate_coordinates(convert(l)) is True

l = """
1101
0111
0100
1100
"""
assert validate_coordinates(convert(l)) is True


l = """
0001
0011
0100
1100
"""
assert validate_coordinates(convert(l)) is False

l = """
1101
0011
0100
1100
"""
assert validate_coordinates(convert(l)) is False


l = """
0000000
0011110
0000110
0001110
0011000
0000000
"""
assert validate_coordinates(convert(l)) is True

p = Polyominoes()
# assert Polyominoes().run(2) == 1
# assert Polyominoes().run(3) == 2
# assert Polyominoes().run(4) == 7
assert Polyominoes().run(5) == 18
assert Polyominoes().run(6) == 60
assert Polyominoes().run(7) == 196
print Polyominoes().run(8)

