# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(m, n):
            if not m and not n:
                return True
            if not m or not n:
                return False
            if m.val != n.val:
                return False
            return dfs(m.left, n.left) and dfs(m.right, n.right)

        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if curr.val == subRoot.val:
                if dfs(curr, subRoot):
                    return True
        return False
        