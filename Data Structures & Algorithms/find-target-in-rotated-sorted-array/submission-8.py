class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r: 

            m = (l + r) // 2

            if nums[m] == target:
                return m


            # if left side is sorted
            if nums[l] <= nums[m]: 
                
                # if on right side
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                
                # if on left side
                elif target < nums[m] or target > nums[r]:
                    r = m - 1
            
            else: # nums[r] >= nums[m], right side is sorted

                # if on left side
                if target < nums[m] or target > nums[r]:
                    r = r - 1
                
                # if on right side
                elif target > nums[m] or target < nums[l]:
                    l = l + 1

        return -1
                



