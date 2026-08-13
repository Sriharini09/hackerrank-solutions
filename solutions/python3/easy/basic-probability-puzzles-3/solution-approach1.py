# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-3/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #3
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:21 a.m.
# Technique   probabilistic-case-summation
# Time        O(1)
# Space       O(1)
# Insight     The total probability of drawing exactly two red balls and one black ball is the sum of the probabilities of the three mutually exclusive scenarios where exactly one urn yields a black ball.
# Interview   Before: "How would you calculate the probability of a specific combination of independent events?" After: "I sum the probabilities of all disjoint outcomes that satisfy the condition. Here, it is O(1) time to compute the three cases: (B,R,R), (R,B,R), and (R,R,B)."
# Pitfalls    (1) Failing to account for all three mutually exclusive permutations of the two red and one black ball outcome.  (2) Incorrectly calculating the total number of balls in each urn, leading to wrong denominators for the individual fractions.
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
