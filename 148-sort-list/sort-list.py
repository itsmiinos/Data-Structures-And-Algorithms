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
        left_head = head
        right_head = middle.next
        middle.next = None

        left = self.sortList(left_head)
        right = self.sortList(right_head)

        return self.mergeList(left,right)
    
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev  # Return the node before the midpoint

    def mergeList(self, headA : Optional[ListNode] , headB : Optional[ListNode]) -> Optional[ListNode]:
        if headA is not None and headB is None : 
            return headA
        if headA is None and headB is not None :
            return headB
        if headA is None and headB is None :
            return None
        
        dummyNode = ListNode(-1)
        temp = dummyNode
        temp1 = headA
        temp2 = headB

        while temp1 and temp2 : 
            if temp1.val < temp2.val : 
                temp.next = temp1
                temp1 = temp1.next
            else :
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        
        if temp1 : temp.next = temp1
        else : temp.next = temp2
        
        return dummyNode.next