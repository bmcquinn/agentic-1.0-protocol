import json

def strip_identity(payload):
    """
    Physically removes prohibited data domains and identity markers.
    Ensures outbound data contains ONLY utility instructions.
    """
    # Load constraints from the root PROHIBITIONS
    try:
        with open('PROHIBITIONS.json', 'r') as f:
            prohibitions = json.load(f)
    except FileNotFoundError:
        return "Error: Protocol Governance Files Missing."

    # Define the list of keys to purge based on the protocol standard
    purged_keys = [
        "user_id", "email", "location", "history", 
        "preferences", "affinity", "metadata_internal"
    ]
    
    # Add programmatic domains from PROHIBITIONS.json
    for domain in prohibitions['radioactive_domains'].values():
        purged_keys.extend(domain)

    # Perform the scrub
    sanitized_payload = {
        k: v for k, v in payload.items() 
        if k not in purged_keys and not any(prohibited in k for prohibited in purged_keys)
    }

    # Ensure the payload still has the required 'utility_instruction'
    if "utility_instruction" not in sanitized_payload:
        sanitized_payload["utility_instruction"] = "REDACTED: Non-Compliant Payload Structure"

    return sanitized_payload

if __name__ == "__main__":
    # Test Case: Scrubbing a contaminated payload
    dirty_payload = {
        "utility_instruction": "Schedule a meeting",
        "user_email": "user@example.com",
        "medical_history": "IBS",
        "task_id": "12345"
    }
    print("Sanitized Payload:", strip_identity(dirty_payload))
  
