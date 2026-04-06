class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # send dfs up and left, if return true we are at pacific
        # send dfs down and right, if one if true we are at atlantic
        # a cell has to return true for both of these then we'll have successfull cell

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # we dont count cells we visited before
            # 
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return

            visit.add((r,c)) # we're at a new cell

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c]) 
            dfs(r, c + 1, visit, heights[r][c]) 
            dfs(r, c - 1, visit, heights[r][c]) 

        # top and bottom
        for c in range(COLS):
            # send in first row/border of pacific on top
            # heights[r][c] is the first ROWS height, which the rest have to be greater than (inverse)
            dfs(0, c, pac, heights[0][c]) 

            # send in first border of atlantic on bottom
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        # left and right
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])
        
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r, c) in atl:
                    result.append([r,c])
        
        return result
        



