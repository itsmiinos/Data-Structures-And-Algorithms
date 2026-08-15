# Last updated: 8/15/2026, 8:40:24 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev = None
9        curr = head
10
11        while curr is not None : 
12            currp1 = curr.next
13            curr.next = prev
14            prev = curr
15            curr = currp1
16        
17        return prev