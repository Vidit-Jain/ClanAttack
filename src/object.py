from tracemalloc import start


class Object:
    def __init__(self, game, symbol, color, startx, starty, height, width, health):
        self.game = game
        self.symbol = symbol
        self.color = color
        self.x = [startx, startx + width]
        self.y = [starty, starty + height]
        self.health = health

    def delta(self, x, y):
        self.game.screen.remove(self)
        self.x = [self.x[0] + x, self.x[1] + x]
        self.y = [self.y[0] + y, self.y[1] + y]
        self.game.screen.add(self)

    def movedown(self):
        self.delta(0, 1)
