# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # - inf < root < inf
        # - inf < 1 < old root
        # old root < root < inf 

        def dfs(root, left_b, right_b ):
            
            # base case when the branch is valid 
            if not root:
                return True 

            # base when its false
            if not (root.val < right_b and root.val > left_b):
                return False
            
            # left 
            return ( dfs(root.left, left_b, root.val) and #  - inf < 1 < 2
                     dfs(root.right, root.val, right_b) ) # 2 < 3 < inf
        

        return dfs(root, float("-inf"), float("inf"))
