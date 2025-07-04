'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # code here
        if head is None or head.next is None : 
            return head
        
        middle = self.mergeSortMiddleHelper(head)
        middle_next = middle.next
        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(middle_next)
        
        return self.mergeHelper(left , right)
        
        
    
    def mergeSortMiddleHelper(self ,head) : 
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev  # node before midpoint
        
    def mergeHelper(self, head1 , head2) : 
        dummyNode = Node(-1)
        runnerNode = dummyNode
        
        while head1 is not None and head2 is not None : 
            if head1.data < head2.data : 
                runnerNode.next = head1
                head1 = head1.next
                runnerNode = runnerNode.next
            else : 
                runnerNode.next = head2
                head2 = head2.next
                runnerNode = runnerNode.next
        
        if head1 is None : 
            runnerNode.next = head2
        else : 
            runnerNode.next = head1
        
        return dummyNode.next
        
    