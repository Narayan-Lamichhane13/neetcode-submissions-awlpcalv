class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1


        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left sorted
            if nums[m] >= nums[l]:

                # find target
            
                # on right side
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    # on left side
                    r = m - 1

            # right sorted
            else: # nums[m] < nums[r]
                
                # on left side
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                
                else:
                    l = m + 1

        return -1
