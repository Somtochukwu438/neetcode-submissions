# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        queue = deque([root])
        levels = []
        while queue:
            curr = queue.popleft()
            levels.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        s = sorted(levels, reverse = False)
        return s[k-1]
        # heap = []
        # for i in levels:
        #     heapq.heappush(heap, -i)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # final = heap[0]
        # return abs(final)
        