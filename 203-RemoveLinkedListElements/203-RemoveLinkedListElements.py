# Last updated: 8/13/2025, 8:21:27 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        temp = dummyNode

        while temp.next is not None :
            if temp.next.val == val :
                temp.next = temp.next.next
            else :
                temp = temp.next
            
        return dummyNode.next
        