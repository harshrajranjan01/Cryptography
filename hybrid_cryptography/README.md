# 🔐 Hybrid Cryptography System

### Secure Message Communication Using RSA, AES-256-GCM & Digital Signatures

**Confidentiality | Integrity | Authentication**

A Python-based educational project demonstrating how symmetric encryption, asymmetric encryption, and digital signatures work together to establish secure communication between two parties.

The project simulates a real-world communication scenario in which Alice sends a confidential, digitally signed message to Bob.

It combines the efficiency of AES symmetric encryption with RSA asymmetric cryptography to protect the message and its encryption key.

---

## 📌 1. Project Overview

Imagine Alice wants to send a confidential message to Bob over an untrusted communication channel.

She has three important requirements:

1. **Confidentiality:** Nobody except Bob should be able to read the message.
2. **Integrity:** Bob should be able to detect whether the message has been modified.
3. **Authentication:** Bob should be able to verify that the message carries a valid signature created using Alice's private key.

Using only one cryptographic algorithm is not the most suitable way to address all three requirements.

This is where **Hybrid Cryptography** becomes useful.

The project combines:

- **AES-256-GCM:** Encrypts the actual message payload.
- **RSA-OAEP:** Protects the AES session key using Bob's public key.
- **RSA-PSS:** Creates and verifies Alice's digital signature.
- **SHA-256:** Provides cryptographic hashing used by the RSA schemes.

The result is a complete educational demonstration of a hybrid cryptographic communication workflow.

---

## 🎯 2. What Does This Project Demonstrate?

| Security property | How this project demonstrates it |
|---|---|
| Confidentiality | AES-256-GCM encrypts the message payload |
| Secure key delivery | RSA-OAEP encrypts the AES session key |
| Integrity | AES-GCM authentication and RSA-PSS signature verification |
| Signature verification | Bob verifies Alice's signature using her public key |
| Hybrid encryption | Combines AES symmetric encryption and RSA asymmetric encryption |

**Important distinction:** A valid digital signature proves that the signature corresponds to the supplied public key. To establish Alice's identity, Bob must also trust that the public key genuinely belongs to Alice.

---

## 🧠 3. Understanding the Main Concept

### Why do we need Hybrid Cryptography?

There are two major types of encryption.

**A. Symmetric Encryption**

The same secret key is used for encryption and decryption.

Example: AES-256-GCM.

```text
              SECRET AES KEY
                    |
          +---------+---------+
          |                   |
          v                   v
      Encryption          Decryption
          |                   |
          v                   v
     Ciphertext            Plaintext
```

Advantages:
- Fast encryption and decryption.
- Suitable for large amounts of data.
- Efficient for files, messages, and network traffic.

Problem:

How can Alice securely provide Bob with the secret AES key without exposing it to an attacker?

**B. Asymmetric Encryption**

Uses two mathematically related keys:

- Public key
- Private key

Example: RSA.

```text
         Bob's RSA Key Pair
                 |
          +------+------+
          |             |
          v             v
       Public Key    Private Key
          |             |
          v             v
       Encryption    Decryption
```

The public key can be shared, while the private key must remain secret.

Problem:

RSA is not normally used to encrypt large amounts of application data directly.

**C. The Hybrid Cryptography Solution**

Combine both approaches.

```text
             ALICE
               |
               v
         Original Message
               |
               v
        AES-256-GCM Encryption
               |
               v
           Ciphertext
               |
        +------+------+
        |             |
        v             v
     AES Key       Nonce
        |
        v
  RSA-OAEP Encryption
  (Bob's Public Key)
        |
        v
   Encrypted AES Key
        |
        v
     TRANSMISSION
        |
        v
         BOB
        |
        v
  RSA-OAEP Decryption
  (Bob's Private Key)
        |
        v
    Recover AES Key
        |
        v
  AES-256-GCM Decryption
        |
        v
   Original Message
```

This approach uses AES for efficient data encryption and RSA to protect the AES session key.

---

## 🔄 4. Complete Project Workflow

The project simulates two participants:

- **Alice:** Sender of the message.
- **Bob:** Receiver of the message.

### 📤 Part A: Alice — Sending a Secure Message

**Step 1: RSA Key Generation**

Alice and Bob each generate their own RSA public and private key pairs.

```text
Alice:
    Alice Private Key
    Alice Public Key

Bob:
    Bob Private Key
    Bob Public Key
```

Alice needs Bob's public key to encrypt the AES session key.

