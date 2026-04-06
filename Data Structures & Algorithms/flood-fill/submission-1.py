class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        org_pixel = image[sr][sc]

        if org_pixel == color:
            return image
        
        def dfs(r, c):

            # check out of bounds
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return 
            
            # check if the curr iterant pixel is not org_pixel
            if image[r][c] != org_pixel:
                return
            
            image[r][c] = color

            dfs(r + 1, c) # down
            dfs(r - 1, c) # up
            dfs(r, c + 1) # right
            dfs(r, c - 1) # left

        
        dfs(sr,sc)

        return image


