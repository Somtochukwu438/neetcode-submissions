# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lis = []
        curr = head
        while curr:
            lis.append(curr)
            curr = curr.next
        
        dummy = ListNode()
        current = dummy
        l = 0 
        r = len(lis) - 1
        while l <= r:
            if l == r:
                current.next = lis[l]
                current = current.next
                break
            current.next = lis[l]
            current = current.next
            l += 1

            current.next = lis[r]
            current = current.next
            r -= 1

        current.next = None
