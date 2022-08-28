# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None
        
        sum = l1.val + l2.val
        is_round_up = False
        if sum >= 10:
            is_round_up = True
            sum = sum - 10
        
        new_node = ListNode(sum)
        buildSumLinkedList(l1.next, l2.next, new_node, is_round_up)
        return new_node
        
        
def buildSumLinkedList(l1: Optional[ListNode], l2: Optional[ListNode], before_node: ListNode, is_round_up = False):
    if l1 is None and l2 is None:
        if is_round_up is True:
            before_node.next = ListNode(1)     
        return
    
    l1_val = 0
    l2_val = 0
    l1_next = None
    l2_next = None
    if l1 is not None:
        l1_val = l1.val
        l1_next = l1.next
    if l2 is not None:
        l2_val = l2.val
        l2_next = l2.next
    
    sum = l1_val + l2_val
    is_next_round_up = False
    if is_round_up is True:
        sum = sum + 1
    if sum >= 10:
        is_next_round_up = True
        sum = sum - 10  
    
    new_node = ListNode(sum)
    before_node.next = new_node
    
    buildSumLinkedList(l1_next, l2_next, new_node, is_next_round_up)
    return