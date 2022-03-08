from colorama import Back, Fore, init

init(autoreset=True)
GAME = {
    "window": {"height": 45, "width": 140},
    "background": Back.BLACK,
    "symbol": " ",
    "color": Fore.WHITE,
    "fps": 20,
}
INITPOS = {
    "spawnpoints": [[50, 5], [90, 32], [110, 25]],
    "huts": [[60, 13], [40, 3], [85, 33], [102, 22], [80, 14]],
    "cannons": [[60, 20], [90, 30]]
}

FIGHTER = {
    "width": 1,
    "height": 1,
}

BARBARIAN = {
    "damage": 25,
    "health": 100,
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
    "move_speed": 7,
    "attack_speed": 1,
    "symbol": "!",
}
KING = {
    "damage": 50,
    "health": 200,
    "color": Fore.BLUE,
    "move_speed": 4,
    "attack_speed": 0.5,
    "symbol": "K",
    "starting_coords": [0, 0],
    "control_keys": ['w', 'a', 's', 'd']
}

BUILDING = {
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
}

HUT = {
    "health": 150,
    "width": 2,
    "height": 2,
    "symbol": "^",
}

WALL = {
    "health": 75,
    "width": 1,
    "height": 1,
    "symbol": "#",
}

TOWNHALL = {
    "health": 300,
    "width": 3,
    "height": 4,
    "symbol": "$",
    "starting_coords": [GAME["window"]["width"] / 2, GAME["window"]["height"] / 2]
}

SPAWNPOINT = {
    "health": 9999,
    "width": 1,
    "height": 1,
    "symbol": "X",
}

CANNON = {
    "health": 125,
    "width": 1,
    "height": 1,
    "attack_speed": 1,
    "damage": 33,
    "symbol": "Y",
}
