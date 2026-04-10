class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #           0  1 2 3
        # heights = [1,2,3,4]

        # Area : width/(r - l) * min(heights[r], heights[l])

        l, r = 0, len(heights) - 1

        max_area = 0

        while l < r:    
            max_area = max(max_area, (r-l) * min(heights[r], heights[l]))

            if heights[r] > heights[l]:
                l += 1
            else: # l > r or l == r 
                r -= 1
            
        
        return max_area
            