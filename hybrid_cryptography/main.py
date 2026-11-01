from encyption import encrypt_message
from decryption import decrypt_message


def main():
    message=b"Hello BOb!, This is a secret message"

    print("Original Message: ",message)

    aes_key,nonce,ciphertext=encrypt_message(message)

    print("=======Encryption======")
    print("AES Key",aes_key)
    print("Nonce: ",nonce)
    print("Ciphertext: ",ciphertext)

    plaintext=decrypt_message(aes_key,nonce,ciphertext)
    print("=======Decryption======")

    print("Decrypted Message: ",plaintext.decode("utf-8"))

if __name__=="__main__":
    main()