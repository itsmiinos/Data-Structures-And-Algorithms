# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # l1 = self.reverseLinkedList(l1)
        # l2 = self.reverseLinkedList(l2)

        sum = 0
        carry = 0
        dummyNode = ListNode()
        temp = dummyNode

        while l1 or l2 :
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum = val1 + val2 + carry
            carry = 0
            if sum > 9 :
                carry = sum // 10
                sum = sum % 10
            else :
                carry = 0
            newNode = ListNode(sum)
            temp.next = newNode
            print(newNode.val)
            temp = temp.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if carry > 0 :
            temp.next = ListNode(carry)
        
        head = dummyNode.next
        return head
    


    def reverseLinkedList(self , head : listNode) -> listNode :
        prev = None
        curr = head

        while curr is not None :
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev