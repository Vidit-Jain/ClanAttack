from src.Fighters.fighter import *


class King(Fighter):
    def __init__(self, game):
        super().__init__(
            game,
            KING["symbol"],
            KING["color"],
            KING["starting_coords"][0],
            KING["starting_coords"][1],
            KING["damage"],
            KING["health"],
            KING["move_speed"],
            KING["attack_speed"],
        )
        self.range = KING["range"]

    # def attack(self, obj):
    #     if obj is None:
    #         return
    #     if time.monotonic() - self.last_attacked < 1 / self.attack_speed:
    #         return
    #     self.last_attacked = time.monotonic()
    #     obj.damaged(self.damage)

    # def loop_attack(self, obj_list: list[Object]):
    #     if obj_list is not None:
    #         for obj in obj_list:
    #             point = self.__cl
    #             if self.__dist()
    #                 return obj
    #     return None

    # def attack(self):
    #     if time.monotonic() - self.last_attacked < 1 / self.attack_speed:
    #         return
    #     self.last_attacked = time.monotonic()
    #     obj = self.loop_collide(self.game.huts)
    #     if obj is None:
    #         obj = self.loop_collide(self.game.walls)
    #     if obj is None:
    #         obj = self.loop_collide(self.game.cannons)
    #     if obj is None and self.game.townhall is not None:
    #         obj = self.loop_collide([self.game.townhall])

    def attack_loop(self, obj_list, buildings: set):
        for obj in obj_list:
            x, y = self.closest_point(obj)
            if abs(x - self.x[0]) + abs(y - self.y[0]) <= self.range:
                buildings.add(obj)

    def attack(self):
        if time.monotonic() - self.last_attacked < 1 / self.attack_speed:
            return
        self.last_attacked = time.monotonic()
        buildings = set()
        self.attack_loop(self.game.huts, buildings)
        self.attack_loop(self.game.walls, buildings)
        self.attack_loop(self.game.cannons, buildings)

        x, y = self.closest_point(self.game.townhall)
        if abs(x - self.x[0]) + abs(y - self.y[0]) <= self.range:
            buildings.add(self.game.townhall)
        for obj in buildings:
            obj.damaged(self.damage * (self.game.rageActive + 1))

    def move(self, ch: str):
        if ch == "w":
            super().move(0, -1)
        elif ch == "a":
            super().move(-1, 0)
        elif ch == "s":
            super().move(0, 1)
        elif ch == "d":
            super().move(1, 0)
        else:
            self.attack()


def add_king(game):
    game.king = King(game)
