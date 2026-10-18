# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        num_nodes = 0
        curr = head
        while curr:
            num_nodes += 1
            curr = curr.next
        if num_nodes == n:
            return head.next
        current = head
        diff = num_nodes - n
        for i in range(diff):
            if i == diff-1:
                current.next = current.next.next
                break
            else:
                current = current.next
        return head
            


        