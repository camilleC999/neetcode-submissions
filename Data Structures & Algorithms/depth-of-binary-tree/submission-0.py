# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
BFS or DFS, 
    - I think BFS bc we literally just counting levels
A.) BFS Approach
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        count = 0
        while q:
            count += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

        return count - 1