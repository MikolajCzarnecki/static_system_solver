import pytest
import numpy as np

import static_system_solver.conic_solver

def test_elementary_equation():
    # Minimize:
    # x - 2y
    # Subject to:
    # z - 1 == 0
    # x^2 + y^2 <= 2 z

    objective = np.array([1, -2, 0])
    constraints_variables = np.array([[0,0,1]])
    constraints_constants = np.array([1])
    cones = 0.5*np.array([1,1,0])

    solution = static_system_solver.conic_solver(objective,constraints_variables,constraints_constants,cones)

    true_solution = np.array([-0.632455532033676, 1.2649110640673518, 1.])

    assert allclose(solution, true_solution)
