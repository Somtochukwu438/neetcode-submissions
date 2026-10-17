# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        lis1 = []
        lis2 = []
        merge = []
        p1 = list1
        p2 = list2

        while p1:
            lis1.append(p1.val)
            p1 = p1.next
        while p2:
            lis2.append(p2.val)
            p2 = p2.next
        x1 = 0
        x2 = 0
        while x1 < len(lis1) and x2 < len(lis2):
            if lis1[x1] <= lis2[x2]:
                merge.append(lis1[x1])
                x1 += 1
            else:
                merge.append(lis2[x2])
                x2 += 1
        merge.extend(lis1[x1:])
        merge.extend(lis2[x2:])

        dummy = ListNode(merge[0])
        current = dummy
        for i in range(1, len(merge)):
            current.next = ListNode(merge[i])
            current = current.next
        return dummy
        




        
        