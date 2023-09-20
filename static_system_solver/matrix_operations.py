import numpy as np

def add_diagonally(arr1 : np.array, arr2 : np.array):
    assert arr1.ndim == 2
    assert arr2.ndim == 2
    
    ret_arr = arr1
    arr1_rows = len(arr1)
    arr1_columns = 0
    arr2_columns = len(arr2[0])
    arr2_rows = len(arr2)

    if arr1_rows != 0:
        arr1_columns = len(arr1[0])
    
    top_right = np.zeros((arr1_rows, arr2_columns))
    ret_arr = np.hstack((ret_arr, top_right))
    bottom_left = np.zeros((arr2_rows, arr1_columns))
    bottom = np.hstack((bottom_left, arr2))
    ret_arr = np.vstack((ret_arr, bottom))
    return ret_arr
