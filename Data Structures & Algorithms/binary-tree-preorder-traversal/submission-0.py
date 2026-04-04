# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # all the way left while including values into list
        # stack [1]  
        # stack [2,1]
        # [2,1] -- while adding to list 
        # found null, pop
        # [2,1]
        # go right, add to list
        
        output = []
        stack = []

        
        curr = root
        

        while stack or curr:
            while curr:
                output.append(curr.val)
                # output = [1,2,4,5, 3, 6]
                if curr.right:
                    stack.append(curr.right)
                # stack = []

                curr = curr.left 
            
            if stack:
                curr = stack.pop()
            # curr = 3
            # stack = []

        return output



















        # while stack or curr:
            
        #     stack.append(curr)
        #     output.append(curr.val)

        #     while curr.left:
        #         curr = curr.left
        #         stack.append(curr.right)
        #         output.append(curr.val)
        #     curr = stack.pop()

        #     if curr.right:
        #         curr = curr.right
        #         stack.pop()
        
        # return output
        
        # stack[1]
        # output[1,2,4,5,3,6,7]
        # curr = 7


            



                
                
            





