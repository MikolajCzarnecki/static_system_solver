import numpy as np
import scipy

#From ordered set of points creates constraints
#for being inside of the shape

def constraints_from_shape_inside(points):          #returns [A,B], where A and B are
    constraintsA = np.array([])                     #matrices from A x <= B used by
    constraintsB = np.array([])                     #scipy.optimize.linprog()
    for i in range(len(points)):
        if (points[i][0] != points[i - 1][0]):
            a = (points[i][1] - points[i - 1][1]) /\
                (points[i][0] - points[i- 1][0])
            b = ((points[i][0] * points[i - 1][1]) -\
                (points[i - 1][0] * points[i][1])) /\
                (-points[i - 1][0] + points[i][0])
            if (points[i][0] > points[i - 1][0]):   #region above ax + b
                np.append(constraintsA, np.array([a,-1]))
                np.append(constraintsB, -b)
            else:                                   #region below ax + b
                np.append(constraintsA, np.array([-a, 1]))
                np.append(constraintsB, b)
        else:                                       #vertical line
            if(points[i][1] > points[i - 1][1]):    #region on the left from x0
                np.append(constraintsA, np.array([1, 0]))
                np.append(constraintsB, points[i][0])
            else:                                    #region on the right from x0
                np.append(constraintsA, np.array([-1,0]))
                np.append(constraintsB, points[i][0])
    return np.array([constraintsA, constraintsB])

