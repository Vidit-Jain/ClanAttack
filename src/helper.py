
def remove_destroyed(game):
    for barbarian in game.barbarians:
        if barbarian.destroyed:
            game.barbarians.remove(barbarian)

    for wall in game.walls:
        if wall.destroyed:
            game.walls.remove(wall)

    for hut in game.huts:
        if hut.destroyed:
            game.x = 1
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
