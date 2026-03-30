class Solution:
    def removeElement(self, nums, val):
        k = 0 

        for i in range(len(nums)): #iterate through list
            if nums[i] != val: # if nums != 2, non val number
                nums[k] = nums[i] #slide index i non val number to position k which is val number
                k += 1 # k will be 1 ahead of i at the end of each iteration
        
        return k