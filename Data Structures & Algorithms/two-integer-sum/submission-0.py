class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {} #num value : index
        
        for index, num in enumerate(nums):
            if target - num in sum_dict:
                sum_list = [sum_dict[target-num], index]
                return sum_list

            else: 
                sum_dict[num] = index 

        return []