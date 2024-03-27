# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head
        even = head.next
        evenHead = head.next
        while even and even.next:
            odd.next = even.next
            even.next = odd.next.next
            even = even.next
            odd = odd.next
        odd.next = evenHead
        return head