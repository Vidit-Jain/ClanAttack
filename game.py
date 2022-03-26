from src.game_input import *
from src.screen import *
from src.Fighters.king import *
from src.Buildings.townhall import *
from src.Buildings.spawnpoint import *
from src.Buildings.hut import *
from src.Buildings.cannon import *
from src.Buildings.wall import *
from src.helper import *
from src.spell import *


class Game:
    def __init__(self):
        self.king = None
        self.townhall = None
        self.input = Get()
        self.screen = Screen()
        self.rage = Rage(self)
        self.healSpell = Heal(self)
        self.barbarian_count = GAME["barbarian_count"]
        self.game_end = 0
        self.game_result = 0
        self.frames = []
        add_townhall(self)

        add_spawnpoints(self)
        add_huts(self)
        add_walls(self)
        add_cannons(self)
        add_king(self)
        self.barbarians = []
        self.enemy_buildings = [self.huts, self.walls, self.cannons, self.townhall]
        self.imp_buildings = [self.huts, self.cannons, self.townhall]
        self.x = 1

    def handle_input(self):
        ch = input_to(self.input)
        if ch == "c":
            file = store_replay(self)
            print(self.x)
            print("Replay stored in replays/" + file)
            return 1
        # Don't process input if game over
        if self.game_end == 1:
            return 0
        if ch in KING["control_keys"] and self.king is not None:
            self.king.move(ch)
        elif ch in SPAWNPOINT["control_keys"]:
            spawn(game, ch)
        elif ch in SPELL["control_keys"]:
            use_spell(self, ch)
        return 0

    def loop(self):
        while 1:
            self.screen.clear()
            self.screen.add_to_screen(self)
            if self.game_end == 0:
                self.rage.check_expired()
                shoot_cannons(game)
                move_barbarians(game)
                remove_destroyed(game)
                game_ended(game)
            else:
                self.screen.add_game_end(self.game_result)

            self.screen.render(self)
            if self.handle_input() == 1:
                break


if resolution_check():
    game = Game()
    erase_screen()
    game.loop()
