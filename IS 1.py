s = "Hello World"

print("Original String:", repr(s))
print("-" * 60)

for ch in s:

    # Convert character to ASCII number
    ascii_val = ord(ch)

    # Convert ASCII number to binary
    binary_val = format(ascii_val, '08b')

    # AND with 127
    and_val = ascii_val & 127

    # XOR with 127
    xor_val = ascii_val ^ 127

    print("Character :", repr(ch))
    print("ASCII     :", ascii_val)
    print("Binary    :", binary_val)
    print("AND 127   :", and_val, "->", chr(and_val))
    print("XOR 127   :", xor_val, "->", chr(xor_val))
    print("-" * 60)