# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        if not root:
            return 0
        level = []
        depth = 0
        while queue:
            result = []
            for l in range(len(queue)):
                curr = queue.popleft()
                result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level.append(result)
            depth += 1
        return len(level)
