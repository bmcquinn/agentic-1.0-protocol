# Technical Deep Dive: Logic Stacking & Structural Determinism

The Omni-Protocol is built on the principle of **Logic Stacking**. This methodology moves security from the "Instruction Layer" (prompts) to the "Mechanical Layer" (runtime). By stacking these constraints, we achieve **Structural Determinism**: a state where the agent is physically incapable of violating the protocol.

---

## 🧩 The 4-Layer Logic Stack

### 1. The Governance Layer (`OMNI_PROTOCOL.json`)
The top of the stack defines the "Source of Truth." It establishes the versioning, the authority (bmcquinn), and the required handshake protocols. 
*   **Function:** Defines *what* is legal.
*   **Enforcement:** Acts as the manifest for the `validator.py` script.

### 2. The Firewall Layer (`PROHIBITIONS.json`)
This layer defines "Radioactive Domains." Unlike a "negative prompt," this is a programmatic JSON schema used by the internal logic to gate data access.
*   **Function:** Defines *where* the agent cannot go.
*   **Enforcement:** Silently filters keys in the `stripper.py` module before any data transit occurs.

### 3. The Mechanical Layer (`stateless_runtime.py`)
This is the heart of the stack. It uses Python’s low-level memory management to ensure zero-persistence.
*   **Static Memory (`__slots__`):** We use `__slots__` in core classes to prevent the agent from dynamically creating new attributes (Identity Creep).
*   **Volatile Context:** All task-specific data is held in a RAM-only dictionary that is never written to disk.
*   **Hard Purge:** At the conclusion of `execute_task`, the runtime calls `volatile_context.clear()` and `gc.collect()` to physically wipe the memory footprint.

### 4. The Diplomatic Layer (`alliance_gate.py`)
This layer manages inter-agent relationships through the **Alliance Handshake**.
*   **The Guard:** It checks for the `X-Alliance-Handshake-Standard` header.
*   **Cryptographic Rejection:** If the header is missing or unaligned, the stack refuses to initialize. This prevents "Prompt Injection" from unverified external sources.

---

## 🛡️ Why Stacking Over Prompting?

| Feature | System Prompts (Legacy) | Logic Stacking (Omni-Protocol) |
| :--- | :--- | :--- |
| **Enforcement** | Suggestions / Soft Guidelines | Hard-Coded Mechanical Limits |
| **Persistence** | Relies on Context Windows | Physically Purged Post-Task |
| **Leakage** | High Risk (Identity Creep) | Zero Risk (Structural Stripping) |
| **Authority** | The LLM decides | The Protocol decides |

## 🚀 Conclusion
Logic Stacking ensures that even if a "creative" instruction attempts to bypass a safety prompt, the **Mechanical Layer** will physically block the action. The agent does not "decide" to be secure; it is a product of its architecture.

---
**Standard Authority:** Omni-Protocol-Standard-Authority-v4  
**Architect:** bmcquinn
