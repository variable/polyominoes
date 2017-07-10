# encoding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

def validate_coordinates(coordinates):
    """
    check if adjacent point exist
    first, group the points by adjcent ones
    then through recursive call to merge the groups into final form
    """
    coordinates_set = set(coordinates)

    def get_adjacent_points(coordinates, point):
        x, y = point
        # check up left right down exists
        up = (x + 1, y)
        left = (x, y - 1)
        down = (x - 1, y)
        right = (x, y + 1)
        return coordinates_set.intersection(set([up, down, left, right]))

    def traverse_combination(coordinates, point, traversed):
        if point not in traversed:
            traversed.append(point)
        # get the coordinates around the point
        adjacent_points = get_adjacent_points(coordinates, point)

       # get the adjacent points that not been traversed
        adjacent_points = adjacent_points - set(traversed)

        for adjacent_point in adjacent_points:
            traverse_combination(coordinates, adjacent_point, traversed)

    traversed = []
    traverse_combination(coordinates, coordinates[0], traversed)

    return len(traversed) == len(coordinates)

def convert_to_shape(coordinates):
    return [[1 if (x, y) in coordinates else 0 for y in range(len(coordinates))] for x in range(len(coordinates))]

def trim_shape(shape):
    """
    take out blank lines in the data store like
    xxx
      xxx
    # TODO: rotate the shape for vertical trim
    """

    # trim horizontally
    trimmed = []
    for row in shape:
        if any(row):
            trimmed.append(row)

    # trim vertically
    cols = []
    for x in range(len(trimmed[0])):
        if any([row[x] for row in shape]):
            cols.append(x)

    v_trimmed = []
    for y, row in enumerate(trimmed):
        new_row = []
        for y in cols:
            new_row.append(row[y])
        v_trimmed.append(new_row)

    return v_trimmed

def rotate_shape(shape):
    """
    rotate list 90 degrees
    after rotated result is in tuples, we need to turn everything to list
    """
    new_shape = []
    # borrowed from http://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
    rotated = zip(*shape[::-1])
    for row in rotated:
        new_shape.append([list(item) if isinstance(item, tuple) else item for item in row])
    return new_shape
