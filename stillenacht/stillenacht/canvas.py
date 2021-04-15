import sys


class Canvas:
    def __init__(self):
        self.width = int(sys.argv[1])
        self.height = int(sys.argv[2])
        self.color = [0, 0, 0]
