from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def search(x, y, empty):
            if x < 0 or x >= a or y < 0 or y >= b or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if empty == 0 else 0

            grid[x][y] = -1  # Mark as visited
            valid_paths = 0

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                valid_paths += search(x + dx, y + dy, empty - 1) # Recurive

            grid[x][y] = 0  # Reset the cell after backtracking
            return valid_paths

        a, b = len(grid), len(grid[0])
        start_x, start_y, empty_cells = 0, 0, 0

        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    empty_cells += 1
        
        return search(start_x, start_y, empty_cells + 1)