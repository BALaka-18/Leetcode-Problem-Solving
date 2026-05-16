# Leetcode 200: Number of Islands
# DFS/BFS

'''
Example:
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
ans = 3
'''

import collections

def numIslands(grid: List[List[str]]) -> int:
        if grid is []:
            return 0

        m, n = len(grid), len(grid[0])

        '''
        def bfs(i, j):
            queue = collections.deque()
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            
            queue.append((i, j))
            grid[i][j] = "0"    # Mark as visited

            while queue:
                r, c = queue.popleft()
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    print(nr, nc)
                    if (nr >= 0 and nr < m) and (nc >= 0 and nc < n) and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"

        '''

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "0"    # Mark as visited
            dfs(i, j+1) # Right
            dfs(i, j-1) # Left
            dfs(i-1, j) # Up
            dfs(i+1, j) # Down


        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands