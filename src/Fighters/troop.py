from src.Fighters.fighter import *


class Troop(Fighter):
    def __init__(
            self,
            game,
            symbol: str,
            color: str,
            startx: int,
            starty: int,
            damage: int,
            health: int,
            move_speed: int,
            attack_speed: int,
            building_preferences: list,
            collision_buildings: list = None
    ):
        super().__init__(
            game,
            symbol,
            color,
            startx,
            starty,
            damage,
            health,
            move_speed,
            attack_speed,
            collision_buildings
        )
        self._building_preferences = building_preferences
