from os.path import exists
import pickle
def remove_destroyed(game):
    for barbarian in game.barbarians:
        if barbarian.destroyed:
            game.barbarians.remove(barbarian)

    for wall in game.walls:
        if wall.destroyed:
            game.walls.remove(wall)

    for hut in game.huts:
        if hut.destroyed:
            game.huts.remove(hut)

    for cannon in game.cannons:
        if cannon.destroyed:
            game.cannons.remove(cannon)

    if game.king is not None and game.king.destroyed:
        game.king = None

    if game.townhall is not None and game.townhall.destroyed:
        game.townhall = None


def move_barbarians(game):
    for barbarian in game.barbarians:
        barbarian.move()


def shoot_cannons(game):
    for cannon in game.cannons:
        cannon.shoot()


def game_over(game):
    return game.king is None and len(game.barbarians) == 0 and game.barbarian_count == 0


def game_win(game):
    return game.townhall is None and len(game.huts) == 0 and len(game.cannons) == 0


def store_replay(game):
    filename = 0
    while exists("replays/" + str(filename)):
        filename += 1
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
