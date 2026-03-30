class Solution:
    def hasDuplicate(self, nums:int) -> bool:

        nums_map = set()

        for num in nums:
            if num in nums_map:
                return True

            nums_map.add(num)

        return False