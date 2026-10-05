# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Pair :
    def __init__(self , value : int , node : ListNode) -> None :
        self.value = value
        self.node = node

    def __lt__(self , other) -> bool:
        return self.value < other.value



class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        my_heap = []
        for l in lists :
            if l is not None :
                heapq.heappush(my_heap , Pair(l.val , l))
        
        dummyNode = ListNode()
        temp = dummyNode

        while len(my_heap) > 0 :
            temp.next = heapq.heappop(my_heap).node
            temp = temp.next

            if temp.next is not None :
                heapq.heappush(my_heap , Pair(temp.next.val , temp.next))
        
        return dummyNode.next
