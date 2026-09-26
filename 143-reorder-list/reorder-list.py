# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step1  : find the midpoint
        #step2 : reverse the second half
        #step3 : merge alternate nodes

        slow = head
        fast = head

        while fast is not None and fast.next is not None : 
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None

        prev = None
        curr = second_head

        while curr is not None : 
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        first_head = head
        second_head = prev


        while first_head and second_head :
            first_head_next = first_head.next
            first_head.next = second_head
            second_head_next = second_head.next
            second_head.next = first_head_next
            first_head = first_head_next
            second_head = second_head_next
        
        return head
        