from tracemalloc import start


class Object:
    def __init__(self, game, symbol, color, startx, starty, height, width, health):
        self.game = game
        self.symbol = symbol
        self.color = color
        self.x = [startx, startx + width]
        self.y = [starty, starty + height]
        self.health = health
