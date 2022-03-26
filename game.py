from src.game_input import *
from src.screen import *
from src.Fighters.king import *
from src.Fighters.queen import *
from src.Buildings.townhall import *
from src.Buildings.spawnpoint import *
from src.Buildings.hut import *
from src.Buildings.cannon import *
from src.Buildings.wall import *
from src.helper import *
from src.spell import *


class Game:
    def __init__(self):
        self.input = Get()
        self.screen = Screen()
        self.game_end = -1
        self.game_result = 0
        self.frames = []
        self.player_choice = 0

        # Buildings
        self.spawnpoints = []
        self.townhall = []
        self.huts = []
        self.cannons = []
        self.townhall = []
        self.wizards = []
        add_spawnpoints(self)
        add_townhall(self)
        add_huts(self)
        add_cannons(self)
        add_walls(self)

        self.enemy_buildings = [self.huts, self.walls, self.cannons, self.townhall]
        self.imp_buildings = [self.huts, self.cannons, self.townhall]
        self.buildings = [self.huts, self.walls, self.cannons, self.townhall, self.spawnpoints]

        # Spells
        self.rage = Rage(self)
        self.healSpell = Heal(self)

        # Player
        self.player = None

        # Troops
        self.troop_count = GAME["troop_count"]
        self.barbarians = []
        self.archers = []
        self.balloons = []
        self.troops = [self.barbarians, self.archers, self.balloons]

    def handle_input(self):
        ch = input_to(self.input)

        if ch is None:
            return 0

        if ch == "c":
            file = store_replay(self)
            print("Replay stored in replays/" + file)
            return 1
        # Don't process input if game over
        if self.game_end == -1:
            if ord(ch) == 13:
                if self.player_choice == 0:
                    add_king(self)
                else:
                    add_queen(self)

                self.game_end = 0
            elif ch == "j":
                self.player_choice = min(1, self.player_choice + 1)
            elif ch == "k":
                self.player_choice = max(0, self.player_choice - 1)
            return 0
        if self.game_end == 1:
            return 0
        if (not self.player.is_destroyed()) and (ch in self.player.control_keys):
            self.player.move(ch)
        elif ch in SPAWNPOINT["control_keys"]:
            spawn(self, ch)
        elif ch in SPELL["control_keys"]:
            use_spell(self, ch)
        return 0

    def loop(self):
        while 1:
            self.screen.clear()
            if self.game_end == -1:
                self.screen.add_player_choice(self)
            elif self.game_end == 0:
                self.screen.add_to_screen(self)
                self.rage.check_expired()
                shoot_cannons(game)
                move_troops(game)
                remove_destroyed(game)
                game_ended(game)
            else:
                self.screen.add_to_screen(self)
                self.screen.add_game_end(self.game_result)

            self.screen.render(self)
            if self.handle_input() == 1:
                break


if resolution_check():
    game = Game()
    erase_screen()
    game.loop()
