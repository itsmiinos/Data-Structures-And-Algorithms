# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None :
            return True
        
        slow = head
        fast = head

        while fast and fast.next : 
            slow = slow.next
            fast = fast.next.next
        
        prev = None

        while slow is not None :
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        left = head
        right = prev

        while right : 
            if left.val != right.val :
                return False
            left = left.next
            right = right.next
        
        return True