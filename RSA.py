from math import gcd, isqrt


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, isqrt(number)+1):
        if number % i == 0:
            return False

    return True

# Generate RSA keys


def generate_keys(p, q):
    # validate prime numbers
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both p and q must be prime numbers")

    if p == q:
        raise ValueError("p and q must be different prime numbers")

    # calculate the modulus(n)
    n = p*q

    # calculate Euler's totient
    phi = (p-1)*(q-1)

    # choose public exponent
    e = 65537

    # Use a smaller exponent if 65537 is unsuitable

    if e >= phi or gcd(e, phi) != 1:
        e = 3
        while e < phi and gcd(e, phi) != 1:
            e += 2

    if e >= phi:
        raise ValueError("Unable to find a valid public exponent")

    # calculate private exponent
    d = pow(e, -1, phi)  # (e to power -1) mod phi

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# Encrypt a message


def encrypt(message, public_key):

    e, n = public_key

    # Each character is converted to its Unicode integer

    encrypted_message = []

    for character in message:
        m = ord(character)

        if m >= n:
            raise ValueError(
                "Message character is too large for this RSA module")

        c = pow(m, e, n)

        encrypted_message.append(c)

    return encrypted_message


def decrypt(ciphertext, private_key):
    d, n = private_key

    decrypted_message = ""

    for c in ciphertext:
        m = pow(c, d, n)

        decrypted_message += chr(m)

    return decrypted_message



if __name__=="__main__":

    p=61
    q=53

    public_key,private_key=generate_keys(p,q)

    message="HELLO RSA"

    ciphertext=encrypt(message,public_key)

    decrypted_message=decrypt(ciphertext,private_key)

    print("Original message :", message)
    print("Public key       :", public_key)
    print("Private key      :", private_key)
    print("Encrypted message:", ciphertext)
    print("Decrypted message:", decrypted_message)
