import pygame
import random
import shape


# class that controls the game menu
class Game:
    level = 1
    score = 0
    board = []
    width = 800  # Taken from menu dimensions
    height = 800  # Taken from menu dimensions
    shapes = None

    def __init__(self):
        # Create dashed marks to simulate the board of tetris
        for i in range(800):
            line = []  # create new dash mark array
            for j in range(800):
                line.append(0)
                self.board.append(line)  # Add line into board

    # Create new shape
    def new_piece(self):
        self.shapes = shape.Shape(0, 3)

    # check if the shape is being blocked by wall or other shape
    def is_blocked(self):
        blocked = False
        for i in range(4):  # Loop through outer shape Matrix
            for j in range(4):  # Loop through inner shape Matrix
                blocked = self.bound_check(i, j)

    def bound_check(self, row, col):
        temp = self.shapes.get_figure()  # extract figure to run bound tests
        board_length = 4
        # check to see if shape itself can fit on location
        if temp.__contains__(row * board_length + col):
            # Horizontal Axis bound check
            if self.width - 1 < col + self.shapes.x:
                return True
            elif col + self.shapes.x < 0:
                return True
            # Vertical check
            elif self.height - 1 < row + self.shapes.y:
                return True
            # Check to see if blocked by another shape
            elif self.board[row + self.shapes.y][col + self.shapes.x] != 0:  # if 0 then this area was not occupied
                return True
        return False
