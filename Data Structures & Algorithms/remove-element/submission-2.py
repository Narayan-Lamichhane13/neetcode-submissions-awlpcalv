class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Array of integers called nums
        # Integer called val
        # Remove all "val" from "nums"

        k = 0 

        for i in range(len(nums)): #iterate through entire array

            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

        
