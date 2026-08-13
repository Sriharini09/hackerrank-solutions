# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/dip-image-segmentation-2/problem?isFullScreen=true
# Problem     Image Segmentation #2
# Difficulty  Easy
# Subdomain   Digital Image Analysis
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:33 a.m.
# Technique   breadth-first-search-connected-components
# Time        O(R * C)
# Space       O(R * C)
# Insight     The algorithm identifies connected components in a binary grid by performing a breadth-first search starting from each unvisited object pixel and marking all reachable 8-connected neighbors as visited.
# Interview   Before: "How would you count distinct objects in a binary image?" After: "I would use BFS or DFS to traverse each connected component. By iterating through every cell and triggering a traversal for each unvisited '1', I can count the components in O(R * C) time, where R and C are grid dimensions."
# Pitfalls    (1) Failing to include all eight directions in the neighbor search, which violates the 8-pixel connectivity requirement.  (2) Neglecting to mark the starting pixel as visited before initiating the queue, leading to redundant processing or infinite loops.  (3) Incorrectly handling grid boundaries during neighbor coordinate calculation, which causes index out of bounds errors.
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

# 8-directional connectivity
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

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
