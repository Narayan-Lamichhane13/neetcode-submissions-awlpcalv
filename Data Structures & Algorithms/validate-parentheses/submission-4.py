class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False

        bracket_map = {

            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = [] # ( [

        for i in range(len(s)):

            # if we get closed 
            # key
            if s[i] in bracket_map:
                if stack and stack[-1] == bracket_map[s[i]]:
                    stack.pop() #remove the top pair bracket
                else:
                    return False
            else: # if we get a open bracket
                stack.append(s[i])
        
        # stack[] empty or full
        # return if is not 0/empty : NOT FALSE
        return False if stack else True  



