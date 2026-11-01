from key_generation import generate_rsa_key
from digital_signature import (
    create_signature,
    verify_signature
)


def main():

    # Generate Alice Key
    alice_private_key, alice_public_key = generate_rsa_key()

    message = b"Hello Bob!!"

    # Alice signs the message
    signature = create_signature(message, alice_private_key)

    # Bob Verify the message
    result=verify_signature(message,signature,alice_public_key)

    print("Signature valid: ",result)


if __name__=="__main__":
    main()