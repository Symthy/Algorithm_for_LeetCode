class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        root = ListNode(head.val)
        root.next = resolve(head.next, head.val)

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