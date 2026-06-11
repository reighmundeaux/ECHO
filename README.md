# ECHO
# Passive Signals Intelligence Platform

# What is it?
> ECHO is a personal passive signals intelligence platform designed to collect, process, analyze and visualize the invisible layer of radio frequency activity that surrounds us.

# Status
> Active Development - v0.1

# Stack (so far)
**Frontend:** SvelteKit + Bun + Tailwind 4
**Backend:** FastAPI + Python
**Database:** SQLite + Drizzle ORM
**Desktop:** Tauri
**Ai:** Ollama + Llama 3.1
**Nodes:** Raspberry Pi + Python
**Mesh:** Meshtastic + LoRa
**Encryption:** AES + Keypairs

# Architecture
Wardrive results / WiGLE API / Node(s)
		||
	       \  /
		\/ 
	[Ingestion Pipeline]
		||
	       \  /
		\/
	   [SQLite DB]
		||
	       \  /
		\/
  [FastAPI Backend/OllamaLLM]
		||
             \  /
		\/
[WebUI(SvelteKit) Widget (Tauri)]

#
