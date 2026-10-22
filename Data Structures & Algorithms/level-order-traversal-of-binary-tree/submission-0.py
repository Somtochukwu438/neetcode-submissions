# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        ans.append([root.val])
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    temp.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    temp.append(node.right.val)
                    queue.append(node.right)
            if temp:
                ans.append(temp)
        return ans

            
        