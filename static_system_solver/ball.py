import numpy as np

class Ball:
    def __init__(self, pos, weight, is_ground: bool):
        self.number = -1
        self.pos = np.array(pos)
        self.weight = weight
        self.is_ground = is_ground

    def set_number(self, number: int):
        print("Changed ball's number to " + str(number))
        self.number = number

    def not_ground(self):
        return not self.is_ground

