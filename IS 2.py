def encrypt_transposition(text, key):
    cipher = ""

    for col in range(key):
        for i in range(col, len(text), key):
            cipher += text[i]

    return cipher


def decrypt_transposition(cipher, key):
    plain = [""] * len(cipher)

    rows = len(cipher) // key
    extra = len(cipher) % key
    index = 0

    for col in range(key):
        col_len = rows + (1 if col < extra else 0)

        for row in range(col_len):
            pos = row * key + col

            if pos < len(cipher):
                plain[pos] = cipher[index]
                index += 1

    return "".join(plain)


# Main Program
text = input("Enter Plain Text: ").replace(" ", "")
key = int(input("Enter Key: "))

encrypted = encrypt_transposition(text, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt_transposition(encrypted, key)
print("Decrypted Text:", decrypted)