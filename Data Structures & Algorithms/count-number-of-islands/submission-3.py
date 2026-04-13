class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # constraints 
        # if its 0: skip
        # if its out of bounds

        # to traverse use DFS
        # if 0 stop that direction 
        # if its out of bounds stop doing dfs in that direction

        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):

            if ( r < 0 or c < 0 or # left and up
                 c >= COLS or r >= ROWS or # right and down 
                 grid[r][c] == "0" or 
                 grid[r][c] == "2" # visited islands
                ):
                return 
        
            grid[r][c] = "2"
            
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right
        

        for r in range(ROWS): # rows
            for c in range(COLS):
                
                if ( grid[r][c] == "0" or 
                     r < 0 or c < 0 or # left and up
                     c >= COLS or r >= ROWS or # right and down 
                     grid[r][c] == "2"
                ):
                    continue  # if boundries reached skip to next cell
                
                count += 1
                dfs(r, c)
        
        return count 
                
                

