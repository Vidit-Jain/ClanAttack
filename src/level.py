from src.config import *
from src.Buildings.spawnpoint import *
from src.Buildings.townhall import *
from src.Buildings.spawnpoint import *
from src.Buildings.hut import *
from src.Buildings.cannon import *
from src.Buildings.wizard import *
from src.Buildings.wall import *
from src.spell import *


class Levels:

    def __init__(self, game):
        self.game = game
        self.level_count = LEVELS["level_count"]

    def reset_level(self):
        pass

    def generate_level(self, level):
        # Spells
        self.game.rage = Rage(self.game)
        self.game.healSpell = Heal(self.game)

        # Troops
        self.game.troop_count = GAME["troop_count"].copy()
        self.game.barbarians = []
        self.game.archers = []
        self.game.balloons = []
        self.game.troops = [self.game.barbarians, self.game.archers, self.game.balloons]

        # Buildings
        self.game.spawnpoints = []
        self.game.townhall = []
        self.game.huts = []
        self.game.cannons = []
        self.game.wizards = []
        self.game.walls = []
        add_spawnpoints(self.game, level)
        add_townhall(self.game, level)
        add_huts(self.game, level)
        add_cannons(self.game, level)
        add_wizards(self.game, level)
        add_walls(self.game, level)

        self.game.enemy_buildings = [self.game.huts, self.game.walls, self.game.cannons, self.game.townhall]
        self.game.imp_buildings = [self.game.huts, self.game.cannons, self.game.townhall]
        self.game.buildings = [
            self.game.huts,
            self.game.walls,
            self.game.cannons,
            self.game.townhall,
            self.game.spawnpoints,
        ]
