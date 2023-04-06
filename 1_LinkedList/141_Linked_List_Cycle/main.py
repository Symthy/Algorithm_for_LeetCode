# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head.next
        fast = head.next.next
        while slow is not None and fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        if head == None:
            return False
        node = head
        while True:
            if node in nodes:
                return True
            nodes.add(node)
            if node.next == None:
                break
            node = node.next
        return False
