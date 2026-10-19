# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lis1 = []
        curr1 = l1
        while curr1:
            lis1.append(curr1.val)
            curr1 = curr1.next
        lis2 = []
        curr2 = l2
        while curr2:
            lis2.append(curr2.val)
            curr2 = curr2.next
        lis1 = lis1[::-1]
        lis2 = lis2[::-1]
        str_l1 = "".join(map(str, lis1))
        str_l2 = "".join(map(str, lis2))

        sum1 = int(str_l1) + int(str_l2)
        sum2 = str(sum1)

        str_t = sum2[::-1]
        final = []

        for x in str_t:
            final.append(int(x))
        dummy = ListNode(final[0])
        current = dummy
        for i in range(1, len(final)):
            current.next = ListNode(final[i])
            current = current.next
        return dummy
