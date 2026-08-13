# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-3/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #3
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:21 a.m.
# ──────────────────────────────────────────────────

from fractions import Fraction

# Urn X: 4 red, 3 black
# Urn Y: 5 red, 4 black
# Urn Z: 4 red, 4 black

# Case 1: X = Black, Y = Red, Z = Red
p1 = Fraction(3, 7) * Fraction(5, 9) * Fraction(4, 8)

# Case 2: X = Red, Y = Black, Z = Red
p2 = Fraction(4, 7) * Fraction(4, 9) * Fraction(4, 8)

# Case 3: X = Red, Y = Red, Z = Black
p3 = Fraction(4, 7) * Fraction(5, 9) * Fraction(4, 8)

ans = p1 + p2 + p3

print(f"{ans.numerator}/{ans.denominator}")
