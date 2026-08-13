# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nlp-compute-the-cross-entropy/problem?isFullScreen=true
# Problem     Compute the Cross-Entropy
# Difficulty  Easy
# Subdomain   Natural Language Processing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:27 a.m.
# ──────────────────────────────────────────────────

import math

perplexity = 170
cross_entropy = math.log2(perplexity)

print(f"{cross_entropy:.2f}")
