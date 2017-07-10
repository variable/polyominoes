# encoding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
import itertools
import sys

def generate_coordinates(number):
    """
    Generator to generate variant shapes based on all combinations
    """

    tuples = []
    for y in range(number):
        for x in range(number):
            tuples.append((y, x))

    # combination, not permutation, because points are the same
    # eg. (0,0) and (0,1) is the same as (0,1) and (0,0) represented in diagram
    for coordinates in itertools.combinations(tuples, number):
        yield coordinates
