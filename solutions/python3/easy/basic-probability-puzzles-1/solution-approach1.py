# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-1/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #1 
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:17 a.m.
# Technique   brute-force-nested-loops
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through all possible outcomes of two six-sided dice to count pairs whose sum is at most nine, then reduces the resulting fraction using the greatest common divisor.
# Interview   Before: "How would you calculate the probability of a sum constraint for two dice?" After: "I iterate through all 36 possible outcomes in O(1) time, count the favorable cases where the sum is at most 9, and simplify the fraction using the GCD."
# Pitfalls    (1) Failing to account for the total sample space of 36 outcomes when calculating the probability.  (2) Forgetting to reduce the fraction to its irreducible form as required by the problem statement.  (3) Incorrectly setting the loop range, which must cover all values from 1 to 6 inclusive for both dice.
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
