# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        cur = head
        lis = lis[::-1]

        curri = head
        for i in range(len(lis)):
            curri.val = lis[i]
            curri = curri.next
        return cur