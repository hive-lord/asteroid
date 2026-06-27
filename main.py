import pygame as pg

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfields = AsteroidField()
    player = Player(x, y)

    while True:
        log_state()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        pg.display.flip()


if __name__ == "__main__":
    main()
