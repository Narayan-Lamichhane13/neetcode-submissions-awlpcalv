class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # given integer array nums of len = n
        # make a new array ans of len * 2
        # ans[i] will be same as nums[i]
        # ans[i + len(nums)] = nums[i]

        # nums[1,4,1,2]
        # ans[1,4,1,2,1,4,1,2]

        ans = nums + nums

        return ans