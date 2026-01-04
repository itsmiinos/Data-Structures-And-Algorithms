# Last updated: 1/4/2026, 3:46:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        #step1  : find the midpoint
12        #step2 : reverse the second half
13        #step3 : merge alternate nodes
14
15        slow = head
16        fast = head
17
18        while fast is not None and fast.next is not None : 
19            slow = slow.next
20            fast = fast.next.next
21
22        second_head = slow.next
23        slow.next = None
24
25        prev = None
26        curr = second_head
27
28        while curr is not None : 
29            curr_next = curr.next
30            curr.next = prev
31            prev = curr
32            curr = curr_next
33        
34        first_head = head
35        second_head = prev
36
37
38        while first_head and second_head :
39            first_head_next = first_head.next
40            first_head.next = second_head
41            second_head_next = second_head.next
42            second_head.next = first_head_next
43            first_head = first_head_next
44            second_head = second_head_next
45        
46        return head
47        