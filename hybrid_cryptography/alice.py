from digital_signature import create_signature

from payload import create_payload

from encryption import encrypt_message

from rsa_encryption import encrypt_aes_key


def alice_send(message,alice_private_key,bob_public_key):
    print("\n=========== Alice: SENDING MESSAGE ===========")

    # Step 1: convert message into bytes
    message_bytes=message.encode("utf-8")

    # Step 2: create digital signature
    signature=create_signature(message_bytes,alice_private_key)

    print("[+] Digital Signature created")

    # Step 3: Combine mesage and signature in payload

    payload=create_payload(message,signature)

    print("[+] Payload Created")


    # Step 4: Encrypt payload using AES-256-GCM
    aes_key,nonce,ciphertext=encrypt_message(payload)

    print("[+] Message and signature encrypted using AES-256-GCM")

    # Step 5: Encrypt AES key using bob's public key

    encrypted_key=encrypt_aes_key(aes_key,bob_public_key)

    print("[+] AES key encrypted using Bob's RSA public key")

    # Step 6: Preapare package for transmission

    package={
        "encrypted_key":encrypted_key,
        "nonce":nonce,
        "ciphertext":ciphertext
    }

    print("[+] Package ready for transmission")

    return package