# Last updated: 8/13/2025, 8:24:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(None)
        temp1 = l1
        temp2 = l2
        carry = 0
        temp = dummyNode

        while temp1 is not None or temp2 is not None or carry : 
            x = temp1.val if temp1 else 0
            y = temp2.val if temp2 else 0
            sum = x + y + carry
            carry = sum // 10
            sum = sum % 10
            
            temp.next = ListNode(sum)
            temp = temp.next

            if temp1 : temp1 = temp1.next
            if temp2 : temp2 = temp2.next
        
        return dummyNode.next



        