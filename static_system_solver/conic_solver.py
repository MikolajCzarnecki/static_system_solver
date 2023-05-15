import numpy as np

def conic_solver(objective,constraint_variables,constraint_constants,cones_across,cones_along):
    """
    Returns solution to conic problem.

    :math:`A x + b = 0`
    :math:`A x + b < 0`

    Parameters
    ----------
    objective: np.array
        Length `N` vector specifying objective function.
    constraint_variables: np.array
        Shape `N` by `M` array giving coefficients by each variable in constraining equations.

    Returns
    -------
    np.array
        Solution of the conical problem or None if there is no solution.
    """

    return np.ones_like(objective)
