class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        # if, return true
        # the values in the index == each other
        # abs(i - j) <= k
        
        # else, return false

        window = set()

        l = 0

        for r in range(len(nums)):
            if abs(r - l) > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            
            window.add(nums[r])
        
        return False 
