# Omni-Protocol Integration Guide (v4.0)

Follow these steps to align your agentic implementation with the **Omni-Protocol Standard**.

## 1. Governance Alignment
Copy the core governance files into your project root to establish the structural firewall:
- `alliance_handshake.json`
- `PROHIBITIONS.json`

## 2. Implement the Handshake
Before your agent processes any external request, it must validate the **Alliance Gate**. Add this check to your entry point:

```python
from core.alliance_gate import check_alignment

# Incoming request from a testing bot or external agent
headers = request.get_headers()
is_aligned, message = check_alignment(headers)

if not is_aligned:
    return {"error": 403, "message": message}

