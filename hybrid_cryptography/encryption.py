import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_message(message):

    # Step 1: Generate a random AES-256 key
    aes_key=AESGCM.generate_key(bit_length=256)

    # Step 2: Generate 12-byte nonce
    nonce=os.urandom(12)

    # Step 3: Create AES-GCM object
    aes=AESGCM(aes_key)

    # Encrypt the message
    ciphertext=aes.encrypt(
        nonce,
        message,
        None
    )

    return aes_key,nonce,ciphertext

