# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
immediately, I'm like evaluate the parent and the kids first
    - if kids violate, return False
    - if we get to the leaves and we've never hit false, so return true
bfs would involve going to the queue and validating that every value in the queue is
ascending

i haven't implemented bfs in a second so let me do that

I'm thinking about the min of the right sub tree, has to be greater than the max of the left subtree
DFS:
    - 
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #(true or false, min, max)
        def dfs(root):
            if not root:
                return True, None, None

            if not root.left and not root.right:
                return True, root.val, root.val

            cur = True

            left = dfs(root.left)
            right = dfs(root.right)

            if not left[0] or not right[0]:
                return False, None, None

            if left[2]:
                cur = cur and left[2] < root.val
            if right[1]:
                cur = cur and root.val < right[1]

            return (cur, left[1] or root.val, right[2] or root.val)

        return dfs(root)[0]



        