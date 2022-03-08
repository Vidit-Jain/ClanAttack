import time
from src.config import *


class Spell:
    def __init__(self, game, uses):
        self.uses = uses
        self.game = game

    def use(self):
        pass


class Rage(Spell):
    def __init__(self, game):
        super().__init__(game, SPELL["RAGE"]["uses"])
        self.duration = SPELL["RAGE"]["duration"]
        self.last_used = -self.duration

    def use(self):
        if self.uses > 0:
            self.uses -= 1
            self.last_used = time.monotonic()
            self.game.rageActive = 1

    def check_expired(self):
        if self.game.rageActive == 1 and time.monotonic() >= self.last_used + self.duration:
            self.game.rageActive = 0


class Heal(Spell):
    def __init__(self, game):
        super().__init__(game, SPELL["HEAL"]["uses"])

    def use(self):
        if self.uses > 0:
            self.uses -= 1
            for barbarian in self.game.barbarians:
                barbarian.health = min(int(barbarian.health * 1.5), barbarian.max_health)
            self.game.king.health = max(self.game.king.max_health, int(self.game.king.health * 1.5))


def use_spell(game, ch: str):
    if ch == "r":
        game.rageSpell.use()
    else:
        game.healSpell.use()
