# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(root):
            nonlocal arr
            if not root:
                return

            (left := dfs(root.left)) and arr.append(left)
            arr.append(root.val)
            (right := dfs(root.right)) and arr.append(right)

            return

        dfs(root)
        return arr[k - 1]
        