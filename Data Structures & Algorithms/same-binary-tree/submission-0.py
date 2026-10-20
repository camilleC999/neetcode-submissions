# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pec = deque([p])
        rec = deque([q])
        
        while pec and rec:
            if len(pec) != len(rec):
                return False

            for i in range(len(pec)):
                twin1 = pec.popleft()
                twin2 = rec.popleft()

                if twin1 and twin2:
                    if twin1.val == twin2.val:
                        pec.extend([twin1.left, twin1.right])
                        rec.extend([twin2.left, twin2.right])
                    else:
                        return False
                elif twin1 or twin2:
                    return False

        return True


