import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here\
    rows=len(A)
    cols=len(A[0])
    transposed_matrix=[[0 ]*rows for _ in range(cols) ]
    for row in range(rows):
        for col in range(cols):
            transposed_matrix[col][row]=A[row][col]
    return np.asarray(transposed_matrix)
        