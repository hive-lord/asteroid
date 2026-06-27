import pygame as pg

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pg.Vector2]:
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> float:
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def update(self, dt: float) -> None:
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rotate(-1 * dt)
        if keys[pg.K_d]:
            self.rotate(dt)
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-1 * dt)

    def move(self, dt: float) -> None:
        unit_vector = pg.Vector2(0, 1)
        unit_vector = unit_vector.rotate(self.rotation)
        dist = unit_vector * PLAYER_SPEED * dt
        self.position += dist
