# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_map = defaultdict(list)

        count = 0

        def dfs(root, count):

            if not root:
                return

            count += 1

            level_map[count].append(root.val)

            dfs(root.left, count)
            dfs(root.right, count)
        
        dfs(root, count)

        output = list(level_map.values())

        return output

        