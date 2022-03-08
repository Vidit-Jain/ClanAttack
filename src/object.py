class Object:
    def __init__(self, game, symbol, color, startx, starty, height, width, health):
        self.game = game
        self.symbol = symbol
        self.color = color
        self.x = [startx, startx + width]
        self.y = [starty, starty + height]
        self.health = health
        self.max_health = health
        self.destroyed = False

    def collide(self, obj):
        return min(obj.x[1], self.x[1]) > max(obj.x[0], self.x[0]) and min(
            obj.y[1], self.y[1]
        ) > max(obj.y[0], self.y[0])
