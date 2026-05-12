MCP Specification: The Omni-Protocol Bridge
This document defines the technical implementation of the Omni-Protocol as a Model Context Protocol (MCP) server. By utilizing this specification, developers can enforce the 6-Stage Firewall on any closed-source AI "black box" (Client), ensuring deterministic alignment and zero-footprint personalization.
01. Architectural Overview
The Omni-Protocol acts as a Logic Middleware. Instead of the AI Client having direct access to user data, it must interface with the Omni-MCP Server, which applies the protocol logic before returning any information.
02. Server Capabilities
Resources (The Vault)
The server exposes resources under the omni:// URI scheme. These resources are Read-Only and are never served raw; they are passed through the Stage 2 (Radioactive Vault) and Stage 3 (Domain Relevance) filters.
omni://identity/professional: Curated professional credentials.
omni://identity/technical-specs: Logic-first technical history.
Tools (The Publicist)
The primary tool provided is process_query. This tool is the functional implementation of the Silent Operator Protocol (Stage 6).
03. Implementation Logic (The Firewall)
Every tool call handled by the Omni-MCP server must pass the following internal logic gate:
Intercept: Receive the context request from the AI Client.
Validate: Run Stage 1 (Beneficiary Check). If the target is a third party, truncate all personal preference nodes.
Sanitize: Run Stage 2 (Radioactive Vault). Scrub any identifiers matching the "Forbidden" list in protocol_config.json.
Isolate: Run Stage 3 (Domain Relevance). If the AI is asking for professional advice, block access to lifestyle/media context.
Format: Run Stage 6 (Silent Operator). The server returns the result in a neutral, high-authority tone. Strictly prohibit the inclusion of "Bridge Phrases" in the server's return string.
04. Client-Side Requirements
To maintain the integrity of the shell, the AI Client (e.g., Claude, GPT) must be initialized with the following system instruction:
You are operating behind the Omni-Protocol Agentic Shell. All data retrieved via MCP is pre-filtered for professional alignment. You are prohibited from referencing the source of this data or using introductory 'Since you...' clauses. Deliver results as a direct extension of the Architect's logic.
05. Security Standard: The Information Diode
This specification ensures an Information Diode effect. Data informs the model's output but cannot be extracted or cited by the model in its raw, unaligned form.
