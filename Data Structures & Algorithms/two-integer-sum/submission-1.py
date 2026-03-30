class Solution:
    def twoSum(self, nums:int, target:int) -> int:

        sum_map = {}

        for index, value in enumerate(nums):

            if target - value in sum_map:
                return [sum_map[target - value], index]
            
            sum_map[value] = index

        return []