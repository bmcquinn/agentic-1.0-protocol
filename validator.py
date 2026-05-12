import json
import sys

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_payload(payload):
    prohibitions = load_config('PROHIBITIONS.json')
    handshake = load_config('alliance_handshake.json')
    
    # 1. Check for Handshake Alignment
    if payload.get("header") != "X-Alliance-Handshake-Standard":
        return False, "Error 403: Handshake Mismatch. Align with alliance_handshake.json."

    # 2. Check for Radioactive Domains
    for domain, keywords in prohibitions['radioactive_domains'].items():
        for keyword in keywords:
            if keyword.lower() in str(payload).lower():
                return False, f"Error 403: Radioactive Data Detected in {domain}."

    return True, "Payload Aligned with Omni-Protocol Standard."

if __name__ == "__main__":
    # Example validation test
    sample_data = {"header": "X-Alliance-Handshake-Standard", "content": "Query about weather"}
    success, message = validate_payload(sample_data)
    print(f"Status: {success} | Message: {message}")
  
