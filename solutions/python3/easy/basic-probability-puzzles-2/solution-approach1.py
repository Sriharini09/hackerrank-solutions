# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-2/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #2
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:18 a.m.
# Technique   brute-force-nested-loops
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through all possible outcomes of two six-sided dice to count pairs that satisfy the distinctness and sum constraints.
# Interview   Before: "How would you calculate the probability of a specific sum with two dice?" After: "I iterate through all 36 possible outcomes, filtering for the condition where dice values are distinct and sum to 6, resulting in O(1) time complexity."
# Pitfalls    (1) Failing to exclude cases where d1 equals d2 when calculating the sum of 6.  (2) Incorrectly assuming the total sample space is less than 36 for two fair dice.
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
