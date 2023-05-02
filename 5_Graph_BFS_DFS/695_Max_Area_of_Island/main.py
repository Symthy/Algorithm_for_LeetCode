class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area_num = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                count = self.resolve_area_by_dfs(grid, row, col)
                max_area_num = max(max_area_num, count)
        return max_area_num
    
    def resolve_area_by_dfs(self, grid, row, col, count = 0) -> int:
        if grid[row][col] == 0:
            return count
        
        grid[row][col] = 0
        count = count + 1
        if row < len(grid) - 1:
            count = self.resolve_area_by_dfs(grid, row + 1, col, count)
        if col < len(grid[row]) - 1:
            count = self.resolve_area_by_dfs(grid, row, col + 1, count)
        if row > 0:
            count = self.resolve_area_by_dfs(grid, row - 1, col, count)
        if col > 0:
            count = self.resolve_area_by_dfs(grid, row, col - 1, count)
        return count