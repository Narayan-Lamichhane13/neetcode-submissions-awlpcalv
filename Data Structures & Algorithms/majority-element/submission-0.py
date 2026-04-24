class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # 6/2 = 3 
        # 5/2 = 2.5 -> round down 2 

        # hash map = { 2 : 3    }
        # max count = 2
        # max count < 3 
        # res = 2
        # max count = 3


        count_map = defaultdict(int)
        res = max_count = 0
        
        for num in nums:

            count_map[num] += 1

            if max_count < count_map[num]:
                max_count = count_map[num]
                res = num
        
        return res
                
