class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0" or grid[i][j] == "2":
                return
            
            grid[i][j] = "2"

            dfs(i + 1, j) # down
            dfs(i - 1, j) # up
            dfs(i, j + 1) # right
            dfs(i, j - 1) # left


        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "0" or grid[i][j] == "2":
                    continue
                
                dfs(i, j)
                island_count += 1
        
        return island_count



        