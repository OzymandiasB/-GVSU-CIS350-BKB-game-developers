import pygame
import random
import shape



# Game Logic (model)
class Game:
    level = 1
    # start score at 10 so power up works later on
    score = 10
    board = []
    # How big the board is
    width = 15
    height = 30
    shapes = None
    game_over = False
    is_legacy = False
    song_switch = False

    def __init__(self, is_leg):
        self.is_legacy = is_leg
        # instantiate the board
        for i in range(30):
            line = []  # create new row
            for j in range(15):
                line.append(0)
            self.board.append(line)  # Add row onto board

    # Spawn in new Shape in the center
    def new_piece(self):
        self.shapes = shape.Shape(7, 0, self.is_legacy)
        # After spawning new shape, check if game is over
        if self.is_blocked():
            print("Game Over")
            self.game_over = True

    # check if the shape is being blocked by wall or other shape
    def is_blocked(self):
        blocked = False
        mat_length = 4
        for i in range(mat_length):  # Loop through outer shape Matrix
            for j in range(mat_length):  # Loop through inner shape Matrix
                temp = self.shapes.get_shape()  # extract figure to run bound tests
                board_length = 4
                # check to see if shape itself can fit on location
                if temp.__contains__(i * board_length + j):
                    # Horizontal Axis bound check
                    if self.width - 1 < j + self.shapes.x:
                        return True
                    if j + self.shapes.x < 0:
                        return True
                    # Vertical check
                    if self.height - 1 < i + self.shapes.y:
                        return True
                    # Check to see if blocked by another shape
                    if self.board[i + self.shapes.y][j + self.shapes.x] != 0:  # if 0 then this area was not occupied
                        return True

        return False

    # Clears Clearable lines aha, i have been debugging this for one hour if this does no work i will shoot myself
    def clear_lines(self, row):
        # Do a bottom up approach
        pt = row
        # start at row needed
        while pt > 1:
            # scan through entire width of board, clearing out each element
            for w in range(self.width):
                self.board[pt][w] = 0  # make spot on board empty
            pt = pt - 1

    # Check to see if lines can be cleared,
    def check_lines(self):
        # track how many rows were cleared
        counter = 0
        for i in range(1, self.height):
            row_empty = False
            for j in range(self.width):
                # check to see if any spot in row was empty
                if self.board[i][j] == 0:
                    # if spot was empty, mark it
                    row_empty = True
            if row_empty:
                # reset counter of lines if previous row had empty element
                counter = 0
            else:  # else clear out the lines
                counter = counter + 1
                self.clear_lines(i)
                self.song_switch = True
        self.score = self.score + counter * 5

        # if the score is high enough trigger the power up
        if self.score % 100 == 0:
            self.power_up()
            self.score = self.score * 2

    # Holds shape in place after dropping it.
    def lock_shape(self):
        mat_length = 4
        for row in range(mat_length):  # Loop through outer shape Matrix
            for col in range(mat_length):  # Loop through inner shape Matrix
                temp = self.shapes.get_shape()
                if temp.__contains__(row * mat_length + col):
                    # if the figure is correctly centered; lock it in that board space
                    self.board[row + self.shapes.y][col + self.shapes.x] = 1  # turn locked into grey like tetris effect
        # check if you can now clear any lines
        self.check_lines()
        # spawn in new figure
        self.new_piece()

    # Move shape down
    def shape_down(self):
        self.shapes.y = self.shapes.y + 1
        # Check to see if its still in bounds
        if self.is_blocked():
            # if blocked push the shape up one and lock it in
            self.shapes.y = self.shapes.y - 1
            self.lock_shape()

    # Move shape to the left
    def shape_left(self):
        self.shapes.x = self.shapes.x - 1
        if self.is_blocked():
            # if blocked go back to old position
            self.shapes.x = self.shapes.x + 1

    # Move shape to the right
    def shape_right(self):

        self.shapes.x = self.shapes.x + 1
        if self.is_blocked():
            # if blocked go back to old position
            self.shapes.x = self.shapes.x - 1

    # Rotate shape
    def shape_rotate(self):
        # save previous rotation
        temp = self.shapes.shape_rotation
        # check to see if rotate works
        self.shapes.rotate()
        # if it doesnt go back to previous rotation
        if self.is_blocked():
            self.shapes.shape_rotation = temp

    # this is the power up that clears everything on the screen
    def power_up(self):
        for pt in range(self.height):
            # scan through entire width of board, clearing out each element
            for w in range(self.width):
                self.board[pt][w] = 0  # make spot on board empty
