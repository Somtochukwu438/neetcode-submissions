# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        cur = head
        while cur.next != None:
            lst.append(cur)
            cur = cur.next

        lst.append(cur)

        dummy = ListNode()
        d = dummy
        l, r = 0, len(lst) - 1
        while l < r:
            dummy.next = lst[l]
            dummy = dummy.next
            l += 1

            dummy.next = lst[r]
            dummy = dummy.next
            r -= 1
        
        if len(lst) % 2 == 1:
            dummy.next = lst[l]
            dummy = dummy.next

        dummy.next = None
        
        for i in range(len(lst)):
            print(d.next.val)
            d = d.next
        
