def rotate_rows(matrix):
    
    matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3] = matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][0]
    matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3] = matrix[2][2], matrix[2][3], matrix[2][0], matrix[2][1]
    matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3] = matrix[3][3], matrix[3][0], matrix[3][1], matrix[3][2]

def reverse_rotate_rows(matrix):
    
    matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][0] = matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3]
    matrix[2][2], matrix[2][3], matrix[2][0], matrix[2][1] = matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3]
    matrix[3][3], matrix[3][0], matrix[3][1], matrix[3][2] = matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3]


polynomial_mult = lambda val: (((val << 1) ^ 0x1B) & 0xFF) if (val & 0x80) else (val << 1)

def transform_column(column):
    
    combined = column[0] ^ column[1] ^ column[2] ^ column[3]
    temp = column[0]
    column[0] ^= combined ^ polynomial_mult(column[0] ^ column[1])
    column[1] ^= combined ^ polynomial_mult(column[1] ^ column[2])
    column[2] ^= combined ^ polynomial_mult(column[2] ^ column[3])
    column[3] ^= combined ^ polynomial_mult(column[3] ^ temp)

def transform_matrix_columns(matrix):
    
    for col in matrix:
        transform_column(col)

def reverse_transform_columns(matrix):
    
    for col in matrix:
        temp1 = polynomial_mult(polynomial_mult(col[0] ^ col[2]))
        temp2 = polynomial_mult(polynomial_mult(col[1] ^ col[3]))
        col[0] ^= temp1
        col[1] ^= temp2
        col[2] ^= temp1
        col[3] ^= temp2

    transform_matrix_columns(matrix)


state_matrix = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]


reverse_transform_columns(state_matrix)
reverse_rotate_rows(state_matrix)

for row in state_matrix:
    for val in row:
        print(chr(val), end="")
