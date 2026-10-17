# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(p):
            if not p:
                return 0
            if not p.left and not p.right:
                return 1
            return 1 + max(depth(p.left), depth(p.right))

        if not root or (not root.left and not root.right):
            return True
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)