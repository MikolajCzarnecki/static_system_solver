import numpy as np
from scipy.spatial.transform import Rotation as R

class Ball:
    
    def __init__(self, x : float, y : float, z : float, friction : float,\
            mass : float = 1., radius : float = 1.):
        """
        Object representing ball placed in (x,y,z) point in space.
        Ball has attributes such as mass, radius, friction.
        Ball stores other balls it contacts.

        Parameters
        ------------

        x : float
            x-axis position of ball center
        y : float
            y-axis position of ball center
        z : float
            z-axis position of ball center

        friction : float
            friction coefficient of ball
        mass : float
            mass of ball
        radius : float
            radius of ball

        Returns
        --------

        Object representing ball with given attributes placed in certain point
        with empty list of other balls it contacts.

        """
        self.friction = friction
        self.center = np.array([x,y,z])
        self.mass = mass
        self.radius = radius
        self.contacts = np.empty((0,3), float)
        self.constraintsG_matrices= []
        self.constraintsh_matrices = []

    def add_contact(self, x : float, y : float, z : float):
        new_contact = np.array([x, y, z])
        self.contacts = np.vstack((self.contacts, new_contact))

    def vec(self, contact_number : int):
        return_vec = np.subtract(self.contacts[contact_number], self.center)
        return return_vec

    def matrix_for_contact(self, contact_number : int):
        """
        Create matrix rows representing conic
        constraints for cvxopt.solvers.conelp for given contact.

        Parameters
        ----------

        contact_number: int
            Number of contact for which we want to generate constraints.

        Returns
        -------
            np.array
                Constraints in the form of 4-row matrix.
        """
        assert np.size(self.contacts, 0) > contact_number

        vec_normal = self.contacts[contact_number] - self.center
        vec_ortho = np.cross(vec_normal,np.array([0. ,0. , 1.]))
        ortho_norm = np.linalg.norm(vec_ortho)
    
        if ortho_norm == 0:         #case where contact at [0., 0., x]
            vec_ortho = np.array([0., -1., 0.])
        else:
            vec_ortho = vec_ortho/ortho_norm
        
        dotproduct = np.dot(vec_normal, np.array([0., 0., 1.]))
        deg = np.arccos(dotproduct / (np.linalg.norm(vec_normal)))
        rotation = R.from_rotvec(deg * vec_ortho)
        rt = R.as_matrix(rotation)
        leftside = -np.array([rt[0][:2], rt[1][:2], rt[2][:2]])
        leftside = np.column_stack((leftside, np.array([[0.],[0.],[0.]])))
        rightside = -self.friction * np.array([[rt[0][2]], [rt[1][2]],[rt[2][2]]])
        matrixh = np.array([0., 0., 0.])

        #Norm[leftside] <= rightside * friction
        matrixG = np.empty((3,0), float)
        matrixG = np.column_stack((matrixG, rightside))
        matrixG = np.column_stack((matrixG, leftside))

        self.constraintsG_matrices.append(matrixG)
        self.constraintsh_matrices.append(matrixh)
        return

    def generate_constraints(self):
        i = 0
        for i in range(len(self.contacts)):
            self.matrix_for_contact(i)

