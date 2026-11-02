from key_generation import generate_rsa_key

from digital_signature import create_signature, verify_signature

from payload import create_payload
from payload_parser import extract_payload


def main():
    # Generate Alice's RSA key
    alice_private_key, alice_public_key = generate_rsa_key()

    message = "Hello Bob!, This is a secret Message"

    # Convert the message into bytes for signing
    message_bytes = message.encode("utf-8")

    # Alice creates digit signature
    signature = create_signature(
        message_bytes,
        alice_private_key
    )

    print("[+] Digital Signature created")

    # Alice combine message and signature
    payload_bytes = create_payload(
        message,
        signature
    )

    print("[+] Payload created")

    print("\nSerialized payload:")
    print(payload_bytes.decode("utf-8"))

    # Bob extracts message and signature
    received_message,received_signature=extract_payload(
        payload_bytes
    )


    print("\n[+] Payload extracted")
    print("Received Message: ",received_message)

    # Bob verifies signature
    is_valid=verify_signature(
        received_message.encode("utf-8"),
        received_signature,
        alice_public_key

    )


    print("\nSignature Valid:", is_valid)
    

if __name__ == "__main__":
    main()
