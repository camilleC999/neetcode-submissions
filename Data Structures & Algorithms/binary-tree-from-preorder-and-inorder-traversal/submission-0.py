# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        
        root = preorder[0]
        root_idx = inorder.index(root)

        #define left and right subtrees for inorder
        left_in = inorder[:root_idx]
        right_in = inorder[root_idx + 1:]

        #define left and right preorder
        left_pre = preorder[1: len(left_in) + 1]
        right_pre = preorder[len(left_in) + 1: ]
        
        cur = TreeNode(root)
        cur.left = self.buildTree(left_pre, left_in)
        cur.right = self.buildTree(right_pre, right_in)

        return cur


