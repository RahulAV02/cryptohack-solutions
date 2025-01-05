current_state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

key_schedule = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def xor_with_key(state, key):
    for row in range(4):
        for col in range(4):
            print(chr(state[row][col] ^ key[row][col]), end="")

xor_with_key(current_state, key_schedule)
