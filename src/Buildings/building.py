from src.object import Object
from src.config import BUILDING, COLORS


class Building(Object):
    def __init__(
        self,
        game,
        building_type: str,
        symbol: str,
        startx: int,
        starty: int,
        height: int,
        width: int,
        health: int,
    ):
        super().__init__(
            game, symbol, BUILDING["colors"][-1], startx, starty, height, width, health
        )
        self.building_type = building_type

    def __update_color(self):
        if self.health / self.max_health >= 0.5:
            self.color = COLORS["GREEN"]
        elif self.health / self.max_health >= 0.2:
            self.color = COLORS["YELLOW"]
        else:
            self.color = COLORS["RED"]

    def damaged(self, damage: int):
        self.health -= damage
        self.__update_color()
        if self.health <= 0:
            self.game.x = 1
            self.destroyed = True


