# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/dip-morphological-operations-dilation/problem?isFullScreen=true
# Problem     Morphological Operations: Dilation
# Difficulty  Easy
# Subdomain   Digital Image Analysis
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:38 a.m.
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
