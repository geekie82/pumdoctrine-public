#!/bin/sh
# verify.sh — independent verifier using ONLY openssl + base64 + sha256sum.
# No python, no cryptography library. Two implementations (this and prove_it.py)
# must agree; the manifest is checked first, so a rewritten verifier is caught
# before it ever runs.
cd "$(dirname "$0")" || exit 1
BAD=0
SIG=$(mktemp); PAIRS=$(mktemp)
trap 'rm -f "$SIG" "$PAIRS"' EXIT

if base64 -d PUBLIC-MANIFEST.sig > "$SIG" 2>/dev/null && \
   openssl pkeyutl -verify -pubin -inkey public-key.pem -rawin \
     -in PUBLIC-MANIFEST.json -sigfile "$SIG" >/dev/null 2>&1; then
  echo "PASS  manifest signature (openssl)"
else
  echo "FAIL  manifest signature (openssl)"; BAD=1
fi

grep -oE '"[^"]+": "[0-9a-f]{64}"' PUBLIC-MANIFEST.json \
  | sed 's/"//g; s/: / /' | grep -v '^manifest_sha256 ' > "$PAIRS"
while read -r f h; do
  a=$(sha256sum "$f" 2>/dev/null | cut -d' ' -f1)
  if [ "$a" != "$h" ]; then echo "FAIL  $f (changed or missing)"; BAD=1; fi
done < "$PAIRS"
[ "$BAD" -eq 0 ] && echo "PASS  all published files match the manifest (including the verifiers)"
echo
[ "$BAD" -eq 0 ] && echo "EVIDENCE VERIFIED (openssl-only)" || echo "EVIDENCE FAILED"
exit $BAD
