from src.object import Object
from src.config import BUILDING


class Building(Object):
    def __init__(
        self,
        game,
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

    def __update_color(self):
        if self._health / self._max_health >= 0.5:
            self._color = BUILDING["colors"][2]
        elif self._health / self._max_health >= 0.2:
            self._color = BUILDING["colors"][1]
        else:
            self._color = BUILDING["colors"][0]

    def damaged(self, damage: int):
        super().damaged(damage)
        self.__update_color()
