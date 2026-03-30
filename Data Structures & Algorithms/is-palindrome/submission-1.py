class Solution:
    def alphaNum(self, c):
            return c.isalnum()

    def isPalindrome(self, s: str) -> bool:
        

        l, r = 0, len(s) - 1 

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() == s[r].lower():
                l += 1 # because it could've gone through steps above
                r -= 1
                continue
            else:
                return False 
        
        return True 



        # s = "".join(ch for ch in s if ch.isalnum())
        # s.lower()

        # # case insensitive (uppercase doesn't matter)
        # # includes numbers and letters
        # # other symbols are ignored
        # p1 = len(s) - 1

        # # odd length
        # # if len(s) % 2:
        # #     return 

        # for i in range(len(s)//2):
        #     if s[i] == s[p1]:
        #         p1 -= 1
        #         continue
        #     else:
        #         return False 

        # return True

        