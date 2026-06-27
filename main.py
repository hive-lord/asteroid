import pygame as pg
from pygame import Surface, display

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        pg.display.flip()


if __name__ == "__main__":
    main()
