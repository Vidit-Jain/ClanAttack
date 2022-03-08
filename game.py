from src.game_input import *
from src.screen import *
from src.Fighters.king import *
from src.Buildings.townhall import *
from src.Buildings.spawnpoint import *
from src.Buildings.hut import *
from src.Buildings.cannon import *
from src.Buildings.wall import *
from src.config import *
from src.helper import *
from src.spell import *


class Game:
    def __init__(self):
        self.king = None
        self.townhall = None
        self.input = Get()
        self.screen = Screen()
        self.rageSpell = Rage(self)
        self.healSpell = Heal(self)
        self.rageActive = False

        add_king(self)
        add_townhall(self)

        add_spawnpoints(self)
        add_huts(self)
        add_walls(self)
        add_cannons(self)
        self.barbarians = []

    def handle_input(self):
        ch = input_to(self.input)
        if ch in KING["control_keys"]:
            self.king.move(ch)
        elif ch in SPAWNPOINT["control_keys"]:
            self.barbarians.append(spawn(game, ch))
        elif ch in SPELL["control_keys"]:
            use_spell(self, ch)
        if ch == "c":
            return 1
        return 0

    def loop(self):
        while 1:
            self.screen.clear()
            self.screen.add_to_screen(self)
            self.rageSpell.check_expired()
            shoot_cannons(game)
            move_barbarians(game)
            remove_destroyed(game)
            self.screen.render()
            if self.handle_input() == 1:
                break


game = Game()
erase_screen()
game.loop()
