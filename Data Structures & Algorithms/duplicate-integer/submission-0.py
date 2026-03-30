class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        duplicate_list = []

        for num in nums:
            if num in duplicate_list:
                return True
            
            duplicate_list.append(num)
        
        return False
