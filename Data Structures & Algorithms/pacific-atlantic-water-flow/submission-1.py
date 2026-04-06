class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, seen, prevHeight):
            
            # contraints
            # if we reach pacific border
            # if we reach atlantic border
            # if we reach height >= org height
            # return
            if ( (r, c) in seen or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return 
            
            seen.add( (r, c) )

            dfs(r + 1, c, seen, heights[r][c])
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])



        # top and bottom
        for c in range(COLS):
            # pacific top
            dfs(0, c, pac, heights[0][c])

            # atlantic bottom
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        

        # left and right
        for r in range(ROWS):
            # left side
            dfs(r, 0, pac, heights[r][0])

            # right side
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        
        # two sets that have all the nodes that reach the pacific or atlantic
        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append( (r, c) )
        
        return result


            

