# Last updated: 8/13/2025, 8:17:04 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        counter = 0
        nodeToConnect = ListNode(-1)
        dummyNode = ListNode(-1)
        dummyNode.next = list1
        temp = dummyNode

        while temp.next is not None : 
            if counter == a : 
                nextNode = temp.next
                temp.next = list2
                while counter!=b :
                    nextNode = nextNode.next
                    counter +=1
                nodeToConnect = nextNode.next
            temp = temp.next
            counter+=1
        
        temp.next = nodeToConnect
        return dummyNode.next
