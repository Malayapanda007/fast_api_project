import json
import hashlib

def convert_into_hash(input: dict) -> str:
    raw = json.dumps(input,sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()