import random as rm

import pygame as pg

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = rm.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            rad = self.radius - ASTEROID_MIN_RADIUS
            ass1 = Asteroid(self.position.x, self.position.y, rad)
            ass2 = Asteroid(self.position.x, self.position.y, rad)
            ass1.velocity = v1 * 1.2
            ass2.velocity = v2 * 1.2
