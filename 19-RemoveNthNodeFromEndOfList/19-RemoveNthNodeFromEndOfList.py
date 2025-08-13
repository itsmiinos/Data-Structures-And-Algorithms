# Last updated: 8/13/2025, 8:24:21 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(None)
        dummyNode.next = head
        fast = dummyNode
        slow = dummyNode

        for i in range(n+1) : 
            fast = fast.next
        
        if fast is None : 
            return head.next
        
        while fast is not None : 
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head