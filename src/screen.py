from src.config import * 
import time
class Screen:
    def __init__(self):
        self.height = GAME["window"]["height"] 
        self.width = GAME["window"]["width"] 
        self.screen = [['~'] * self.width] * self.height
        self.last_render = time.monotonic()

    def set_cursor(self, x=0, y=0):
        print("\033[" + str(x) + ";" + str(y) + "H")

    def should_render(self):
        return time.monotonic() - self.last_render > 1 / GAME["fps"]

    def render(self):
        if (not self.should_render()):
            return
        self.set_cursor()

        for _ in self.screen:
            print("".join(_))
        self.last_render = time.monotonic() 

    
