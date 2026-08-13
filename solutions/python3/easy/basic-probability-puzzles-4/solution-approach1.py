# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-4/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #4
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:26 a.m.
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
