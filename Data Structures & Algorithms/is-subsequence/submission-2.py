class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #dict stores keys and values (counts)
        # two pointer compare two indexes
        
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            j += 1

        if i == len(s):
            return True

        return False

