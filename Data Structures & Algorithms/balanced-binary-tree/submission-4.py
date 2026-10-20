# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
This has to be dfs
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def dfs(root):
            nonlocal balance
            if not balance:
                return False

            if not root:
                return 1

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right - left) > 1:
                balance = False
            
            return max(right, left) + 1

        dfs(root)
        return balance





        