# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_ancestor):
            if not root:
                return 0

            if root.val >= max_ancestor:
                res = 1
            else:
                res = 0
                
            max_ancestor = max(max_ancestor, root.val)

            left = dfs(root.left, max_ancestor)
            right = dfs(root.right, max_ancestor)

            return res + left + right

        return dfs(root, root.val)

            
            