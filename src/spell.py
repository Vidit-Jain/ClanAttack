import time
from src.config import *
from src.audio import *


class Spell:
    def __init__(self, game, uses, sound_file):
        self._uses = uses
        self._game = game
        self._active = False
        self._sound_file = sound_file

    def use(self):
        if self._uses > 0:
            self._uses -= 1
            play(self._sound_file)

    def get_active(self):
        return self._active

    def get_uses_left(self):
        return self._uses


class Rage(Spell):
    def __init__(self, game):
        super().__init__(game, SPELL["RAGE"]["uses"], SPELL["RAGE"]["sound_file"])
        self._duration = SPELL["RAGE"]["duration"]
        self._last_used = -self._duration

    def use(self):
        if self._uses > 0:
            super().use()
            self._last_used = time.monotonic()
            self._active = 1

    def check_expired(self):
        if (
            self._active == 1
            and time.monotonic() >= self._last_used + self._duration
        ):
            self._active = 0


class Heal(Spell):
    def __init__(self, game):
        super().__init__(game, SPELL["HEAL"]["uses"], SPELL["HEAL"]["sound_file"])

    def use(self):
        if self._uses > 0:
            super().use()
            for troop_arr in self._game.troops:
                for troop in troop_arr:
                    troop.heal()
            self._game.player.heal()


def use_spell(game, ch: str):
    if ch == "r":
        game.rage.use()
    else:
        game.healSpell.use()
