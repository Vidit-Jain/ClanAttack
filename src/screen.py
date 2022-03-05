from src.config import * 
from colorama import Fore 
import time
class Screen:
    def __init__(self):
        self.height = GAME["window"]["height"] 
        self.width = GAME["window"]["width"] 
        self.screen = [[GAME["background"] + GAME["symbol"] for i in range(self.width)] for i in range(self.height)]
        self.last_render = time.monotonic()

    def set_cursor(self, x=0, y=0):
        print("\033[" + str(x) + ";" + str(y) + "H")

    def should_render(self):
        return time.monotonic() - self.last_render > 1 / GAME["fps"]

    def render(self):
        if (not self.should_render()):
            return
        self.set_cursor()

        for i in self.screen:
            for j in i:
                print(j, end='')
            print()
        self.last_render = time.monotonic() 
    
    def add(self, obj):
        symbol = obj.color + GAME["background"] + obj.symbol
        for i in range(obj.y[0], obj.y[1]):
            for j in range(obj.x[0], obj.x[1]):
                self.screen[i][j] = symbol 
    def remove(self, obj):
        for i in range(obj.y[0], obj.y[1]):
            for j in range(obj.x[0], obj.x[1]):
                self.screen[i][j] = GAME["background"] + GAME["symbol"] 


    
