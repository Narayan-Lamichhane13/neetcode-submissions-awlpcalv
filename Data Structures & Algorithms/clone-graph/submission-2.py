"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        pair_map = {}

        def dfs(node):

            if not node:
                return None

            # base case
            if node in pair_map:
                return pair_map[node]

            new_node = Node(node.val) # old_1 new_1
            pair_map[node] = new_node
            # org_2 : [new_2]

            # if node.neighbors == []
            #if node.neighbors == []:
                #return node

            for n in node.neighbors:
                new_node.neighbors.append(dfs(n)) # 1 -> 2  copy_2

            
            return new_node


        return dfs(node)
    

