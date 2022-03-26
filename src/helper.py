import os
import pickle
from src.config import *


def remove_destroyed(game):
    for building_arr in game.buildings:
        for building in building_arr:
            if building.is_destroyed():
                building_arr.remove(building)
    for troop_arr in game.troops:
        for troop in troop_arr:
            if troop.is_destroyed():
                troop_arr.remove(troop)
    if game.king is not None and game.king.is_destroyed():
        game.king = None


def move_troops(game):
    for troop_arr in game.troops:
        for troop in troop_arr:
            troop.action()


def shoot_cannons(game):
    for cannon in game.cannons:
        cannon.shoot()


def game_over(game):
    return game.king is None and len(game.barbarians) == 0 and game.barbarian_count == 0


def game_win(game):
    win = True
    for building_arr in game.imp_buildings:
        win = win and len(building_arr) == 0
    return win


def store_replay(game):
    filename = 0
    while os.path.exists("replays/" + str(filename)):
        filename += 1

    if not os.path.exists('replays'):
        os.makedirs('replays')

    with open("replays/" + str(filename), 'ab') as file:
        pickle.dump(game.frames, file)
    return str(filename)


def game_ended(game):
    if game_win(game):
        game.game_end = 1
        game.game_result = 1
    elif game_over(game):
        game.game_end = 1
        game.game_result = -1


def resolution_check():
    curr_height, curr_width = os.popen("stty size", "r").read().split()
    if int(curr_width) < GAME["window"]["width"] or int(curr_height) < GAME["window"]["height"]:
        print("Your terminal is too small to play this game")
        return False
    return True
