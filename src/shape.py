import pygame
import random


# create shapes and initialize their locations in the game
# Shape initialization follows this pattern
#       0   1   2   3
#       4   5   6   7
#       8   9   10  11
#       12  13  14  15
#
#
class Shape:
    shapes = [
        [[2, 6, 10, 14], [4, 5, 6, 7]],  # stick shape
        [[2, 5, 6, 7], [2, 5, 6, 10], [5, 6, 7, 10], [2, 6, 7, 10]],  # tetramino shape
        [[1, 2, 5, 6]],  # Cube shape
        [[2, 3, 5, 6], [1, 5, 6, 10]],  # Squiggly Shape
        [[2, 6, 10, 11], [3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9]],  # L shape
        [[6]],  # Custom pointer shape
        [[1, 2, 3, 5, 7], [1, 2, 6, 9, 10], [5, 7, 9, 10, 11], [1, 2, 5, 9, 10]],  # Custom C shape
        [[3, 5, 7, 9, 10, 11], [0, 4, 6, 8, 9, 10], [0, 1, 2, 4, 6, 8], [1, 2, 3, 5, 7, 11], [5, 6, 10, 12, 13, 14],
         [5, 6, 9, 13, 14, 15], [0, 1, 2, 6, 10, 9], [1, 2, 3, 5, 9, 10]]  # custom J shape

    ]
    # for legacy mode
    legacy_shapes = [
        [[2, 6, 10, 14], [4, 5, 6, 7]],  # stick shape
        [[2, 5, 6, 7], [2, 5, 6, 10], [5, 6, 7, 10], [2, 6, 7, 10]],  # tetramino shape
        [[1, 2, 5, 6]],  # Cube shape
        [[2, 3, 5, 6], [1, 5, 6, 10]],  # Squiggly Shape
        [[2, 6, 10, 11], [3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9]],  # L shape
    ]

    # init coordinates to start with
    x = 0
    y = 0

    # constructor for shape
    def __init__(self, x, y,leg):
        self.x = x
        self.y = y
        if leg:
            self.shapes = self.legacy_shapes
        self.shape_type = random.randint(0, len(self.shapes) - 1)  # location in outer shape array
        self.shape_rotation = 0  # which rotation it is in (location in inner most shape array)

    # retrieve shape figure from shapes array
    def get_shape(self):
        return self.shapes[self.shape_type][self.shape_rotation]

    def rotate(self):
        # if rotation possible, rotate otherwise reset rotation on array
        if self.shape_rotation + 1 < len(self.shapes[self.shape_type]):
            self.shape_rotation = self.shape_rotation + 1
        else:
            self.shape_rotation = 0
