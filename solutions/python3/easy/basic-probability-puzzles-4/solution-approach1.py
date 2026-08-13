# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-4/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #4
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:26 a.m.
# Technique   combinatorial-probability-summation
# Time        O(1)
# Space       O(1)
# Insight     The total probability is calculated by summing the mutually exclusive events of drawing a red ball from the first bag and two black balls from the second, or a black ball from the first and one red and one black from the second.
# Interview   Before: "How would you calculate the probability of a combined event across two independent bags?" After: "I partition the problem into disjoint cases based on the first draw, then use combinations to find the probability of each outcome in O(1) time."
# Pitfalls    (1) Failing to account for both mutually exclusive scenarios where the red ball originates from either the first or the second bag.  (2) Incorrectly applying the combination formula by using permutations instead of combinations for drawing balls from the second bag.
# ──────────────────────────────────────────────────

from fractions import Fraction
from math import comb

# Bag 1
r1, b1 = 4, 5

# Bag 2
r2, b2 = 3, 7

# Case 1: Red from Bag1, Black+Black from Bag2
p1 = Fraction(r1, r1 + b1) * Fraction(comb(b2, 2), comb(r2 + b2, 2))

# Case 2: Black from Bag1, Red+Black from Bag2
p2 = Fraction(b1, r1 + b1) * Fraction(comb(r2, 1) * comb(b2, 1), comb(r2 + b2, 2))

ans = p1 + p2
print(f"{ans.numerator}/{ans.denominator}")
