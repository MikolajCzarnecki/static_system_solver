import numpy as np

import ball as b
import matrix_operations as mat

class Structure:

    def __init__(self):
        self.elements = []
        self.c_matrix = np.empty(0, float)
        self.G_matrix = np.empty((0, 4), float)
        self.h_matrix = np.empty(0, float)
        self.A_matrix = np.empty((6, 0))
        self.b_matrix = np.array([0., 0., self.mass, 0., 0., 0.])
        self.dims = {'l':0, 'q': [0], 's': [0]}       

    def add_element(self, element : b.Ball):
        self.elements.append(element)

    def add_contacts(self, ball_num_1 : int, ball_num_2 : int):
        ball1 = self.elements[ball_num_1]
        ball2 = self.elements[ball_num_2]
        contact = 0.5 * ball1  + 0.5 * ball2
        ball1.add_contact(contact[0], contact[1], contact[2])
        ball2.add_contact(contact[0], contact[1], contact[2])


    def between_balls(self, ball_num_1 : int, ball_num_2 : int):
        ball1 = self.elements[ball_num_1]
        ball2 = self.elements[ball_num_2]

        dist_vec = ball2 - ball1
        dist = np.linalg.norm(dist_vec)

        radiae = ball1.radius + ball2.radius

        if dist == radiae:
            self.add_contacts(ball_nu
                              m_1, ball_num_2)

        def prepare(self):
            self.b_matrix = np.hstack(ball.b_matrix for ball in self.elements)
            for i in range(len(self.elements)):
                for j in range(len(i, self.elements)):
                    self.between_balls(i, j)

            