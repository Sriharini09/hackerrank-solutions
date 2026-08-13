# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/dip-morphological-operations-erosion/problem?isFullScreen=true
# Problem     Morphological Operations: Erosion
# Difficulty  Easy
# Subdomain   Digital Image Analysis
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:39 a.m.
# Technique   sliding-window-morphological-erosion
# Time        O(R * C)
# Space       O(R * C)
# Insight     The algorithm sets a pixel to one if and only if all pixels within the 3x3 neighborhood centered at that coordinate are one in the original image.
# Interview   Before: "How would you implement morphological erosion for a binary image?" After: "I iterate through the image, excluding the boundary pixels, and check if every pixel in the 3x3 neighborhood is one. This O(R * C) approach ensures the structuring element is fully contained within the foreground."
# Pitfalls    (1) Failing to exclude the image boundaries, which causes an index out of bounds error when accessing the 3x3 neighborhood.  (2) Incorrectly assuming the structuring element origin can be placed on the image border without padding.  (3) Miscounting the final result by including pixels that were set to zero during the erosion process.
# ──────────────────────────────────────────────────

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

img = [[int(x) for x in row] for row in image]

result = [[0] * cols for _ in range(rows)]

# Erosion using 3x3 structuring element
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        all_one = True

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if img[i + di][j + dj] == 0:
                    all_one = False

        if all_one:
            result[i][j] = 1

# Count 1 pixels
count = sum(sum(row) for row in result)

print(count)
