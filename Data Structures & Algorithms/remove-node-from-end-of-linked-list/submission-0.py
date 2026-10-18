# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        lis.pop(-n)
        if not lis:
            return None
        dummy = ListNode(lis[0])
        current = dummy
        for x in range(1, len(lis)):
            current.next = ListNode(lis[x])
            current = current.next
        return dummy

        