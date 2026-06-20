class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = [0, 7, 2, 5]
        #         i = 0, 1, 2, 3


       #contianer
       # min(two heights) 
       # max water 
       # maximum of the min( 2 heights ) * length (distance between the heights in the array)
    
        #brute: find all areas, find the max of that

        # Find the maxmium
        # lenght: most left and mmsot right
        # two pointer

        # height: min(6, 1) * (r-l)
        # 1 * 7

        # store value in cache 

        # find the largest height 
        # if r > l: l+=1
        # if l >= r: r-=1

        l, r = 0, len(heights) - 1
        max_cont = 0


        while l < r:
            # curr area
            area = min(heights[l], heights[r]) * (r-l)

            # compare, is our new area bigger than previous cached area?
            max_cont = max(max_cont, area)

            if heights[r] > heights[l]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1
            

        return max_cont



        






