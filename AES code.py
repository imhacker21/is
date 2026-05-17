#Run this command in CMD/Terminal: pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# ---------------- ENCRYPTION ----------------

key = b'abcdefghijklmnop'
message = input("Enter message: ")
cipher = AES.new(key, AES.MODE_CBC)
encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
encrypted_text = base64.b64encode(cipher.iv + encrypted).decode()

print("\nEncrypted Text:", encrypted_text)

# ---------------- DECRYPTION ----------------

data = base64.b64decode(encrypted_text)
iv = data[:16]
encrypted_message = data[16:]
decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(
    decrypt_cipher.decrypt(encrypted_message),
    AES.block_size
).decode()

print("Decrypted Text:", decrypted)

