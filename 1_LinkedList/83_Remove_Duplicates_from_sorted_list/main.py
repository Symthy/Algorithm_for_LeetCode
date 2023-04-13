# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def resolve(head: Optional[ListNode], beforeNum: int) -> Optional[ListNode]:
            if head is None:
                return head
            nextNode: ListNode = head
            curNum = nextNode.val
            while curNum != beforeNum:
                if not hasattr(nextNode, "next"):
                    break
                nextNode = nextNode.next
            curNum = nextNode.val
            newNode = ListNode(curNum)
            newNode.next = resolve(nextNode.next, head.val)
            return newNode

        if head is None or head.next is None:
            return head
        root = ListNode(head.val)
        root.next = resolve(head.next, head.val)


class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        current = head.next
        before = head
        while current != None:
            if before.val == current.val:
                before.next = current.next
                current = current.next
                continue
            before = current
            current = current.next
        return head
