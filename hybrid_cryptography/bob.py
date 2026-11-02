from rsa_decryption import decrypt_aes_key

from decryption import decrypt_message

from payload_parser import extract_payload

from digital_signature import verify_signature


def bob_receive(package, bob_private_key, alice_public_key):

    print("\n========== BOB: RECEIVING MESSAGE ==========")

    # Step 1: Decrypt AES key using Bob's Private key

    aes_key = decrypt_aes_key(
        package["encrypted_key"],
        bob_private_key
    )

    print("[+] AES key decrypted")

    # Step 2: Decrypt the payload using AES-GCM

    plaintext = decrypt_message(
        aes_key,
        package["nonce"],
        package["ciphertext"]
    )

    print("[+] Payload Decrypted")

    # Step 3: Extract message and digital signature
    message, signature = extract_payload(plaintext)

    print("[+] Message and signature extracted")

    # Step 4: Convert message into bytes
    message_bytes = message.encode("utf-8")

    # Verify Alice digital Signature
    is_valid = verify_signature(
        message_bytes,
        signature,
        alice_public_key
    )

    if is_valid:
        print("[+] DIGITAL SIGNATURE VERIFIED")
        print("[+] Message integrity confirmed")

        return message

    else:
        print("[-] DIGITAL SIGNATURE INVALID")
        return None
