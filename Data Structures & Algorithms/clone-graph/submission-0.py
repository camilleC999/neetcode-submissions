"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        stack = {}

        def dfs(node, stack):
            if node.val in stack.keys():
                return stack[node.val]

            newNode = Node(node.val)
            stack[newNode.val] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor, stack))

            return newNode

        return node if not node else dfs(node, stack)
            
        
        