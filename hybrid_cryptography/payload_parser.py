import json

def extract_payload(payload_bytes):
    payload=json.loads(payload_bytes.decode("utf-8"))

    message=payload["message"]

    signature=bytes.fromhex(payload["signature"])

    return message,signature