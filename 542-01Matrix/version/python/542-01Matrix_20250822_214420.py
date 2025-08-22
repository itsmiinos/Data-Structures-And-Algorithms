# Last updated: 8/22/2025, 9:44:20 PM
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)]
        q = deque()

        # Step 1: Put all 0s in queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    ans[r][c] = 0
                    q.append((r, c))

        # Step 2: BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and ans[nr][nc] == -1:
                    ans[nr][nc] = ans[r][c] + 1
                    q.append((nr, nc))

        return ans
