# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        stack = []
        node = head
        while True:
            stack.insert(0, node.val)
            node = node.next
            if node is None:
                break

        new_head = ListNode(stack.pop(0))
        before = new_head
        while True:
            current = ListNode(stack.pop(0), None)
            before.next = current
            if len(stack) == 0:
                break
            before = current
        return new_head