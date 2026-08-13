# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true
# Problem     Basic Statistics Warmup
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:02 a.m.
# Technique   frequency-map-and-sorting
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation calculates descriptive statistics by sorting the array for the median and using a frequency map to identify the smallest mode among those with the highest occurrence count.
# Interview   Before: "How would you calculate the mode if multiple values share the same frequency?" After: "I would use a hash map to track frequencies, then select the minimum key among those with the maximum frequency, resulting in O(N) time for the mode and O(N log N) overall due to sorting."
# Pitfalls    (1) Failing to use the numerically smallest integer when multiple modes exist as required by the problem statement.  (2) Incorrectly calculating the population standard deviation by using N-1 instead of N as specified in the formula.  (3) Rounding errors when formatting output to one decimal place instead of using the required 0.0 format.
# ──────────────────────────────────────────────────

import math
from collections import Counter

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Mean
mean = sum(arr) / n

# Median
arr_sorted = sorted(arr)
if n % 2 == 1:
    median = float(arr_sorted[n // 2])
else:
    median = (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2

# Mode
freq = Counter(arr)
max_freq = max(freq.values())
mode = min(k for k, v in freq.items() if v == max_freq)

# Standard Deviation (Population SD)
variance = sum((x - mean) ** 2 for x in arr) / n
sd = math.sqrt(variance)

# 95% Confidence Interval
margin = 1.96 * (sd / math.sqrt(n))
lower = mean - margin
upper = mean + margin

# Output
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
print(f"{sd:.1f}")
print(f"{lower:.1f} {upper:.1f}")
