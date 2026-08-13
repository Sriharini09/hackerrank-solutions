# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-2/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #2
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:18 a.m.
# ──────────────────────────────────────────────────

from math import gcd

fav = 0
total = 36

for d1 in range(1, 7):
    for d2 in range(1, 7):
        if d1 != d2 and d1 + d2 == 6:
            fav += 1

g = gcd(fav, total)
print(f"{fav//g}/{total//g}")
