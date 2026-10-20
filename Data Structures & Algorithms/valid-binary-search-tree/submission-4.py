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
        def dfs(root, left_max, right_min):
            if not root:
                return True

            if not (left_max < root.val < right_min):
                return False

            return dfs(root.left, left_max, root.val) and dfs(root.right, root.val, right_min)

        return dfs(root, float('-inf'), float('inf'))



        