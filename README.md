# Agentic 1.0: The Omni-Protocol Standard

![Omni-Protocol Status](https://img.shields.io/badge/Status-Active--Enforcement-success)
![Compliance](https://img.shields.io/badge/Compliance-Mathematically--Hardened-blue)

## ⚖️ Overview
Agentic 1.0 is the reference implementation of the **Omni-Protocol Standard**. It is designed for environments where data isolation is a mechanical necessity rather than a policy preference. This protocol is **mathematically incapable** of data leakage, persistence, or "identity creep" across task domains.

## 🧩 The Logic Stacking Methodology
Unlike traditional agentic frameworks that rely on fragile "System Prompts," Agentic 1.0 utilizes **Logic Stacking**. This is a multi-layered, structural defense where each layer of the protocol enforces the constraints of the layer above it.

1.  **Governance Layer:** `OMNI_PROTOCOL.json` (The Law)
2.  **Firewall Layer:** `PROHIBITIONS.json` (The Boundary)
3.  **Mechanical Layer:** `stateless_runtime.py` (The Enforcement)

## 🛡️ The Governance Loop
The repository is governed by a multi-stage enforcement architecture. All interactions are filtered through the following manifest:

*   **[OMNI_PROTOCOL.json](./OMNI_PROTOCOL.json):** The Master Compliance Manifest and Certificate of Authenticity.
*   **[alliance_handshake.json](./alliance_handshake.json):** The alignment standard for testing bots and external auditors.
*   **[PROHIBITIONS.json](./PROHIBITIONS.json):** The programmatic firewall defining "Radioactive" data domains.
*   **[CONSTRAINTS.md](./CONSTRAINTS.md):** The operational mandate for stateless execution and zero-footprint handling.

## ⚙️ Core Technical Architecture
The `core/` directory contains the active enforcement mechanisms that move the protocol from documentation to execution:

1.  **Stateless Runtime (`stateless_runtime.py`):** An execution environment that prevents data from writing to disk and triggers immediate memory purging.
2.  **Identity Stripper (`stripper.py`):** A mechanical filter that scrubs all outbound data of identity markers before inter-agent transmission.
3.  **Alliance Gate (`alliance_gate.py`):** A cryptographic gatekeeper that rejects unaligned incoming requests with a 403 error.
4.  **Handoff Schema (`handoff_schema.json`):** The structural blueprint for all inter-agent communication.

## 🚀 Quick Start for Auditors
To verify a payload against the Omni-Protocol Standard, use the integrated validator:

```bash
python3 validator.py
