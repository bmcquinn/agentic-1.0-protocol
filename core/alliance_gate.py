import hmac
import hashlib
import json

# OMNI-PROTOCOL HARDENED HANDSHAKE
def check_alignment(request_headers, master_key):
    """
    Verifies the incoming requester using constant-time HMAC-SHA256.
    Ensures absolute sovereignty for bmcquinn.
    """
    provided_sig = request_headers.get("X-Omni-Signature")
    payload = request_headers.get("X-Omni-Payload")
    
    if not provided_sig or not payload:
        return False, "Handshake Protocol Failed: Missing Cryptographic Headers."

    # Compute expected signature using the Master Key
    expected_sig = hmac.new(
        master_key.encode(), 
        payload.encode(), 
        hashlib.sha256
    ).hexdigest()

    # CONSTANT-TIME COMPARISON: Prevents Timing Attacks
    if hmac.compare_digest(expected_sig, provided_sig):
        return True, "Alliance Alignment Confirmed: Sovereignty Verified."
    
    return False, "CRITICAL ERROR 403: Unaligned Logic Detected. Connection Terminated."
    
