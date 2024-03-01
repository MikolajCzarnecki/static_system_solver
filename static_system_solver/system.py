import numpy as np

import contact
import ball

class System:

    def __init__(self):
        self.number_of_forces = 0
        self.balls = list()
        self.contacts = list()
        self.equation_matrix
        
    def add_ball(self, ball: ball.Ball):
        self.balls.append(ball)

    def add_contact(self, pos, ball1: ball.Ball, ball2: ball.Ball):

        c = contact.Contact(pos, )

    def second_newton_matrix(self):
        matrix = np.zeros((len(self.balls) * 6, self.number_of_forces * 3 + 1))

    def make_equation_matrix(self):


    def run(self):