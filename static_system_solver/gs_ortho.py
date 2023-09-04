import numpy as np
import random as rand

def proj(vec1 : np.array, vec2 : np.array):
    mult = np.dot(vec1, vec2)
    denom = np.dot(vec1, vec1)
    return (mult/denom) * vec1

def get_orthogonal(vec : np.array):
    rand.seed()
    rand_vec = np.array([rand.random(), rand.random(), rand.random()])
    return_vec =  rand_vec - proj(vec, rand_vec)
    return return_vec / np.linalg.norm(return_vec)

    