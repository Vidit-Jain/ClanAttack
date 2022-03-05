from src.object import Object
from src.config import *


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
