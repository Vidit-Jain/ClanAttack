from subprocess import DEVNULL, STDOUT, check_call, Popen


def play(path):
    Popen(['mpg123', path], stdout=DEVNULL, stderr=STDOUT)
