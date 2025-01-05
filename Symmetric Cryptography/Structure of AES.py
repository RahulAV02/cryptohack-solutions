def bytes_to_matrix(data):
    
    return [list(data[idx:idx+4]) for idx in range(0, len(data), 4)]

def matrix_to_bytes(mat):
    result = ''
    for row in mat:
        result += ''.join(chr(element) for element in row)
    return result

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix_to_bytes(matrix))
