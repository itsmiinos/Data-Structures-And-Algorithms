# Last updated: 10/4/2025, 10:30:53 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None : 
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second is not None : 
            secondp1 = second.next
            second.next = prev
            prev = second
            second = secondp1
        
        list1 = head
        list2 = prev

        dummyNode = ListNode()
        temp = dummyNode

        first = head
        second = prev
        
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2




        