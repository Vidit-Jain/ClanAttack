from src.object import Object
from src.config import *
import time


class Fighter(Object):
    def __init__(self, game, symbol, color, startx, starty, damage, health, move_speed):
        super().__init__(
            game,
            symbol,
            color,
            startx,
            starty,
            FIGHTER["height"],
            FIGHTER["width"],
            health,
        )
        self.damage = damage
        self.move_speed = move_speed
        self.last_moved = 0

    def boundmovement(self, x, y):
        if self.x[0] + x < 0:
            x = -self.x[0]
        if self.x[1] + x > GAME["window"]["width"]:
            x = GAME["window"]["width"] - self.x[1]

        if self.y[0] + y < 0:
            y = -self.y[0]
        if self.y[1] + y > GAME["window"]["height"]:
            y = GAME["window"]["height"] - self.y[1]
        return x, y

    def move(self, x, y):
        if time.monotonic() - self.last_moved < 1 / self.move_speed:
            return

        x, y = self.boundmovement(x, y)
        self.game.screen.remove(self)
        self.x = [self.x[0] + x, self.x[1] + x]
        self.y = [self.y[0] + y, self.y[1] + y]
        self.game.screen.add(self)
        self.last_moved = time.monotonic()
