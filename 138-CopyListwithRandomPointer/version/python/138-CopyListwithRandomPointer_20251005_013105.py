# Last updated: 10/5/2025, 1:31:05 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        temp = head

        while temp is not None : 
            copy_node = Node(temp.val)
            tempp1 = temp.next
            temp.next = copy_node
            copy_node.next = tempp1
            temp = temp.next.next
        
        temp = head
        dummyNode = Node(0)
        copy = dummyNode

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # 3️⃣ Step 3: Separate the original and copied lists
        temp = head
        dummy = Node(0)
        copy = dummy
        while temp:
            copy.next = temp.next
            temp.next = temp.next.next  # restore original
            copy = copy.next
            temp = temp.next

        return dummy.next