Bob needs Alice's public key to verify her digital signature.

**Step 2: Message Conversion**

Alice starts with a normal Python string:

```python
message = "Hello Bob! This is a secret message."
```

She converts it into bytes:

```python
message_bytes = message.encode("utf-8")
```

Cryptographic operations in this implementation work with bytes rather than ordinary Python strings.

**Step 3: Digital Signature Creation — RSA-PSS**

Alice signs the original message bytes using her RSA private key.

```text
Original Message
       |
       v
     SHA-256
       |
       v
    RSA-PSS
       |
       v
 Digital Signature
```

The signature is created using:

- RSA-PSS padding
- MGF1 with SHA-256
- SHA-256
- Maximum supported salt length

The signature will later allow Bob to verify that the recovered message matches the signed message.

**Step 4: Payload Creation**

The original message and signature are combined into a JSON payload.

```json
{
    "message": "Hello Bob! This is a secret message.",
    "signature": "hex_encoded_signature"
}
```

The signature is converted into hexadecimal because JSON does not directly support Python bytes.

The JSON payload is then encoded into UTF-8 bytes.

**Step 5: AES-256-GCM Encryption**

Alice encrypts the entire payload using AES-256-GCM.

The implementation generates:

- AES key: 256 bits (32 bytes)
- Nonce: 96 bits (12 bytes)
- Ciphertext: Encrypted payload with an authentication tag

```text
       JSON PAYLOAD
             |
             v
       AES-256-GCM
             |
       +-----+------+
       |            |
       v            v
    AES Key       Nonce
       |
       v
   Ciphertext
   + Authentication Tag
```

The AES key is secret. The nonce does not need to be secret, but it must be unique for each encryption under the same key.

**Step 6: RSA-OAEP Encryption of the AES Key**

Alice encrypts the AES session key using Bob's RSA public key.

```text
       AES SESSION KEY
              |
              v
          RSA-OAEP
              |
       Bob's Public Key
              |
              v
      ENCRYPTED AES KEY
```

The implementation uses OAEP with MGF1 and SHA-256.

Only the corresponding Bob private key should be able to decrypt the encrypted AES key.

**Step 7: Transmission Package**

Alice prepares the package:

```python
package = {
    "encrypted_key": encrypted_key,
    "nonce": nonce,
    "ciphertext": ciphertext
}
```

This package contains everything Bob needs to recover the payload, assuming he has the correct private key and authentic Alice public key.

---

### 📥 Part B: Bob — Receiving and Verifying the Message

Bob receives Alice's package.

**Step 1: AES Key Decryption**

Bob uses his RSA private key to decrypt the encrypted AES key.

```text
Encrypted AES Key
        |
        v
     RSA-OAEP
        |
   Bob's Private Key
        |
        v
  Original AES Key
```

**Step 2: AES-256-GCM Decryption**

Bob uses the recovered AES key and the original nonce to decrypt the ciphertext.

AES-GCM also verifies the authentication tag.

If the ciphertext, nonce, or authentication tag has been modified, decryption fails with an `InvalidTag` exception.

**Step 3: Payload Extraction**

Bob extracts the message and digital signature from the recovered JSON payload.

```text
       JSON PAYLOAD
             |
             v
       JSON Parsing
             |
       +-----+------+
       |            |
       v            v
    Message      Signature
```

The hexadecimal signature is converted back into bytes.

**Step 4: Digital Signature Verification**

Bob converts the recovered message into UTF-8 bytes and verifies the signature using Alice's public key.

```text
     Recovered Message
             |
             v
          SHA-256
             |
             v
      RSA-PSS Verification
             ^
             |
       Alice's Public Key
             |
             v
      Verification Result
```

If verification succeeds, Bob accepts the message.

If verification fails, Bob rejects it.

---

## 🌍 5. Real-World Applications: Where Is This Actually Used?

This is one of the most important parts of understanding this project.

The algorithms you implemented are not merely theoretical concepts. The same cryptographic building blocks and security principles appear in real-world systems.

### A. Secure Messaging Applications

<details>
<summary><strong>Example: Sending an encrypted message to another person</strong></summary>

Imagine sending a private message through a secure messaging application.

A simplified communication process looks like this:

1. The sender and receiver establish or obtain appropriate cryptographic keys.
2. A symmetric encryption key is used to encrypt message content.
3. The encrypted message is transmitted.
4. The receiver obtains the necessary key material and decrypts the message.
5. Authentication mechanisms help detect unauthorized modifications and establish who is communicating.

