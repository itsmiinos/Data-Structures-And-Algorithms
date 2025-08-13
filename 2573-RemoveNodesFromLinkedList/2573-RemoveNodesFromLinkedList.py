# Last updated: 8/13/2025, 8:15:49 PM
import sys
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        suffixMax = []
        dummyNode = ListNode(-1)
        dummyNode.next = head
        temp = head

        while temp is not None :
            suffixMax.append(temp.val)
            temp = temp.next

        max = suffixMax[len(suffixMax)-1]
        for i in range (len(suffixMax)-1 , -1 , -1) :
            if suffixMax[i] > max : 
                max = suffixMax[i]
            else : 
                suffixMax[i] = max
        
        print(suffixMax)

        temp = dummyNode
        i = 0
        while temp.next is not None : 
            if temp.next.val != suffixMax[i] :
                temp.next = temp.next.next
            else :
                temp =  temp.next
            i+=1
        
        return dummyNode.next
        