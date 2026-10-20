# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def bfs(root):
            queue = deque()
            if root:
                queue.append(root)

            level = 0
            while queue:
                print("level: ", level)
                self.res.append([])
                for i in range(len(queue)):
                    cur = queue.popleft()
                    self.res[level].append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)

                level += 1
        bfs(root)
        return self.res
                    