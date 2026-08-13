# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nlp-compute-the-cross-entropy/problem?isFullScreen=true
# Problem     Compute the Cross-Entropy
# Difficulty  Easy
# Subdomain   Natural Language Processing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:27 a.m.
# Technique   logarithmic-base-conversion
# Time        O(1)
# Space       O(1)
# Insight     The cross-entropy of a model is calculated as the base-2 logarithm of its perplexity.
# Interview   Before: "How do you relate perplexity to cross-entropy?" After: "Cross-entropy is the log base 2 of perplexity, resulting in an O(1) calculation for this specific value of 170."
# Pitfalls    (1) Using the natural logarithm instead of the base-2 logarithm for perplexity calculations.  (2) Failing to format the output to exactly two decimal places as required by the problem statement.
# ──────────────────────────────────────────────────

import math

perplexity = 170
cross_entropy = math.log2(perplexity)

print(f"{cross_entropy:.2f}")
