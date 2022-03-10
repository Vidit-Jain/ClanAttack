class Object:
    def __init__(self, game, symbol, color, startx, starty, height, width, health):
        self.game = game
        self._symbol = symbol
        self._color = color
        self._x = [startx, startx + width]
        self._y = [starty, starty + height]
        self._health = health
        self._max_health = health
        self._destroyed = False

    def collide(self, obj):
        return min(obj.get_x()[1], self.get_x()[1]) > max(obj.get_x()[0], self.get_x()[0]) and min(
            obj.get_y()[1], self.get_y()[1]
        ) > max(obj.get_y()[0], self.get_y()[0])

    def attack(self, obj):
        pass

    def damaged(self, damage: int):
        self._health -= damage
        if self._health <= 0:
            self._destroyed = True

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_health(self):
        return self._health

    def get_max_health(self):
        return self._max_health

    def is_destroyed(self):
        return self._destroyed

    def destroy(self):
        self._destroyed = True

    def get_color(self):
        return self._color

    def get_symbol(self):
        return self._symbol
