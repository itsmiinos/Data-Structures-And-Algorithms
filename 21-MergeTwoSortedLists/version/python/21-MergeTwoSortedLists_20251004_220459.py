# Last updated: 10/4/2025, 10:04:59 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummyNode = ListNode()
        temp = dummyNode
        
        while head1 is not None and head2 is not None :

            if head1.val <= head2.val : 
                temp.next = head1
                head1 = head1.next
            else :
                temp.next = head2
                head2 = head2.next
            
            temp = temp.next
        
        if head1 is not None : 
            temp.next = head1
        
        if head2 is not None : 
            temp.next = head2
        
        return dummyNode.next
