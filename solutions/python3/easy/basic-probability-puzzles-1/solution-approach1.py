# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-1/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #1 
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:17 a.m.
# ──────────────────────────────────────────────────

from math import gcd

favorable = 0
total = 36

for d1 in range(1, 7):
    for d2 in range(1, 7):
        if d1 + d2 <= 9:
            favorable += 1

g = gcd(favorable, total)
print(f"{favorable//g}/{total//g}")
