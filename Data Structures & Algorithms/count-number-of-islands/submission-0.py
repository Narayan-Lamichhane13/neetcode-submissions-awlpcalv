class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_count = 0 

        def dfs(i, j):
            if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0" or grid[i][j] == "2":
                return 
            
            grid[i][j] = "2"
            
            dfs(i + 1, j) # down
            dfs(i - 1, j) # up
            dfs(i, j - 1) # left
            dfs(i, j + 1) # right
            

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "0" or grid[i][j] == "2":
                    continue

                # found 1
                island_count += 1
                dfs(i, j)


                    
        
        return island_count
                
