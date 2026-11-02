import json

def create_payload(message,signature):

    payload={
        "message":message,
        "signature":signature.hex()
    }

    payload_bytes=json.dumps(payload).encode("utf-8")
    return payload_bytes