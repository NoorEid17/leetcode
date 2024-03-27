# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next.next
        if fast is None:
            return head.val + head.next.val
        stack = []
        while fast:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        stack.append(slow.val)
        slow = slow.next
        # reached the middle now calculate the max twin sum
        max_sum = 0
        while slow:
            max_sum = max(max_sum, stack.pop() + slow.val)
            slow = slow.next
        return max_sum