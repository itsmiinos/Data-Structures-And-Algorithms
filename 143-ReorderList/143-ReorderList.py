# Last updated: 8/13/2025, 8:22:08 PM
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
        # get the middle point

        slow = head
        fast = head

        while fast is not None and fast.next is not None : 
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None #dividing the two list

        #reversing the second list
        prev = None
        curr = second_head

        while curr is not None : 
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        #adding to the list one by one
        p1 = head
        p2 = prev

        i = 1

        while p1 is not None and p2 is not None : 
            if i%2 == 0 : 
                p2_next = p2.next
                p1_next = p1.next
                p1.next = p2
                p2.next = p1_next
                p2 = p2_next
                p1 = p1_next
            i+=1
        
        return head

        
        