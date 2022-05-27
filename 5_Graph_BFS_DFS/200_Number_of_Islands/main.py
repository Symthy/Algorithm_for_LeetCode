from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                count = count + self.dfs_masking(grid, row, col)
        return count
            
    def dfs_masking(self, grid: List[List[str]], row: int, col: int) -> int: 
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == '0': 
            return 0
        grid[row][col] = '0'
        self.dfs_masking(grid, row + 1, col)
        self.dfs_masking(grid, row, col + 1)
        self.dfs_masking(grid, row - 1, col)
        self.dfs_masking(grid, row, col - 1)
        return 1