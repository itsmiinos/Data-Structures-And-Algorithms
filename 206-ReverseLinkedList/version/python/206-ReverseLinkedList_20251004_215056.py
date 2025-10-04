# Last updated: 10/4/2025, 9:50:56 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None : 
            currp1 = curr.next
            curr.next = prev
            prev = curr
            curr = currp1
        
        return prev