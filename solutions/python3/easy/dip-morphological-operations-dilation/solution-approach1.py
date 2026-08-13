# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/dip-morphological-operations-dilation/problem?isFullScreen=true
# Problem     Morphological Operations: Dilation
# Difficulty  Easy
# Subdomain   Digital Image Analysis
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:38 a.m.
# Technique   3x3-structuring-element-dilation
# Time        O(R * C)
# Space       O(R * C)
# Insight     The algorithm performs morphological dilation by setting a pixel in the output grid to one if any pixel within its 3x3 neighborhood in the input grid is one.
# Interview   Before: "How would you implement morphological dilation for a binary image?" After: "I iterate through each pixel, and if it is one, I mark its 3x3 neighborhood in a new grid as one. This O(R*C) approach correctly handles boundary conditions by checking index bounds before updating the result."
# Pitfalls    (1) Failing to check boundary conditions when applying the 3x3 structuring element, which causes index out of bounds errors.  (2) Updating the original image matrix during iteration instead of using a separate result matrix, which leads to incorrect dilation propagation.  (3) Misinterpreting the origin of the structuring element, which shifts the dilated output incorrectly.
# ──────────────────────────────────────────────────

# Read the binary image
image = [
    "0000000000",
    "0111111100",
    "0000111100",
    "0000111100",
    "0001111100",
    "0000111100",
    "0001100000",
    "0000000000",
    "0000000000"
]

rows = len(image)
cols = len(image[0])

# Convert to integer matrix
img = [[int(x) for x in row] for row in image]

# 3x3 structuring element with origin at center
result = [[0] * cols for _ in range(rows)]

# Dilation
for i in range(rows):
    for j in range(cols):
        if img[i][j] == 1:
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        result[ni][nj] = 1

# Count 1 pixels
count = sum(sum(row) for row in result)

print(count)
