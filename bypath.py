# encoding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
import itertools

def generate_coordinates(number):
    """
    Generator to generate variant shapes based on all combinations
    """

    def up((y, x)):
        return (y - 1, x)

    def left((y, x)):
        return (y, x - 1)

    def down((y, x)):
        return (y + 1, x)

    def right((y, x)):
        return (y, x + 1)

    tuples = []
    enlarge = 3
    for y in range(number * enlarge):
        for x in range(number * enlarge):
            tuples.append((y, x))

    # combination, not permutation, because points are the same
    # eg. (0,0) and (0,1) is the same as (0,1) and (0,0) represented in diagram
    coordinates = []
    for directions in itertools.permutations([up, left, down, right] * (number-1), number-1):
        # print directions
        coordinates = [(number, number)]
        for direction in directions:
            coordinates.append(direction(coordinates[-1]))
        yield coordinates
