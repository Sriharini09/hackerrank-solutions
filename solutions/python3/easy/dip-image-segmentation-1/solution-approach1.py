# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/dip-image-segmentation-1/problem?isFullScreen=true
# Problem     Image Segmentation #1
# Difficulty  Easy
# Subdomain   Digital Image Analysis
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:30 a.m.
# ──────────────────────────────────────────────────

from collections import deque

grid = [
    "000110001010",
    "111011110001",
    "111010010010",
    "100000000100"
]

rows = len(grid)
cols = len(grid[0])

visited = [[False] * cols for _ in range(rows)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '1' and not visited[i][j]:
            count += 1
            q = deque([(i, j)])
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and
                        0 <= ny < cols and
                        not visited[nx][ny] and
                        grid[nx][ny] == '1'):
                        visited[nx][ny] = True
                        q.append((nx, ny))

print(count)
