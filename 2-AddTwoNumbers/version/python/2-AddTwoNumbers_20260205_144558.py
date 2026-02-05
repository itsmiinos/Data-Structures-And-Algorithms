# Last updated: 2/5/2026, 2:45:58 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        carry = 0
9        dummyNode = ListNode()
10        currNode = dummyNode
11        while l1 is not None or l2 is not None :
12            val1 = l1.val if l1 is not None else 0
13            val2 = l2.val if l2 is not None else 0
14            summ = val1 + val2 + carry
15            if summ >= 10 :
16                carry = summ // 10
17                summ = summ % 10
18            else :
19                carry = 0
20            newNode = ListNode(summ)
21            currNode.next = newNode
22            currNode = currNode.next
23            l1 = l1.next if l1 is not None else None
24            l2 = l2.next if l2 is not None else None
25        
26        if carry > 0 :
27            currNode.next = ListNode(carry)
28        return dummyNode.next
29                