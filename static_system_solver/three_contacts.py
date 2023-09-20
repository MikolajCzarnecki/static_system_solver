from cvxopt import matrix, solvers
from ball import Ball
import numpy as np

b1 = Ball(0., 0., 0., 1.)
b1.add_contact(0., 0., -1.)
# print(matrix(b1.c_matrix))
# print(matrix(np.transpose(b1.G_matrix)))
# print(matrix(np.transpose(b1.G_matrix)))
# print(matrix(b1.h_matrix))
# print(b1.dims)
print(matrix(b1.A_matrix))
# print(matrix(b1.b_matrix))
sol = solvers.conelp(matrix(b1.c_matrix),matrix(np.transpose(b1.G_matrix)), matrix(b1.h_matrix)\
                     , b1.dims, matrix(np.transpose(b1.A_matrix)), matrix(b1.b_matrix))
