import pygame
import sys
from pygame.locals import *
import game
pygame.draw



# Setting up window
master_ticker = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Stalin')
screen = pygame.display.set_mode((1024, 1000), 0, 32)

# importing images
bg = pygame.image.load("retro1.jpeg")
bg = pygame.transform.scale(bg, (1024, 1000))

bg2 = pygame.image.load("retro2.jpeg")
bg2 = pygame.transform.scale(bg2, (1024, 1000))

bg3 = pygame.image.load("retro3.jpeg")
bg3 = pygame.transform.scale(bg3, (1024, 1000))

play_sprite = pygame.image.load("play.png").convert_alpha()
play_sprite = pygame.transform.scale(play_sprite, (150, 150))

# START UP THE SOUNDTRACK BABBYYYYY
pygame.mixer.init()
pygame.mixer.music.load("koroben.mp3")
# create array of all songs
songs = ["koroben.mp3", "farewell8bit.mp3"]
# set up fonts to use
small_font = pygame.font.SysFont(None, 30)
big_Font = pygame.font.SysFont(None, 100)
# set up colors
white = (255, 255, 255)
grey = (128, 128, 128)


# function to write text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_box = text_obj.get_rect()
    text_box.topleft = (x, y)
    surface.blit(text_obj, text_box)


click = False


# Navigation controls
def eventCheck():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
    return True


def main_menu(loop_inc):
    pygame.mixer.music.play()
    while True:
        # keep resetting and adding in bgImage
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        draw_text('Main Menu', big_Font, (255, 255, 255), screen, 20, 20)
        # get mouse loc
        mx, my = pygame.mouse.get_pos()

        # create buttons
        first_but = pygame.Rect(50, 100, 200, 50)
        sec_but = pygame.Rect(50, 200, 200, 50)
        opt_but = pygame.Rect(50, 300, 200, 50)
        # check what was clicked
        if first_but.collidepoint((mx, my)):
            if click:
                # start game
                game_menu()
        if sec_but.collidepoint((mx, my)):
            if click:
                # open manual
                manual()
        if opt_but.collidepoint((mx, my)):
            if click:
                # open options
                options(loop_inc)

        pygame.draw.rect(screen, (150, 0, 0), first_but)
        draw_text('Play Game', small_font, (255, 255, 255), screen, 50, 100)
        pygame.draw.rect(screen, (150, 0, 0), sec_but)
        draw_text('Game Manual', small_font, (255, 255, 255), screen, 50, 200)
        pygame.draw.rect(screen, (150, 0, 0), opt_but)
        draw_text('Game Options', small_font, (255, 255, 255), screen, 50, 300)

        click = False
        # Second Set Navigation Controls
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        draw_text('Developed by BKB Game Developers', small_font, (255, 255, 255), screen, 50, 750)

        pygame.display.update()
        master_ticker.tick(60)


def game_menu():
    # insert call into game here
    running = True
    screen.fill((0, 0, 0))
    screen.blit(bg2, (0, 0))
    engine = game.Game()

    while running:
        if engine.shapes is None:
            engine.new_piece()
        draw_text('game', small_font, (255, 255, 255), screen, 20, 20)
        running = eventCheck()
        pygame.display.update()
        master_ticker.tick(60)
        # Draw grid on page
        draw_grid(engine)
        # As long as shape currently exists
        if engine.shapes is not None:
            draw_shapes(engine)


