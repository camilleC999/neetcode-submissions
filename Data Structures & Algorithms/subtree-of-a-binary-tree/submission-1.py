# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(twin, twin2):
            if not twin and not twin2:
                return True

            if twin and twin2 and twin.val == twin2.val:
                left = isSameTree(twin.left, twin2.left)
                right = isSameTree(twin.right, twin2.right)

                return left and right
            else:
                return False

        def dfs(root):
            nonlocal subRoot
            if not root or root is False:
                return False

            status = dfs(root.left) or dfs(root.right)

            if root.val == subRoot.val:
                status = status or isSameTree(root, subRoot)

            return status  



        return dfs(root)

            
        