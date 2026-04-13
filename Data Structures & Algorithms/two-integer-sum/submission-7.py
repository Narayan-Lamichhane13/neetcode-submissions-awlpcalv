class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        
        result = []

        hash_map = defaultdict(int)

        for index, num in enumerate(nums):

            if target - num in hash_map:
                return [hash_map[target - num], index]
            
            hash_map[num] = index
        
        return []

