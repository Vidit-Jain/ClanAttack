from colorama import Back, Fore, init

init(autoreset=True)
COLORS = {
    "GREEN": Fore.GREEN,
    "RED": Fore.RED,
    "MAGENTA": Fore.MAGENTA,
    "YELLOW": Fore.YELLOW,
    "BLACK": Fore.BLACK,
    "BLUE": Fore.BLUE,
}
GAME = {
    "window": {"height": 45, "width": 140},
    "background": Back.BLACK,
    "symbol": " ",
    "color": Fore.WHITE,
    "fps": 20,
    "troop_count": [6, 6, 3],
}
INITPOS = {
    "spawnpoints": [
        [[37, 15], [90, 42], [125, 25]],
        [[37, 15], [90, 42], [125, 25]],
        [[37, 15], [90, 42], [125, 25]],
    ],
    "huts": [
        [[60, 13], [70, 15], [80, 28], [90, 22], [80, 14]],
        [[60, 13], [70, 15], [80, 28], [90, 22], [90, 14]],
        [[60, 13], [70, 15], [80, 28], [90, 22], [90, 14]],
    ],
    "cannons": [
        [[60, 20], [90, 30], [80, 17], [60, 25]],
        [[60, 20], [90, 30], [80, 17], [60, 25], [70, 28], [72, 27]],
        [
            [60, 20],
            [90, 30],
            [80, 17],
            [60, 25],
            [70, 28],
            [72, 27],
            [65, 12],
            [65, 15],
            [84, 14],
        ],
    ],
    "wizards": [
        [[81, 22], [65, 22]],
        [[64, 26], [75, 22], [70, 19]],
        [[64, 26], [75, 22], [70, 19], [90, 19]],
    ],
    "walls": [
        [
            [[56, 11], [56, 27]],
            [[57, 27], [78, 27]],
            [[68, 26], [68, 20]],
            [[68, 26], [68, 20]],
            [[69, 20], [75, 20]],
            [[69, 20], [75, 20]],
            [[76, 26], [76, 20]],
            [[79, 27], [79, 31]],
            [[79, 27], [79, 31]],
            [[80, 31], [95, 31]],
            [[80, 31], [95, 31]],
            [[80, 31], [95, 31]],
            [[80, 31], [95, 31]],
            [[95, 30], [95, 27]],
            [[95, 30], [95, 27]],
            [[94, 27], [90, 27]],
            [[94, 27], [90, 27]],
            [[90, 26], [90, 25]],
            [[90, 26], [90, 25]],
            [[91, 25], [96, 25]],
            [[91, 25], [96, 25]],
            [[96, 24], [96, 11]],
            [[96, 24], [96, 11]],
            [[95, 11], [57, 11]],
        ],
        [
            [[56, 11], [56, 35]],
            [[57, 11], [94, 11]],
            [[57, 35], [94, 35]],
            [[57, 17], [65, 18]],
            [[94, 25], [88, 25]],
            [[95, 11], [95, 35]],
        ],
        [
            [[56, 11], [56, 35]],
            [[57, 11], [94, 11]],
            [[57, 35], [94, 35]],
            [[57, 17], [65, 18]],
            [[94, 25], [88, 25]],
            [[95, 11], [95, 35]],
            [[62, 32], [68, 32]],
            [[80, 20], [80, 26]],
        ],
    ],
}

FIGHTER = {
    "width": 1,
    "height": 1,
}

BARBARIAN = {
    "damage": 24,
    "health": 100,
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
    "move_speed": 7,
    "attack_speed": 1,
    "symbol": "!",
    "sound_file": "src/AudioFiles/barbarian_attack.mp3",
}
ARCHER = {
    "damage": BARBARIAN["damage"] / 2,
    "health": BARBARIAN["health"] / 2,
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
    "move_speed": BARBARIAN["move_speed"] * 2,
    "attack_speed": 1,
    "range": 8,
    "symbol": ">",
    "sound_file": "src/AudioFiles/archer_attack.mp3",
}
BALLOON = {
    "damage": BARBARIAN["damage"] * 2,
    "health": BARBARIAN["health"],
    "colors": [Fore.RED, Fore.YELLOW, Fore.GREEN],
    "move_speed": BARBARIAN["move_speed"] * 2,
    "attack_speed": 1,
    "symbol": "B",
    "sound_file": "src/AudioFiles/balloon_attack.mp3",
}
KING = {
    "damage": 50,
    "health": 200,
    "color": Fore.BLUE,
    "move_speed": 4,
    "attack_speed": 0.5,
    "range": 5,
    "symbol": "K",
    "starting_coords": [0, 0],
    "control_keys": ["w", "a", "s", "d", " "],
    "sound_file": "src/AudioFiles/king_attack.mp3",
}

QUEEN = {
    "damage": int(KING["damage"] * 0.8),
    "health": KING["health"],
    "color": Fore.BLUE,
    "move_speed": KING["move_speed"],
    "attack_speed": 0.5,
    "range": 8,
    "symbol": "Q",
    "starting_coords": [0, 0],
    "tile_dimension": 5,
    "sound_file": "src/AudioFiles/queen_attack.mp3",
    "control_keys": ["w", "a", "s", "d", " ", "x"],
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
    # "starting_coords": [GAME["window"]["width"] / 2, GAME["window"]["height"] / 2],
    "starting_coords": [
        [70, 22],
        [70, 22],
        [70, 22],
    ],
}

SPAWNPOINT = {
    "health": 9999,
    "width": 1,
    "height": 1,
    "control_keys": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "symbol": "X",
}

CANNON = {
    "health": 125,
    "width": 1,
    "height": 1,
    "attack_speed": 2,
    "range": 7,
    "damage": 15,
    "symbol": "Y",
}

WIZARD = {
    "health": 125,
    "width": 1,
    "height": 1,
    "attack_speed": 2,
    "range": 7,
    "damage": 15,
    "symbol": "W",
    "tile_dimension": 3,
}

SPELL = {
    "RAGE": {"duration": 5, "uses": 2, "sound_file": "src/AudioFiles/rage.mp3"},
    "HEAL": {"uses": 2, "sound_file": "src/AudioFiles/heal.mp3"},
    "control_keys": ["h", "r"],
}

MESSAGES = {
    "stats": [0, 125],
    "game_end": [GAME["window"]["width"] // 2, GAME["window"]["height"] // 2],
}

LEVELS = {
    "level_count": 3,
}
