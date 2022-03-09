from os.path import exists
from src.config import *
import pickle
import sys
import time


def set_cursor(x=0, y=0):
    print("\033[" + str(x) + ";" + str(y) + "H")


def erase_screen():
    print("\033[2J")


def should_render(last_render):
    return time.monotonic() - last_render > 1 / GAME["fps"]


def show_replay(filename):
    if not exists("replays/" + filename):
        print("Error while opening replay: No such replay found")
        return

    last_render = 0
    with open("replays/" + filename, "rb") as file:
        frames = pickle.load(file)

    erase_screen()

    for frame in frames:
        while not should_render(last_render):
            pass
        set_cursor()

        output = ""
        for i in frame:
            for j in i:
                output += j
            output += "\n"
        sys.stdout.write(output)
        last_render = time.monotonic()


if len(sys.argv) != 2:
    print("Incorrect number of arguments")
else:
    show_replay(sys.argv[1])
