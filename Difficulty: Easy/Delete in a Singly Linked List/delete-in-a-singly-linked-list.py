# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    temp = head
    k = 2
    if x == 1 : 
        return head.next
    while temp.next is not None : 
        if k == x: 
            temp.next = temp.next.next
            break
        temp = temp.next
        k+=1
    
    return head