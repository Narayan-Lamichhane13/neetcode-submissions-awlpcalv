class Solution:
    def isValid(self, s: str) -> bool:
        # () {} []

        # understand wht the pairs are
        # understand when we switch from open to closed brackets
        # scan the closed brackets to see if there are the same number of brackets
        # edge case: if we start with an open, it is not valid

        # use dictionary to teach the program what is the correcct pairs
        # use a stack to keep track of order and correctly conencted pairs
        #    in the stack if we have a ( and we have 2 {, then the next one should
        #    be a ) closed for the first bracket 

        # after pairs are met we remove, since we remove from top of the stack,
        # we use stack data structure

        open_close = {

            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        stack = []

        for char in s:
            if char in open_close:
                if stack and stack[-1] == open_close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False




