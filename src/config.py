from colorama import Back, Fore, init
init(autoreset=True)
GAME = {
    "window": {
        "height": 30,
        "width": 50 
    },
    "background": Back.BLACK,
    "symbol": '~',
    "fps": 15 
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
    "symbol": '!'
}

KING = {
    "damage": 50,
    "health": 200,
    "color": Fore.BLUE,
    "move_speed": 0.5,
    "symbol": 'K'
}