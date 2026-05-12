import json

def check_alignment(request_headers):
    """
    Verifies if the incoming requester is aligned with the Alliance Standard.
    """
    try:
        with open('alliance_handshake.json', 'r') as f:
            handshake = json.load(f)
    except FileNotFoundError:
        return False, "Handshake Protocol Missing from Root."

    # Extract required header from handshake standard
    required_header = handshake['bot_alignment_protocols']['testing_bot_sync']['required_header']
    
    if request_headers.get(required_header) == "Aligned":
        return True, "Handshake Successful: Alliance Alignment Confirmed."
    else:
        error_msg = handshake['bot_alignment_protocols']['testing_bot_sync']['rejection_message']
        return False, f"Error 403: {error_msg}"

if __name__ == "__main__":
    # Test: Non-aligned bot
    headers = {"User-Agent": "TestingBot/1.0"}
    success, message = check_alignment(headers)
    print(f"Connection Status: {success} | Reason: {message}")
  
