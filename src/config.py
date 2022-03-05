from colorama import Back, Fore, init

init(autoreset=True)
GAME = {
    "window": {"height": 40, "width": 80},
    "background": Back.BLACK,
    "symbol": "~",
    "color": Fore.WHITE,
    "fps": 20,
}

FIGHTER = {
    "width": 1,
    "height": 1,
}

BARBARIAN = {
    "damage": 25,
    "health": 100,
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
    "move_speed": 1,
    "symbol": "!",
}
KING = {
    "damage": 50,
    "health": 200,
    "color": Fore.BLUE,
    "move_speed": 0.5,
    "symbol": "K",
}

BUILDING = {
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
}

HUT = {
    "health": 150,
    "width": 3,
    "height": 3,
    "symbol": "*",
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
    "damage": 1,
    "symbol": "Y",
}
