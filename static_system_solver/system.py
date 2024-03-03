import numpy as np

import contact
import ball

class System:

    def __init__(self):
        self.number_of_forces = 0
        self.balls = list()
        self.contacts = list()
        # self.equation_matrix = np.array()
        self.non_ground = 0

    def add_ball(self, ball: ball.Ball):
        self.balls.append(ball)

        ball.set_number(len(self.balls) - 1)

    def add_contact(self, pos, ball1: ball.Ball, ball2: ball.Ball):
        print('Ball1 not ground: ' + str(ball1.not_ground()))
        print('Ball2 not ground: ' + str(ball2.not_ground()))
        assert (ball1.not_ground() | ball2.not_ground()), "Tried to add contact between two grounds"

        c = contact.Contact(pos, ball1, ball2)

        self.contacts.append(c)

        if  ball1.not_ground() and ball2.not_ground():
            self.non_ground += 1
            self.number_of_forces += 2
        else:
            self.number_of_forces += 1

        

    # def add_ball_forces(matrix, ):

    def fill_rhs(self, matrix):
        matrix[:, -1] = 0.
        
        for ball in self.balls:
            num_to_fit = 6 * ball.number + 2

            matrix[num_to_fit, -1] = -ball.weight

    def second_third_newton_matrix(self):
        matrix = np.zeros((len(self.balls) * 6 + self.non_ground * 3, self.number_of_forces * 3 + 1))
        self.fill_rhs(matrix)

        current_forces = 0
        current_third_newton = 0
        
        for contact  in self.contacts:
            print("There are " + str(current_forces) + ' before')
            
            values = contact.fill_matrix(matrix, current_forces, current_third_newton, len(self.balls))
            
            current_forces += values[0]
            current_third_newton += values[1]

            print("There are " + str(current_forces) + ' after')

        return matrix
            

    def make_equation_matrix(self):

        matrix = self.second_third_newton_matrix()
        
        return matrix

    def run(self):
        return 0