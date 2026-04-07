class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1


        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            #sorted left array
            if nums[m] >= nums[l]:
                
                # target on right of midle
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                
                elif target < nums[m] or target > nums[r]:
                    r = m - 1

            # sorted right array
            else: # nums[m] < nums[r]

                # target is on the left side
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                
                # target is on right side
                elif target > nums[m] or target < nums[l]:
                    l = m + 1
        
        return -1


         