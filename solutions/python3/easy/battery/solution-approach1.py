# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/battery/problem?isFullScreen=true
# Problem     Laptop Battery Life
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:00 a.m.
# Technique   linear-regression-threshold-clipping
# Time        O(1)
# Space       O(1)
# Insight     The model assumes a linear relationship between charging time and battery life up to a saturation point of four hours, after which the battery life remains constant at eight hours.
# Interview   Before: "How would you model the relationship between charging time and battery life?" After: "I observed the training data saturates at 4.0 hours, so I implemented a piecewise linear function with O(1) complexity to handle the saturation point and linear growth."
# Pitfalls    (1) Failing to account for the saturation point at 4.0 hours leads to overestimating battery life for long charge times.  (2) Ignoring the requirement to format the output to exactly two decimal places results in precision errors.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    timeCharged = float(input().strip())

    if timeCharged >= 4.0:
        print("8.00")
    else:
        print(f"{2 * timeCharged:.2f}")
