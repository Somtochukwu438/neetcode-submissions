# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        lis = lis[::-1]

        dummy = ListNode(lis[0])
        curri = dummy
        for i in range(1, len(lis)):
            curri.next = ListNode(lis[i])
            curri = curri.next
        return dummy
