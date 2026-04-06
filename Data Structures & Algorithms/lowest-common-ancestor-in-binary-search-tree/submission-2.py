# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # how to find p and q
        # dfs left and right until we find p and q

        # keep track of the ancestors 
        
        def dfs(node):
            if not node: 
                return node

            elif node.val > p.val and node.val > q.val:
                return dfs(node.left) # the dfs will go to the right node, but never return it back up

            elif node.val < p.val and node.val < q.val:
                return dfs(node.right)
            
            else:
                return node
            


        return dfs(root)




