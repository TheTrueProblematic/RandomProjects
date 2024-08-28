from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import base64
import time

# Generate a key based on the current hour of the day (0-23)
def generate_key(hour=None, key_size=32):
    if hour is None:
        hour = time.localtime().tm_hour  # Get the current hour (0-23)
    hour_str = str(hour).zfill(2)  # Ensure hour is two digits (e.g., "03" instead of "3")
    key_source = hour_str.encode()  # Convert hour to bytes
    key = sha256(key_source).digest()[:key_size]  # Hash the hour and truncate to the key size
    return key

# Encrypt the message using the secret key
def encrypt_message(message: str, secret_key: bytes) -> str:
    cipher = AES.new(secret_key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_message = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_message).decode()

# Decrypt the message using the secret key
def decrypt_message(encrypted_message: str, secret_key: bytes) -> str:
    encrypted_message = base64.b64decode(encrypted_message)
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message[AES.block_size:]), AES.block_size)
    return decrypted_message.decode()

if __name__ == "__main__":
    # Generate and print a secret key based on the current hour
    secret_key = generate_key()
    print(f"Secret Key: {base64.b64encode(secret_key).decode()}")

    # Define the message to encrypt
    mesD = input("Please enter your message to decrypt: \n")

    # Decrypt the message
    decrypted_message = decrypt_message(mesD, secret_key)
    print(f"Decrypted Message: {decrypted_message}")

    mesE = input("Please enter your message to encrypt: \n")

    # Encrypt the message
    encrypted_message = encrypt_message(mesE, secret_key)
    print(f"Encrypted Message: {encrypted_message}")