**Connection to this project:**

| Your project | Messaging system concept |
|---|---|
| Alice | Sender |
| Bob | Receiver |
| AES-256-GCM | Message encryption and authentication |
| RSA key pair | Public-key cryptographic operations |
| Digital signature | Sender authentication mechanism |

Real messaging protocols may use different key exchange mechanisms, identity systems, and end-to-end encryption designs. They are more sophisticated than this demonstration.

</details>

### B. HTTPS and TLS — Secure Website Communication

<details>
<summary><strong>Example: Logging into a banking website</strong></summary>

When you visit a banking website using HTTPS, your browser and the web server establish a protected communication channel.

A simplified TLS handshake involves:

1. The browser connects to the server.
2. The server presents its digital certificate.
3. The browser checks the certificate and the server's identity.
4. Cryptographic key agreement establishes shared session secrets.
5. Symmetric authenticated encryption protects application data.

**Connection to this project:**

| Your project | TLS-related concept |
|---|---|
| RSA public/private keys | Asymmetric cryptography |
| RSA-PSS | Digital signature schemes |
| AES-GCM | Authenticated encryption |
| AES session key | Symmetric session secrets |
| Public-key verification | Certificate and identity validation |

An important distinction: modern TLS commonly uses ephemeral Diffie-Hellman key exchange, such as ECDHE, rather than RSA-OAEP to encrypt a session key. TLS also uses a defined protocol for authentication, key derivation, and record protection.

Your project demonstrates the underlying cryptographic ideas, not a complete TLS implementation.

</details>

### C. Secure File Sharing

<details>
<summary><strong>Example: Sending a confidential PDF to someone</strong></summary>

Imagine Alice wants to send a confidential PDF document to Bob.

A system based on the concepts in your project could:

1. Generate a random AES session key.
2. Encrypt the PDF using AES-GCM.
3. Protect the AES key using Bob's public key.
4. Sign the document or its cryptographic digest using Alice's private key.
5. Send the encrypted document, nonce, encrypted key, and signature.
6. Allow Bob to decrypt the document and verify its signature.

**Connection to this project:**

Your current message payload could conceptually be replaced by a file payload.

```text
         Original PDF
              |
              v
        AES-256-GCM
              |
              v
       Encrypted PDF
              |
              v
      RSA-OAEP protects
         AES key
              |
              v
        Secure Package
              |
              v
             Bob
              |
              v
       Decrypt PDF
              |
              v
       Verify Signature
```

This is particularly relevant to encrypted document transfer, secure backups, and protected file exchange.

</details>

### D. Software Distribution and Digital Signatures

<details>
<summary><strong>Example: Downloading a software installer</strong></summary>

Suppose a software developer releases an application installer.

An attacker might try to modify the installer before it reaches users.

Digital signatures help users verify that the downloaded software matches what the publisher signed.

A simplified process:

1. The developer calculates a cryptographic hash of the software.
2. The developer signs the relevant data using a private signing key.
3. The software and signature are distributed.
4. The user verifies the signature using the developer's trusted public key.

**Connection to this project:**

Your RSA-PSS implementation demonstrates the basic signing and verification mechanism used in this type of workflow.

The important idea is that encryption and digital signatures solve different problems: encryption protects confidentiality, while signatures help establish integrity and signer-key authenticity.

</details>

---

## 🧩 6. Understanding Each Algorithm in Your Project

| Algorithm | What it does | Why it is needed |
|---|---|---|
| RSA-2048 | Generates public/private key pairs | Asymmetric cryptographic operations |
| RSA-OAEP | Encrypts and decrypts the AES key | Protects the session key |
| RSA-PSS | Creates and verifies signatures | Message signature verification |
| AES-256-GCM | Encrypts and authenticates payloads | Confidentiality and integrity |
| SHA-256 | Produces cryptographic hashes | Used by RSA-OAEP and RSA-PSS |
| MGF1 | Generates mask data | Used by OAEP and PSS padding schemes |
| JSON | Serializes message and signature | Organizes payload data |
| Hexadecimal encoding | Represents signature bytes as text | Makes signature suitable for JSON |

---

## 📁 7. Project Structure

