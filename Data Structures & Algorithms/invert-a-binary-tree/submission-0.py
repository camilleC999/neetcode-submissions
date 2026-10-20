# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Everything on the left needs to go on the right. 
BFS or DFS?
    - I'm thinking BFS since we basically want to reverse the rows so that they're backwarks
A.) BFS approach
    -regular imlementation
    -want to have a temp variable to hold a node while we switch
    -set temp = right, root.right = root.left, root.left = temp
    -add to queue left to right bc it'll be in the correct positon by that time
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    temp = cur.right
                    cur.right = cur.left
                    cur.left = temp
                    queue.append(cur.left)
                    queue.append(cur.right)

        return root

        