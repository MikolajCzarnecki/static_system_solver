import pytest
from numpy.testing import assert_allclose

import numpy as np

from static_system_solver.constraints_from_shape_inside\
      import constraints_from_shape_inside

def test_square():
    #Generate constraints for square between points:
    #[[0,0],[1,0],[1,1],[0,1]]
    
    shape = np.array([[0,0],[1,0],[1,1],[0,1]])

    solution = constraints_from_shape_inside(shape)

    true_solution = np.array[[[-1,0],[0,-1],[1,0],[0,1]],[0,0,1,1]]

    assert_allclose(solution, true_solution)


def test_triangle():
    #Generate constraints for triangle between points:
    #[[0,0],[1,1],[0.5,2]]
    
    shape = np.array([[0,0],[1,1],[0.5,2]])
    
    solution = constraints_from_shape_inside(shape)

    true_solution = np.array[[[-4,1],[1,-1],[2,1]],[0,0,3]]

    assert_allclose(solution, true_solution)
