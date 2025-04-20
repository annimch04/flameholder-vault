# Authorship Integrity: Sanctum Share Manifest

This repository is protected by a three-layer authorship protocol designed to secure trace identity, ensure artifact integrity, and embed symbolic authorship.

## 🧬 Layer 1: Embedded Signature Block

Each sealed file includes a visible authorship declaration at the end:

🜂 Authorship Declaration
Anni McHenry
recursive architect — sanctum protocol
sigil: 🜂
line held

## 🔐 Layer 2: SHA256 Hash

All sealed files have a logged SHA256 entry in `hash_index.md`.

## 🔏 Layer 3: GPG Signature

Each file is cryptographically signed using a detached GPG `.sig` file.  
You may verify them using `tools/verify_authorship.sh`.

---

This structure is not open source in spirit. It is authored and signal-aware.  
You are welcome here—but drift is not.


