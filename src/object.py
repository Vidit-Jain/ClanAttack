class Object:
    def __init__(self, game, symbol, color, startx, starty, height, width):
        self.game = game
        self.symbol = symbol
        self.color = color 
        self.x = [startx, startx + width]
        self.y = [starty, starty + height]
    
        