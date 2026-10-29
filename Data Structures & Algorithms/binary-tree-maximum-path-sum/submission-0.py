# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        level = []

        while queue:
            curr = queue.popleft()
            level.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        gain = {}
        res = float('-inf')
        for node in reversed(level):
            left = max(0, gain.get(node.left, 0))
            right = max(0, gain.get(node.right, 0))

            res = max(res, node.val+left+right)
            gain[node] = node.val + max(left, right)
        return res        