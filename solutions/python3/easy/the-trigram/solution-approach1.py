# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-trigram/problem?isFullScreen=true
# Problem     The Trigram
# Difficulty  Easy
# Subdomain   Natural Language Processing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:20 a.m.
# Technique   ordered-dictionary-frequency-counting
# Time        O(N)
# Space       O(N)
# Insight     The implementation uses an OrderedDict to maintain insertion order, ensuring that the first trigram encountered is preserved when multiple trigrams share the same maximum frequency.
# Interview   Before: "How do you handle ties in frequency?" After: "By using an OrderedDict, we naturally track the first occurrence of each trigram, allowing us to return the correct result in O(N) time while respecting the sentence-boundary constraint."
# Pitfalls    (1) Failing to handle the sentence-boundary constraint by splitting the entire text by spaces instead of sentences.  (2) Incorrectly including the dot character in trigrams by failing to strip or split by the period delimiter.  (3) Overlooking the case-insensitivity requirement by failing to convert the input text to lowercase before processing.
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
