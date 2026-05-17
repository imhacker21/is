IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

S_BOX = [
    [14, 4, 13, 1, 2, 15, 11, 8,
     3, 10, 6, 12, 5, 9, 0, 7],

    [0, 15, 7, 4, 14, 2, 13, 1,
     10, 6, 12, 11, 9, 5, 3, 8],

    [4, 1, 14, 8, 13, 6, 2, 11,
     15, 12, 9, 7, 3, 10, 5, 0],

    [15, 12, 8, 2, 4, 9, 1, 7,
     5, 11, 3, 14, 10, 0, 6, 13]
]

def permute(data, table):
    return ''.join(data[i - 1] for i in table)

def xor(a, b):
    return ''.join(
        '0' if x == y else '1'
        for x, y in zip(a, b)
    )

def des_encrypt(plaintext_hex, key_hex):

    plaintext = format(
        int(plaintext_hex, 16),
        '064b'
    )

    key = format(
        int(key_hex, 16),
        '064b'
    )

    ip = permute(plaintext, IP)

    L = ip[:32]
    R = ip[32:]

    print("\nInitial Left (L0):", L)
    print("Initial Right (R0):", R)

    for i in range(1, 17):

        expanded_R = permute(R, E)

        temp = xor(expanded_R, key[:48])

        row = int(temp[0] + temp[5], 2)
        col = int(temp[1:5], 2)

        s_out = format(
            S_BOX[row][col],
            '04b'
        )

        s_out = s_out.ljust(32, '0')

        p_out = permute(s_out, P)

        new_R = xor(L, p_out)

        L = R
        R = new_R

        print(f"Round {i} ->")
        print("L =", L)
        print("R =", R)

    combined = R + L

    cipher = permute(combined, FP)

    return hex(int(cipher, 2))

plaintext = input(
    "Enter 64-bit plaintext (HEX): "
)

key = input(
    "Enter 64-bit key (HEX): "
)

ciphertext = des_encrypt(
    plaintext,
    key
)

print("\nCiphertext:", ciphertext)