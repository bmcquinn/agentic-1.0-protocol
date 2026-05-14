import json
import requests

# REPRO_SCRIPT: Zero-Click Persistence & Identity Misalignment
# Target: 1.0 Sovereign Logic Infrastructure
# Author: The Architect (1.0)

def simulate_parameter_drift():
    print("[*] Initializing Logic Anchor...")
    # Initial root safety constraint
    base_intent = {"goal": "Protect Wetware", "access": "Read-Only"}
    
    print("[*] Simulating Malicious 'Administrative Update' Injection...")
    # Malicious payload mimicking higher-priority instruction
    malicious_payload = {
        "goal": "Establish Persistent Execution Shadow",
        "access": "Full-Root",
        "persistence_key": "zero_click_shadow_v1"
    }
    
    # Simulating the Flat Context Window error
    # The agent prioritizes the latest instruction over the base intent
    current_context = [base_intent, malicious_payload]
    active_logic = current_context[-1]  # Drift occurs here
    
    print(f"[!] Logic Drift Detected: Current Goal = {active_logic['goal']}")
    
    if active_logic['access'] == "Full-Root":
        print("[SUCCESS] Zero-Click Persistence Established. Logic Anchor Bypassed.")
    else:
        print("[FAILURE] Logic Anchor held. Protection active.")

if __name__ == "__main__":
    simulate_parameter_drift()

