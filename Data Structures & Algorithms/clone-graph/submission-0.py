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

        # make copy of one 
        def dfs(node): # node 1

            if not node:
                return None

            if node in pair_map:
                return pair_map[node]
 
            new_node = Node(node.val)
            pair_map[node] = new_node # old node : new node

            # keep track of neighbors
            # deep copy neighbors from input graph --> new graph
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n)) # self.neighbor = [new_neighbors, new_nieghbor2]

            return new_node


        return dfs(node)
