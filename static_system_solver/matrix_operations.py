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
    else:
        return arr2
    
    top_right = np.zeros((arr1_rows, arr2_columns))
    ret_arr = np.hstack((ret_arr, top_right))
    bottom_left = np.zeros((arr2_rows, arr1_columns))
    bottom = np.hstack((bottom_left, arr2))
    ret_arr = np.vstack((ret_arr, bottom))
    return ret_arr

def reduce_matrix(mat: np.array):
    assert mat.ndim == 2
    if len(mat) == 0:
        return ([],[])
    if len(mat) == 1:
        return (mat, [1])
    if len(mat) > len(mat[0]):                  #more rows than columns
        if (np.linalg.det(mat[:len(mat[0])]) != 0):
            return (mat[:len(mat[0])], np.append(np.ones(len(mat[0])), np.zeros(len(mat) - len(mat[0]))))

        red1 = reduce_matrix(mat[:len(mat[0])])
        red2 = reduce_matrix(mat[len(mat[0]):])
        return (reduce_matrix(np.vstack((\
            red1[0], red2[0]
            ))), np.append(red1[1], red2[1]))

    R = np.linalg.qr(np.transpose(mat)).R
    ref = np.zeros(len(mat))
    final_rows = 0
    for i in range(len(R[0])):
        if not np.allclose(R[i][i], 0.):
            ref[i] = 1
            final_rows += 1
    
    ret_mat = np.empty((final_rows, len(mat[0])))
    curr_row = 0
    for i in range(len(mat)):
        if ref[i] == 1:
            for j in range(len(mat[0])):
                ret_mat[curr_row][j] = mat[i][j]
            curr_row += 1
    
    return (ret_mat, ref)
    


            
    
