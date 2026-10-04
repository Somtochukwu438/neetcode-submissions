# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        st = collections.deque()
        st.append(root)
        if not root:
            return None
        if not root.left and not root.right:
            return root
        while st:
            l = len(st)
            for i in range(l):
                item = st.popleft()
                if item.left:
                    st.append(item.left)
                if item.right:
                    st.append(item.right)
                item.left, item.right = item.right, item.left
        return root



        