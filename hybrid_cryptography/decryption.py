from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def decrypt_message(aes_key,nonce,ciphertext):
    # Step 1: Create AES-GCM object
    aes=AESGCM(aes_key)

    # Step 2: Decrypt ciphertext
    plaintext=aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext

