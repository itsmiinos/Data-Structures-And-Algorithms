# Last updated: 8/13/2025, 8:20:04 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None : 
            return head

        second_head = head.next
        first = head
        second = second_head

        if second.next is None : 
            return head

        while second is not None and second.next is not None : 
            second_next = second.next
            first.next = second_next
            first = first.next
            first_next = first.next
            second.next = first_next
            second = second.next
        
        # second.next = None
        first.next = second_head

        return head
        