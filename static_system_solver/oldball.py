import numpy as np
from scipy.spatial.transform import Rotation as R
from matrix_operations import add_diagonally, reduce_matrix

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
        self.contacts = np.empty((0, 3), float)
        self.c_matrix = np.empty(0, float)
        self.G_matrix = np.empty((0, 4), float)
        self.h_matrix = np.empty(0, float)
        self.A_matrix = np.empty((6, 0))
        self.b_matrix = np.array([0., 0., self.mass, 0., 0., 0.])
        self.dims = {'l':0, 'q': [0], 's': [0]}

    def add_contact(self, x : float, y : float, z : float):
        #assert np.linalg.norm(np.array(x, y, z)) == self.radius, "Invalid distance"
        new_contact = np.array([x, y, z])
        self.contacts = np.vstack((self.contacts, new_contact))

        Gh_mats = self.G_matrix_for_contact(len(self.contacts) - 1)
        matrix_to_G = Gh_mats[0]
        self.G_matrix = add_diagonally(self.G_matrix, matrix_to_G)

        self.h_matrix = np.append(self.h_matrix, Gh_mats[1])

        self.c_matrix = np.hstack((self.c_matrix, np.array([-1., 0., 0.])))

        matrix_to_A = self.A_matrix_for_contact(len(self.contacts) - 1)
        self.A_matrix = np.hstack((self.A_matrix, matrix_to_A))

        self.dims["q"][0] = self.dims["q"][0] + 4


    def A_matrix_for_contact(self, contact_number : int):
        mat_A = np.zeros((6,3))
        for i in range(0,3):
            mat_A[i,i] = 1.
        
        vec = self.contacts[contact_number] - self.center
        mat_A[3] = np.array([0., -vec[2], vec[1]])
        mat_A[4] = np.array([vec[2], 0., -vec[0]])
        mat_A[5] = np.array([-vec[1], vec[0], 0.])
        return mat_A

    def G_matrix_for_contact(self, contact_number : int):
        """
        Create matrix rows representing conic
        constraints for cvxopt.solvers.conelp for given contact.

        Parameters
        ----------

        contact_number: int
            Number of contact for which we want to generate constraints.

        Returns
        -------
        
        """
        assert np.size(self.contacts, 0) > contact_number

        vec_normal = self.contacts[contact_number] - self.center
        vec_ortho = np.cross(vec_normal,np.array([0. ,0. , 1.]))
        ortho_norm = np.linalg.norm(vec_ortho)
    
        if np.allclose(vec_normal[:2], [0., 0.]):         #case where contact directly below/under
            vec_ortho = np.array([0., 1., 0.])
        else:
            vec_ortho = vec_ortho/ortho_norm
        
        dotproduct = np.dot(vec_normal, np.array([0., 0., 1.]))
        deg = np.arccos(dotproduct / (np.linalg.norm(vec_normal)))
        rotation = R.from_rotvec(deg * vec_ortho)
        rt = R.as_matrix(rotation)
        leftside = -np.array([rt[0][:2], rt[1][:2], rt[2][:2]])
        leftside = np.column_stack((leftside, np.array([[0.],[0.],[0.]])))
        rightside = self.friction * np.array([[rt[0][2]], [rt[1][2]],[rt[2][2]]])

        #Norm[leftside] <= rightside * friction
        matrixG = np.empty((3,0), float)
        matrixG = np.column_stack((matrixG, rightside))
        matrixG = np.column_stack((matrixG, leftside))
        matrixh = np.array([-1 * np.dot(rt[2], vec_normal),\
                            -1 * np.dot(rt[0], vec_normal),\
                            -1 * np.dot(rt[1], vec_normal),\
                            0.])
        return (matrixG, matrixh)


    def prepare_ball(self):
        reduced = reduce_matrix(self.A_matrix)
        self.A_matrix = reduced[0]

        new_b = np.empty(len(self.A_matrix))
        curr = 0
        for i in range(len(reduced[1])):
            if reduced[1][i] == 1:
                new_b[curr] = self.b_matrix[i]
                curr += 1

        self.b_matrix = new_b

    def generate_constraints(self):
        for i in range(len(self.contacts)):
            self.matrix_for_contact(i)