```text
hybrid_cryptography/
│
├── main.py                  # Main application controller
│
├── key_generation.py        # RSA key generation
│
├── digital_signature.py     # RSA-PSS signing and verification
│
├── encryption.py            # AES-256-GCM encryption
│
├── decryption.py            # AES-256-GCM decryption
│
├── rsa_encryption.py        # RSA-OAEP AES key encryption
│
├── rsa_decryption.py        # RSA-OAEP AES key decryption
│
├── payload.py                # JSON payload creation
│
├── payload_parser.py         # Payload extraction
│
├── alice.py                  # Alice's sending workflow
│
└── bob.py                    # Bob's receiving workflow
```

### Module Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Coordinates the complete application |
| `key_generation.py` | Generates RSA keys for Alice and Bob |
| `digital_signature.py` | Creates and verifies RSA-PSS signatures |
| `encryption.py` | Encrypts payloads using AES-GCM |
| `decryption.py` | Decrypts AES-GCM ciphertext |
| `rsa_encryption.py` | Encrypts AES keys using Bob's public key |
| `rsa_decryption.py` | Decrypts AES keys using Bob's private key |
| `payload.py` | Combines message and signature into JSON |
| `payload_parser.py` | Recovers message and signature |
| `alice.py` | Implements sender-side operations |
| `bob.py` | Implements receiver-side operations |

---

## ⚙️ 8. Installation and Execution

### Prerequisites

- Python 3.9 or later
- pip package manager

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the project directory

```bash
cd hybrid_cryptography
```

### Step 3: Install the dependency

```bash
pip install cryptography
```

### Step 4: Execute the project

```bash
python main.py
```

---

## 💻 9. Sample Output

```text
=========GENERATING RSA KEYS=========

[+] Alice's RSA key generated
[+] Bob's RSA key generated

Original Message:
Hello Bob!, This is digitally signed and Encrypted Message.

=========== Alice: SENDING MESSAGE ===========

[+] Digital Signature created
[+] Payload Created
[+] Message and signature encrypted using AES-256-GCM
[+] AES key encrypted using Bob's RSA public key
[+] Package ready for transmission

[+] Alice's sending process completed

========== BOB: RECEIVING MESSAGE ==========

[+] AES key decrypted
[+] Payload Decrypted
[+] Message and signature extracted
[+] DIGITAL SIGNATURE VERIFIED
[+] Message integrity confirmed

========== FINAL RESULT ==========

Received Message:
Hello Bob!, This is digitally signed and Encrypted Message.
```

The cryptographic keys, nonce, ciphertext, and signatures are generated dynamically, so their values differ between executions.

---

## 📚 10. What I Learned From This Project

This project helped me understand how individual cryptographic algorithms combine to form a complete communication system.

Key learning outcomes:

- Difference between symmetric and asymmetric cryptography.
- Why hybrid encryption is more practical than using RSA alone for large messages.
- How RSA-OAEP protects a symmetric session key.
- How RSA-PSS creates and verifies digital signatures.
- How AES-GCM provides authenticated encryption.
- Why a nonce is required in AES-GCM.
- Why cryptographic functions operate on bytes.
- How JSON serialization works with binary signature data.
- How sender-side and receiver-side cryptographic workflows interact.
- How modular programming helps organize a cryptographic application.

---

## ⚠️ 11. Scope and Security Disclaimer

This project is an educational implementation designed to understand cryptographic concepts and their interaction.

It is not a production-ready secure communication protocol.

Current limitations:

- RSA key pairs are regenerated each time the program runs.
- Public-key authenticity and certificate validation are not implemented.
- The transmission package is an in-memory Python dictionary, not an actual network protocol.
- The implementation has not undergone comprehensive security testing.
- Production-grade key management, protocol protections, and operational security are outside the project's scope.

The project uses established cryptographic primitives through the Python `cryptography` library rather than implementing the underlying algorithms from scratch.

It should not be used to protect real-world sensitive information.

---

## 🏁 12. Final Summary

The Hybrid Cryptography System demonstrates how multiple cryptographic techniques work together to solve different security problems.

**Alice signs the message, encrypts the payload, and protects the AES session key. Bob decrypts the session key, recovers the payload, and verifies Alice's signature.**

The central lesson of this project is:

> Strong cryptographic systems do not depend on a single algorithm. They combine different cryptographic techniques, with each technique serving a specific security purpose.

**Project:** Hybrid Cryptography System  
**Language:** Python  
**Library:** Cryptography  
**Status:** Educational implementation completed.

---

<p align="center">
  <strong>🔐 Learning Cryptography Through Practical Implementation</strong>
  <br/>
  <em>Understand the algorithms. Understand the workflow. Understand the real-world applications.</em>
</p>