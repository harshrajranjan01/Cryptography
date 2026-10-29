
import secrets


def generate_private_key(q):

    return secrets.randbelow(q - 3) + 2


def generate_public_key(a, private_key, q):

    return pow(a, private_key, q)


def generate_shared_secret(public_key, private_key, q):

    return pow(public_key, private_key, q)


def main():

    # Public parameters known to Alice and Bob
    # a is primitive root of q (a<q) and q is prime number
    q = 23
    a = 5

    alice_private_key = generate_private_key(q)
    alice_public_key = generate_public_key(
        a, alice_private_key, q
    )

    bob_private_key = generate_private_key(q)
    bob_public_key = generate_public_key(
        a, bob_private_key, q
    )

    # Exchange public keys and calculate the shared secret
    alice_secret = generate_shared_secret(
        bob_public_key, alice_private_key, q
    )

    bob_secret = generate_shared_secret(
        alice_public_key, bob_private_key, q
    )

    # Display Result
    print("Public Parameters:")
    print("Prime (q):", q)
    print("Generator (a):", a)

    print("\nAlice:")
    print("Private Key:", alice_private_key)
    print("Public Key:", alice_public_key)
    print("Shared Secret:", alice_secret)

    print("\nBob:")
    print("Private Key:", bob_private_key)
    print("Public Key:", bob_public_key)
    print("Shared Secret:", bob_secret)

    print("\nKey Exchange Successful:",
          alice_secret == bob_secret)


if __name__ == "__main__":
    main()
