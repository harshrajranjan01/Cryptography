from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def create_signature(message,private_key):

    signature=private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature


