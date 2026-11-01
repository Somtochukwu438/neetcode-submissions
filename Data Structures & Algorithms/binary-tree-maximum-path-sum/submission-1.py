# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        levels = []
        while queue:
            curr = queue.popleft()
            levels.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        gains = {}
        res = float('-inf')

        for node in reversed(levels):
            left = max(0, gains.get(node.left, 0))
            right = max(0, gains.get(node.right, 0))

            res = max(res, node.val + left + right)
            gains[node] = node.val + max(left, right)
        return res
        
        