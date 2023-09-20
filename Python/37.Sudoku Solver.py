def solveSudoku(board):
    def is_valid(num, row, col):
        # Check if 'num' is valid in the current row, column, and subgrid
        for i in range(9):
            if board[i][col] == num or board[row][i] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True
    
    def backtrack(row, col):
        if row == 9:
            return True  # Reached the end, Sudoku is solved
        
        if col == 9:
            return backtrack(row + 1, 0)  # Move to the next row
        
        if board[row][col] != ".":
            return backtrack(row, col + 1)  # Skip filled cells
        
        for num in map(str, range(1, 10)):
            if is_valid(num, row, col):
                board[row][col] = num  # Place the valid number
                
                if backtrack(row, col + 1):
                    return True  # If Sudoku is solved, return True
                
                board[row][col] = "."  # If Sudoku is not solved, backtrack
        
        return False
    
    backtrack(0, 0)

# Example usage:
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solveSudoku(board)

for row in board:
    print(row)
