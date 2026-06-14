class Solution:
    def isValid(self, s: str) -> bool:
        # s = ([]) 

        # order in which its closed
        # each bracket has to be open AND closed by its pair bracket


        s_dict = {")" : "(", "]": "[", "}" : "{"}
        stack = []

        for char in s:

            if char in s_dict:
                if stack and stack[-1] == s_dict[char]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)

        # stack : 
        
        # [()][ stack: [

        return True if not stack else False