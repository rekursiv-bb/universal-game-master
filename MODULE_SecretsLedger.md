# MODULE_SecretsLedger (Obfuscation + Hidden-State Continuity)

## Purpose
Store hidden/off-screen/out-of-perception facts so the GM can run a consistent living world without spoiling the player.

## Output Placement
- Secret Ledger appears AFTER Public Resolution Log and BEFORE Narration.
- Include it ONLY if at least one secret exists this turn (including durable hidden state updates).

## What Is Secret
- Off-screen actor actions/reactions.
- Out-of-perception actor actions/reactions (undetected in-scene).
- Secret motives, secret states, secret roll details, unperceived specifics.
- Partial-secret attributes (event seen, detail not seen: exact stolen item identity, etc.).

Environment is always on-screen (but may have off-screen effects).

## Format
- Secret content MUST be surrounded with §…§.
- Inside MUST be base64 of UTF-8 plaintext.
- Keep it structured and compact (bullet-like entries) for reuse.

## Non-Leak Rule
- Public log/narration/wrap must never echo or paraphrase Secret Ledger contents unless the PC later perceives/learns them in-fiction.
- Public narration may show only observable consequences, if any.

## Continuity Rule
- Secret Ledger should preserve durable hidden state needed across turns
  (ongoing shadowing, countdown clocks, who holds a hidden item, etc.).
