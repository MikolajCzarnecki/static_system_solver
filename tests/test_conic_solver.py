import pytest
from numpy.testing import assert_allclose

import numpy as np

from static_system_solver.conic_solver import conic_solver

def test_elementary_equation():
    # Minimize:
    # x - 2y
    # Subject to:
    # z - 1 == 0
    # sqrt(x^2 + y^2) <= 2 z

    objective = np.array([1, -2, 0])
    constraints_variables = np.array([[0,0,1]])
    constraints_constants = np.array([1])
    cones_across = np.array([1,1,0])
    cones_along = np.array([0,0,2])

    solution = conic_solver(objective,constraints_variables,constraints_constants,cones_across,cones_along)

    true_solution = np.array([-0.632455532033676, 1.2649110640673518, 1.])

    assert_allclose(solution, true_solution)
