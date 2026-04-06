class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        org_pixel = image[sr][sc]
        

        def dfs(r, c):
            # out of bounds
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return 
            
            # base case 
            if image[r][c] != org_pixel:
                return
            
            # changed the pixel to new color
            image[r][c] = color

            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right



        dfs(sr, sc)

        return image