def manual():

    running = True
    screen.fill((0, 0, 0))
    while running:

        mx, my = pygame.mouse.get_pos()

        draw_text('Game Manual', small_font, (0, 255, 255), screen, 20, 20)
        draw_text('We have 3 new piece types as shown below', small_font, (0, 255, 255), screen, 20, 60)
        draw_text('The Pointer Shape!', small_font, (0,255,255), screen, 20, 100)
        draw_text('The C shape!', small_font, (0, 255, 255), screen, 20, 270)
        draw_text('The J-Block Shape!', small_font, (0, 255, 255), screen, 20, 500)
        draw_text('This updated version of Tetris is simple to play! Just use your arrow keys to move left and right ', small_font, (0, 255, 255), screen, 20, 715)
        draw_text('to move falling blocks in the place you wish them to fall! ', small_font, (0, 255, 255), screen, 20, 740)
        draw_text('These new blocks that are now implemented make the game more fun and stretch your brain a little! ', small_font, (0, 255, 255), screen, 20, 780)


        # pointer shape picture

        pygame.draw.rect(screen, (0,255,255) , [75,165,50,50])

        # C shape picture

        pygame.draw.rect(screen, (0, 255, 255), [75, 325, 50, 150])
        pygame.draw.rect(screen, (0, 255, 255), [75, 325, 150, 45]) # top
        pygame.draw.rect(screen, (0, 255, 255), [75, 430, 150, 45]) # bottom

        # J-Block shape picture

        pygame.draw.rect(screen, (0, 255, 255), [75, 550, 50, 150])
        pygame.draw.rect(screen, (0, 255, 255), [75, 655, 150, 45])
        pygame.draw.rect(screen, (0, 255, 255), [175, 610, 50, 90])


    # back button implementation
        back_but = pygame.Rect(775, 30, 200, 50)
        pygame.draw.rect(screen, (0, 0, 255), back_but)
        draw_text('ESC to Menu', small_font, (255, 255, 255), screen, 810, 45)

    # back button logic




        running = eventCheck()
        pygame.display.update()
        master_ticker.tick(60)


# helper method that draws shapes
def draw_shapes(eng):
    shape_mat = 4  # length of shape matrix defined in shape class
    for i in range(shape_mat):
        for j in range(shape_mat):
            # grab shape to run check on it
            temp = eng.shapes.get_shape()
            shape_check = (i * shape_mat) + j
            # if the shapes area checks out, makes the coords for rect
            if shape_check in temp:
                loc_x = j + eng.shapes.x
                loc_y = i + eng.shapes.y
                # 190 is the grids start x location & 60 is grids y start loc
                rect_coord = [(30 * loc_x) + 191, (30 * loc_y) + 61, 28, 28]
                # draw rectangle that represents shape
                pygame.draw.rect(screen, white, rect_coord)


# Helper method to draw the grid
def draw_grid(eng):
    # Loop through size of grid
    for i in range(eng.height):
        for j in range(eng.width):
            # 190 is where grid starts, 60 is y of where it starts
            rect_coor = [(30 * j) + 190, 60 + (30 * i), 30, 30]
            pygame.draw.rect(screen, grey, rect_coor, 1)
            if eng.board[i][j] != 0:
                # of there is a shape there
                rect_coor = [eng.shapes.x + (30 * j) + 1, eng.shapes.y + (30 * i) + 1, 28, 29]
                pygame.draw.rect(screen, grey, rect_coor)


def change_song(loop_inc):
    if loop_inc >= len(songs):
        pygame.mixer.music.fadeout(30)
        pygame.mixer.music.unload()
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()
        return 0
    else:
        pygame.mixer.music.fadeout(30)
        pygame.mixer.music.unload()
        pygame.mixer.music.load(songs[loop_inc])
        pygame.mixer.music.play()
        return loop_inc


def options(loop_inc):
    click = False
    running = True
    screen.fill((0, 0, 0))
    screen.blit(bg3, (0, 0))

    while running:
        # get loc of mouse
        mx, my = pygame.mouse.get_pos()
        # draw text
        draw_text('Change music preset!', small_font, (0, 255, 255), screen, 20, 20)
        draw_text('start Legacy edition!', small_font, (0, 255, 255), screen, 20, 60)

        # create legacy button
        legacy_but = pygame.Rect(50, 150, 200, 50)
        # Create music Button
        music_but = pygame.Rect(75, 250, 150, 150)
        # pygame.draw.rect(screen, (0, 150, 0), music_but)
        screen.blit(play_sprite, (50, 250))


        # display legacy button
        pygame.draw.rect(screen, (0, 0, 255), legacy_but)
        draw_text('Legacy Mode', small_font, (255, 255, 255), screen, 50, 155)

        # legacy button logic
        if legacy_but.collidepoint((mx, my)):
            if click:
                return


        if music_but.collidepoint((mx, my)):
            if click:
                loop_inc = loop_inc + 1
                loop_inc = change_song(loop_inc)

        # draw_text('Change Music', small_font, (0, 255, 255), screen, 50, 300)
        click = False
        # Manual Event check for secondary buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        master_ticker.tick(60)


loop_inc = 0
main_menu(loop_inc)
