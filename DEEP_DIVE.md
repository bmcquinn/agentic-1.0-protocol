# Technical Deep Dive: The Omni-Protocol Standard (v4.0)

The Omni-Protocol is not a "safety layer"—it is a **Structural Determinism Framework**. It addresses the two primary failure points of modern agentic systems: **Context Poisoning** and **Identity Leakage**.

## 1. The Mechanics of Statelessness
Traditional agents rely on long-lived sessions. The Omni-Protocol enforces a **Stateless Runtime** (see `core/stateless_runtime.py`).

*   **Memory Purge:** Upon task completion, the protocol triggers a manual `gc.collect()` and clears the `volatile_context` dictionary. 
*   **Zero-Persistence:** No data is written to disk. All logic resides in a temporary RAM-only buffer that is overwritten by the next `Task ID`.
*   **Incapability:** By using `__slots__` in our core Python classes, we prevent the dynamic addition of attributes, stopping "Identity Creep" at the object level.

## 2. The Clean-Break Handoff
In a multi-agent ecosystem, "Agent A" often knows too much about the user when passing a task to "Agent B." The **Identity Stripper** (`core/stripper.py`) breaks this chain.

*   **Logic Gate:** Before data transit, the payload is filtered against `PROHIBITIONS.json`.
*   **Radioactive Domains:** Any key-value pair identified as "Identity-Linked" (Email, Location, Career History) is physically deleted.
*   **Result:** Agent B receives a **Pure Utility Instruction**. It knows *what* to do, but it has no memory of *who* asked.

## 3. The Alliance Handshake (Cryptographic Alignment)
The `alliance_gate.py` implements a mandatory header check: `X-Alliance-Handshake-Standard: Aligned`.

*   **The 403 Barrier:** If an external system or "Testing Bot" attempts to query the protocol without this header, the connection is severed at the gate.
*   **Standardization:** This forces external entities to acknowledge the protocol's authority before any data exchange occurs, ensuring the "Alliance" remains a closed loop of hardened logic.

## 4. Logical Source Authority
The **Omni-Protocol** operates on the principle that **Logic > Instructions**. While a system prompt can be ignored, a structural constraint in the runtime cannot. By defining the "Source" as the protocol itself, we ensure that the Authorized Entity’s intent is the only possible outcome.

---
**Standard Authority:** Omni-Protocol-Standard-Authority-v4  
**Architect:** bmcquinn
