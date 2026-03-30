class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:

        l = 0 
        char_set = set()
        longest_count = 0

        for r in range(len(s)):

            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            longest_count = max(longest_count, r - l + 1)
        
        return longest_count

