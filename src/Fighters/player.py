from src.Fighters.fighter import *


class Player(Fighter):
    def __init__(self, game, config: dict, name: str):
        super().__init__(
            game,
            config["symbol"],
            config["color"],
            config["starting_coords"][0],
            config["starting_coords"][1],
            config["damage"],
            config["health"],
            config["move_speed"],
            config["attack_speed"],
            config["sound_file"],
        )
        self._range = config["range"]
        self._last_direction = "d"
        self.control_keys = config["control_keys"]
        self.name = name
        self.ultimate_location = None
        self.last_ult = -1
        self.ult_attack = False

    def ultimate_attack(self):
        pass

    def ult_damage(self):
        pass

    def attacked_buildings(self):
        return set()

    def attack(self):
        if not super().attack():
            return

        buildings = self.attacked_buildings()
        for obj in buildings:
            obj.damaged(self._damage * (self.game.rage.get_active() + 1))

    def move(self, ch: str):
        prev_char = self._last_direction
        self._last_direction = ch
        if ch == "w":
            super().move(0, -1)
        elif ch == "a":
            super().move(-1, 0)
        elif ch == "s":
            super().move(0, 1)
        elif ch == "d":
            super().move(1, 0)
        else:
            self._last_direction = prev_char
            if ch == "x":
                self.ultimate_attack()
            else:
                self.attack()
