# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-trigram/problem?isFullScreen=true
# Problem     The Trigram
# Difficulty  Easy
# Subdomain   Natural Language Processing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:20 a.m.
# ──────────────────────────────────────────────────

from collections import OrderedDict
import re
import sys

text = sys.stdin.read().strip().lower()

# Split into sentences using '.'
sentences = text.split('.')

freq = OrderedDict()

for sentence in sentences:
    words = sentence.strip().split()
    for i in range(len(words) - 2):
        trigram = " ".join(words[i:i+3])
        if trigram not in freq:
            freq[trigram] = 1
        else:
            freq[trigram] += 1

max_count = 0
answer = ""

for trigram, count in freq.items():
    if count > max_count:
        max_count = count
        answer = trigram

print(answer)
