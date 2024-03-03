import numpy as np
import ball

class Contact:
    def __init__(self, my_pos, ball1: ball.Ball, ball2: ball.Ball):
        self.my_pos = np.array(my_pos)
        self.number = -1
        self.ball1 = ball1
        self.ball2 = ball2

    def set_number(self, number: int):
        self.number = number

    def second_newton_cell(self, ball):
        position_vector = self.my_pos - ball.pos

        x = position_vector[0]
        y = position_vector[1]
        z = position_vector[2]

        matrix = np.array([[1., 0., 0.],
                  [0., 1., 0.],
                  [0., 0., 1.],
                  [0., -z, y],
                  [z, 0., -x],
                  [-y, x, 0.]])
        
        return matrix
    

    def third_newton_cell(self):
        matrix = np.zeros((3,3))

        np.fill_diagonal(matrix, 1.)

        return matrix


    def fill_matrix(self, matrix, num, third_newt, num_of_balls):
        ball_num_1 = 0
        my_num_1 = 0
        ball_num_2 = 0
        my_num_2 = 0
        extra_forces = 0
        extra_third_newt = 0

        if self.ball1.not_ground():
            ball_num_1 = self.ball1.number
            my_num_1 = num

            my_columns_1 = [3 * my_num_1, 3 * my_num_1 + 3]
            my_rows_1 = [6 * ball_num_1, 6 * ball_num_1 + 6]
            print("Filling for ball " + str(ball_num_1) + " with rows from " + str(my_rows_1[0]) + " to " + str(my_rows_1[1]) + " and columns from " + str(my_columns_1[0]) + " to " + str(my_columns_1[1]))
            matrix[my_rows_1[0]:my_rows_1[1], my_columns_1[0]:my_columns_1[1]] = self.second_newton_cell(self.ball1)

            extra_forces += 1

        if self.ball2.not_ground():
            ball_num_2 = self.ball2.number
            my_num_2 = num + extra_forces

            my_columns_2 = [3 * my_num_2, 3 * my_num_2 + 3]
            my_rows_2 = [6 * ball_num_2, 6 * ball_num_2 + 6]

            print("Filling for ball " + str(ball_num_2) + " with rows from " + str(my_rows_2[0]) + " to " + str(my_rows_2[1]) + " and columns from " + str(my_columns_2[0]) + " to " + str(my_columns_2[1]))


            matrix[my_rows_2[0]:my_rows_2[1], my_columns_2[0]:my_columns_2[1]] = self.second_newton_cell(self.ball2)

            extra_forces+= 1

        if self.ball1.not_ground() and self.ball2.not_ground():
            third_newton_number = third_newt
            extra_third_newt += 1

            my_rows = [6 * num_of_balls + 3 * third_newton_number, 6 * num_of_balls + 3 * third_newton_number + 3]
            my_columns_1 = [3 * my_num_1, 3 * my_num_1 + 3]
            my_columns_2 = [3 * my_num_2, 3 * my_num_2 + 3]

            diag = np.zeros((3,3))
            np.fill_diagonal(diag, 1.)

            matrix[my_rows[0]:my_rows[1], my_columns_1[0]:my_columns_1[1]] = diag
            matrix[my_rows[0]:my_rows[1], my_columns_2[0]:my_columns_2[1]] = -diag

        return [extra_forces, extra_third_newt]
            
    # def add_to_eq_matrix(self, matrix):
        