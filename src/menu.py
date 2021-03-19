import pygame
import sys
from pygame.locals import *

# Setting up window
master_ticker = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Stalin')
screen = pygame.display.set_mode((600, 800), 0, 32)

# importing images
bg = pygame.image.load("retro1.jpeg")
bg = pygame.transform.scale(bg, (600, 800))

bg2 = pygame.image.load("retro2.jpeg")
bg2 = pygame.transform.scale(bg2, (600, 800))

bg3 = pygame.image.load("retro3.jpeg")
bg3 = pygame.transform.scale(bg3, (600, 800))

# START UP THE SOUNDTRACK BABBYYYYY
pygame.mixer.init()
pygame.mixer.music.load("koroben.mp3")
# create array of all songs
songs = ["koroben.mp3", "farewell8bit.mp3"]
# set up fonts to use
small_font = pygame.font.SysFont(None, 30)
big_Font = pygame.font.SysFont(None, 100)


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


def main_menu():
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
                game()
        if sec_but.collidepoint((mx, my)):
            if click:
                # open manual
                manual()
        if opt_but.collidepoint((mx, my)):
            if click:
                # open options
                options()

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

        pygame.display.update()
        master_ticker.tick(60)


def game():
    running = True
    screen.fill((0, 0, 0))
    screen.blit(bg2, (0, 0))
    while running:
        draw_text('game', small_font, (255, 255, 255), screen, 20, 20)
        running = eventCheck()
        pygame.display.update()
        master_ticker.tick(60)


def manual():
    running = True
    screen.fill((0, 0, 0))
    while running:
        draw_text('Game Manual', small_font, (0, 255, 255), screen, 20, 20)
        draw_text('We have 3 new piece types as shown below', small_font, (0, 255, 255), screen, 20, 60)
        running = eventCheck()
        pygame.display.update()
        master_ticker.tick(60)


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



def options():
    click = False
    loop_inc = 0
    running = True
    screen.fill((0, 0, 0))
    screen.blit(bg3, (0, 0))

    while running:
        # get loc of mouse
        mx, my = pygame.mouse.get_pos()
        # draw text
        draw_text('Change music preset!', small_font, (0, 255, 255), screen, 20, 20)
        draw_text('start Legacy edition!', small_font, (0, 255, 255), screen, 20, 60)
        music_but = pygame.Rect(50, 300, 200, 50)
        pygame.draw.rect(screen, (150, 0, 0), music_but)
        if music_but.collidepoint((mx,my)):
            if click:
                loop_inc = loop_inc + 1
                loop_inc = change_song(loop_inc)

        draw_text('Change Music', small_font, (0, 255, 255), screen, 50, 300)
        click = False
        # Manual Event check for secondary buttons
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
        pygame.display.update()
        master_ticker.tick(60)


main_menu()
