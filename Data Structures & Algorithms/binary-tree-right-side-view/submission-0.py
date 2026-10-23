# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp_level = []
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                    temp_level.append(temp.left.val)    
        
                if temp.right:
                    queue.append(temp.right)
                    temp_level.append(temp.right.val)  
            
            if temp_level:
                ans.append(temp_level[-1])
        
        return ans