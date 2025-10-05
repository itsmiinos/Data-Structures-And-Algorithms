# Last updated: 10/5/2025, 7:53:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode(0)
        temp = dummyNode

        while l1 is not None or l2 is not None or carry!= 0 : 
            number1 = l1.val if l1 is not None else 0
            number2 = l2.val if l2 is not None else 0
            sum = number1 + number2 + carry
            carry = sum // 10
            sum = sum % 10

            temp.next = ListNode(sum)
            temp = temp.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        return dummyNode.next
            
