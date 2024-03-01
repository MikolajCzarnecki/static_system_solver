import numpy as np
import ball
import system as sys

class Contact:
    def __init__(self, my_pos, ball1: ball.Ball, ball2: ball.Ball, sys: sys.System):
        ball1.add_contact(self)
        ball2.add_contact(self)

    def __make

    def add_to_eq_matrix(self, matrix):
        