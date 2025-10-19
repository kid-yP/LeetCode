# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        prev = None
        current = head
        pos = 1

        while pos < left:
            prev = current
            current = current.next
            pos += 1

        tail = current
        prev_sub = None
        while pos <= right:
            next_node = current.next
            current.next = prev_sub
            prev_sub = current
            current = next_node
            pos += 1

        if prev:
            prev.next = prev_sub
        else:
            head = prev_sub

        tail.next = current
        return head