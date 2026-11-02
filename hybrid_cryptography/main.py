from key_generation import generate_rsa_key

from encyption import encrypt_message
from decryption import decrypt_message

from rsa_encryption import encrypt_aes_key
from rsa_decryption import decrypt_aes_key

def main():
    # Generate Bob's RSA key
    bob_private_key,bob_public_key=generate_rsa_key()

    # Original Message
    message=b"Hello Bob! This is secret message"

    # Alice encrypt the message using AES
    aes_key,nonce,ciphertext=encrypt_message(message)

    print("[+] Message encrypted Using AES")

    #Alice Encrypt AES key using Bob's public key

    encrypted_key=encrypt_aes_key(aes_key,bob_public_key)

    print("[+] AES key encrypted using RSA-OAEP")

    #Bob Decrypt AES key
    decrypted_aes_key=decrypt_aes_key(encrypted_key,bob_private_key)

    print("[+] AES key decrypted using RSA-OAEP")

    #Bob Decrypt message using recovered AES key
    plaintext=decrypt_message(decrypted_aes_key,nonce,ciphertext)


    print("\nOriginal Message:", message)

    print("Decrypted Message:", plaintext)


if __name__=="__main__":
    main()