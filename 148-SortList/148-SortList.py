# Last updated: 8/13/2025, 8:21:59 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None : 
            return head
        
        middle = self.findMiddle(head)
        left_half = head
        right_half = middle.next
        middle.next = None

        left = self.sortList(left_half)
        right = self.sortList(right_half)

        return self.merge(left , right)

    
    def findMiddle(self , head : ListNode) -> ListNode : 
        fast = head
        slow = head
        prev = None

        while fast is not None and fast.next is not None : 
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        return prev
    
    def merge(self , head1 : ListNode , head2 : ListNode) -> ListNode : 

        if head1 is not None and head2 is None : 
            return head1
        
        elif head1 is None and head2 is not None : 
            return head2
        
        elif head1 is None and head2 is None : 
            return None
        
        dummyNode = ListNode(None)
        temp = dummyNode

        while head1 is not None and head2 is not None : 
            if head1.val < head2.val : 
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            else : 
                temp.next = head2
                temp = temp.next
                head2 = head2.next
            
        if head1 is not None : 
            temp.next = head1
        
        if head2 is not None : 
            temp.next = head2
        
        return dummyNode.next
