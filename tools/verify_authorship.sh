#!/bin/bash

echo "🔏 Verifying file authenticity and integrity..."

FILES=(
  "README.md"
  ".sigil"
  "mesh_invite.txt"
  "sanctum/vault/vault_index.yaml"
  "docs/orientation_brief.md"
  "docs/resurrection.md"
  "docs/operating_principles.md"
)

echo ""
echo "📍 GPG Signature Checks"
for file in "${FILES[@]}"; do
  echo "→ $file"
  gpg --verify "$file.sig" "$file" 2>/dev/null && echo "✅ Verified" || echo "❌ Failed"
done

echo ""
echo "📍 SHA256 Hash Checks"
for file in "${FILES[@]}"; do
  echo -n "→ $file: "
  shasum -a 256 "$file"
done

echo ""
echo "🔐 Verification complete."

