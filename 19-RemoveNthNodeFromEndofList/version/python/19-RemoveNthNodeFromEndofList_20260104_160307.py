# Last updated: 1/4/2026, 4:03:07 PM
1class Solution:
2    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
3        slow = head
4        fast = head
5
6        while fast is not None and n > 0 : 
7            fast = fast.next
8            n-=1
9        
10        if fast is None : 
11            return head.next
12        
13        while fast.next is not None :
14            slow = slow.next
15            fast = fast.next
16        
17        slow.next = slow.next.next
18
19        return head