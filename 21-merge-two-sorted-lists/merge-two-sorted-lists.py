# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        curr1 = list1
        curr2 = list2
        dummyNode = ListNode()
        temp = dummyNode

        while curr1 is not None and curr2 is not None :
            if curr1.val < curr2.val :
                temp.next = curr1
                curr1 = curr1.next

            else :
                temp.next = curr2
                curr2 = curr2.next
            
            temp = temp.next
        
        while curr1 is not None :
            temp.next = curr1
            curr1 = curr1.next
            temp = temp.next
        
        while curr2 is not None :
            temp.next = curr2
            curr2 = curr2.next
            temp = temp.next
        
        return dummyNode.next