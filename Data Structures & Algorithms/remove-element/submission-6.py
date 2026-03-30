class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)): #traverse through nums including last index

            if nums[i] != val: #move second pointer forward
                nums[k] = nums[i]
                k += 1 # move first pointer k forward

        return k