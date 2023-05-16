from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from os import urandom

def generate_key():
    return urandom(16)  # Generate a 128-bit (16-byte) random key

def ecb_encrypt(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext

def ecb_decrypt(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_plaintext = unpadder.update(plaintext) + unpadder.finalize()
    return unpadded_plaintext

# Example usage
key = generate_key()
message = b"Hello, ECB!"

# Encryption
encrypted_message = ecb_encrypt(key, message)
print("Encrypted:", encrypted_message)

# Decryption
decrypted_message = ecb_decrypt(key, encrypted_message)
print("Decrypted:", decrypted_message.decode())
