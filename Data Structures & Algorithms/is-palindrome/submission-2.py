class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlpha(s[l]):
                l += 1
            while l < r and not self.isAlpha(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True

    
    def isAlpha(self, c: str) -> bool:

        if ord('A') <= ord(c) <= ord('Z'):
            return True
        elif ord('a') <= ord(c) <= ord('z'):
            return True
        elif ord('0') <= ord(c) <= ord('9'):
            return True
        
        return False
        
       