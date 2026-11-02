from key_generation import generate_rsa_key

from alice import alice_send

from bob import bob_receive


def main():

    # Generate Alice's RSA keys
    alice_private_key, alice_public_key = generate_rsa_key()

    # Generate Bob's RSA keys
    bob_private_key, bob_public_key = generate_rsa_key()

    print("[+] Alice's RSA key generated")
    print("[+] Bob's RSA key generated")

    message = "Hello Bob!, This is digitally signed and Encrypted Message."

    print("\nOriginal Message: ", message)

    # Alice Send the  Message
    package = alice_send(message, alice_private_key, bob_public_key)

    print("\n========== TRANSMISSION ==========")

    print("\nEncrypted AES keys: ", package["encrypted_key"].hex())
    print("\nNonce: ", package["nonce"].hex())
    print("\nciphertext: ", package["ciphertext"].hex())

    print("\n[+] Alice's sending process completed")
    # Bob Receive the message
    received_message = bob_receive(
        package,
        bob_private_key,
        alice_public_key)

    if received_message is not None:
        print("Received Message:", received_message)
    else:
        print("Message rejected!")


if __name__ == "__main__":
    main()
