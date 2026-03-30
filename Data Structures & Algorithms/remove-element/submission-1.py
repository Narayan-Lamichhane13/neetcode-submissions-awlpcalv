class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Array of integers called nums
        # Integer called val
        # Remove all "val" from "nums"

        for i in range(len(nums) + 1):
            if val in nums:
                nums.remove(val)
        
        return len(nums)
