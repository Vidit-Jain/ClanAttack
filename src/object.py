
class Object:
    def __init__(self, game, symbol, color, startx, starty, height, width, health):
        self.game = game
        self.symbol = symbol
        self.color = color
        self.x = [startx, startx + width]
        self.y = [starty, starty + height]
        self.health = health

    def collide(self, obj):
        # return (self.x[0] <= obj.x[1] and self.x[1] >= obj.x[0]) and (self.y[0] <= obj.y[1] and self.y[1] >= obj.y[0])
        return min(obj.x[1], self.x[1]) > max(obj.x[0], self.x[0]) and min(obj.y[1], self.y[1]) > max(obj.y[0], self.y[0])
