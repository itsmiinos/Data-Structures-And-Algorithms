# Last updated: 8/13/2025, 8:16:22 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None

        if head is None or head.next is None : 
            return None

        while fast is not None and fast.next is not None : 
            fast = fast.next.next
            prev = slow
            slow = slow.next
       
        prev.next = slow.next

        return head