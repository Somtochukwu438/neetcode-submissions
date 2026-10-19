# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(n, m):
            if not n and not m:
                return True
            if not n or not m:
                return False
            if n.val != m.val:
                return False
            return is_same_tree(n.left, m.left) and is_same_tree(n.right, m.right)

        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            if temp.val == subRoot.val:
                if is_same_tree(temp, subRoot):
                    return True

        return False