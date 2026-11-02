# Hybrid Cryptography System

A Python-based implementation of a hybrid cryptographic communication system that combines **RSA asymmetric cryptography, AES symmetric encryption, and digital signatures** to provide confidentiality, integrity, and sender authentication.

## 1. Project Overview

This project demonstrates how two parties, Alice and Bob, can securely exchange messages using a combination of symmetric and asymmetric cryptographic techniques.

The system uses:

- RSA for asymmetric key operations.
- AES-256-GCM for message encryption and authentication.
- RSA-PSS for digital signatures.
- RSA-OAEP for securely encrypting the AES session key.
- SHA-256 for cryptographic hashing.
- JSON for payload serialization.

The implementation follows a modular architecture, separating cryptographic operations into individual Python files.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Cryptography | Cryptographic library |
| RSA-2048 | Asymmetric key generation |
| RSA-OAEP | AES key encryption |
| RSA-PSS | Digital signatures |
| AES-256-GCM | Authenticated message encryption |
| SHA-256 | Cryptographic hashing |
| MGF1 | Mask generation function |
| JSON | Payload serialization |

## 3. Project Architecture

```text
hybrid_cryptography/
│
├── main.py
│
├── key_generation.py
│
├── digital_signature.py
│
├── encryption.py
│
├── decryption.py
│
├── rsa_encryption.py
│
├── rsa_decryption.py
│
├── payload.py
│
├── payload_parser.py
│
├── alice.py
│
└── bob.py
```

### Module Description

| File | Responsibility |
|---|---|
| `main.py` | Controls the complete communication workflow |
| `key_generation.py` | Generates RSA public and private key pairs |
| `digital_signature.py` | Creates and verifies RSA-PSS signatures |
| `encryption.py` | Encrypts payloads using AES-256-GCM |
| `decryption.py` | Decrypts AES-GCM ciphertext |
| `rsa_encryption.py` | Encrypts AES keys using RSA-OAEP |
| `rsa_decryption.py` | Decrypts AES keys using RSA-OAEP |
| `payload.py` | Combines message and signature into a JSON payload |
| `payload_parser.py` | Extracts message and signature from the payload |
| `alice.py` | Implements Alice's message-sending process |
| `bob.py` | Implements Bob's message-receiving process |

## 4. Cryptographic Workflow

### Alice — Sending Process

1. Alice generates her RSA public and private key pair.
2. Bob generates his RSA public and private key pair.
3. Alice converts the original message into bytes using UTF-8 encoding.
4. Alice creates a digital signature using her RSA private key and RSA-PSS.
5. The original message and digital signature are combined into a payload.
6. The payload is encrypted using AES-256-GCM.
7. A random 256-bit AES key and 96-bit nonce are generated.
8. Alice encrypts the AES key using Bob's RSA public key and RSA-OAEP.
9. Alice prepares a transmission package containing:
   - Encrypted AES key
   - Nonce
   - Ciphertext (including the GCM authentication tag)

### Bob — Receiving Process

1. Bob receives Alice's encrypted package.
2. Bob decrypts the AES key using his RSA private key.
3. Bob decrypts the payload using AES-256-GCM.
4. Bob extracts the original message and digital signature.
5. Bob converts the recovered message into bytes.
6. Bob verifies the digital signature using Alice's RSA public key.
7. If verification succeeds, Bob accepts the message.

### Workflow Diagram

```text
                 ALICE
                   |
             Original Message
                   |
                   v
          Convert Message to Bytes
                   |
                   v
           Create Digital Signature
                (RSA-PSS)
                   |
                   v
           Create JSON Payload
          (Message + Signature)
                   |
                   v
           AES-256-GCM Encryption
                   |
                   v
             AES Session Key
                   |
                   v
          RSA-OAEP Key Encryption
                   |
                   v
           Transmission Package
                   |
          ---------------------
                 NETWORK
          ---------------------
                   |
                   v
                  BOB
                   |
                   v
          RSA-OAEP Key Decryption
                   |
                   v
          AES-256-GCM Decryption
                   |
                   v
           Extract Message and
              Signature
                   |
                   v
          RSA-PSS Verification
                   |
                   v
           Accept / Reject Message
```

## 5. Cryptographic Algorithms Explained

### RSA-2048

RSA is an asymmetric cryptographic algorithm that uses a public key and a private key.

- Public key: Used for encryption and signature verification.
- Private key: Used for decryption and signature creation.

### RSA-OAEP

Optimal Asymmetric Encryption Padding is used to securely encrypt the AES session key using Bob's RSA public key.

Configuration:
- RSA key size: 2048 bits
- Padding: OAEP
- Mask generation: MGF1
- Hash algorithm: SHA-256

### AES-256-GCM

Advanced Encryption Standard with a 256-bit key in Galois/Counter Mode is used to encrypt the actual message payload.

Configuration:
- Key size: 256 bits
- Nonce size: 96 bits (12 bytes)
- Authentication: GCM authentication tag
- Associated authenticated data (AAD): None in the current implementation

### RSA-PSS

Probabilistic Signature Scheme is used to create and verify digital signatures.

Configuration:
- Padding: PSS
- Hash algorithm: SHA-256
- Mask generation: MGF1 with SHA-256
- Salt length: Maximum supported length

## 6. Installation

Clone or download the project and navigate to its directory.

Install the required Python library:

```bash
pip install cryptography
```

## 7. Running the Project

Execute the main Python file:

```bash
python main.py
```

The application will:

1. Generate RSA key pairs for Alice and Bob.
2. Execute Alice's sending process.
3. Prepare the encrypted transmission package.
4. Execute Bob's receiving process.
5. Verify the digital signature.
6. Display the recovered message if verification succeeds.


**Project:** Hybrid Cryptography System  
**Language:** Python  
**Cryptographic Library:** Python Cryptography  

