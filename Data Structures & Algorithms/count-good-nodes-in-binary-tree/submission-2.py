# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        good_nodes = 0
        queue = deque([(root, root.val)])
        while queue:
            for i in range(len(queue)):
                curr, ma = queue.popleft()
                if curr.val >= ma:
                    good_nodes += 1
                ma = max(ma, curr.val)
                if curr.left:
                    queue.append((curr.left, ma))
                if curr.right:
                    queue.append((curr.right, ma))
        return good_nodes
        
            


        