def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d


p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while gcd(e, phi) != 1:
    e += 1

d = mod_inverse(e, phi)

msg = int(input("Enter number to encrypt: "))

cipher = (msg ** e) % n
print("Encrypted number:", cipher)

plain = (cipher ** d) % n
print("Decrypted number:", plain)