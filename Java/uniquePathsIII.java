 class Solution {
    public int uniquePathsIII(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int startX = 0, startY = 0, emptyCells = 0;

        // Find the starting point, ending point, and count empty cells
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                } else if (grid[i][j] == 0) {
                    emptyCells++;
                }
            }
        }

        return dfs(grid, startX, startY, emptyCells + 1); // +1 to account for the starting point
    }

    private int dfs(int[][] grid, int x, int y, int empty) {
        int m = grid.length;
        int n = grid[0].length;

        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == -1) {
            return 0;
        }

        if (grid[x][y] == 2) {
            return empty == 0 ? 1 : 0;
        }

        grid[x][y] = -1; // Mark the current cell as visited
        int validPaths = 0;

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] dir : directions) {
            validPaths += dfs(grid, x + dir[0], y + dir[1], empty - 1);
        }

        grid[x][y] = 0; // Reset the cell after backtracking
        return validPaths;
    }
}