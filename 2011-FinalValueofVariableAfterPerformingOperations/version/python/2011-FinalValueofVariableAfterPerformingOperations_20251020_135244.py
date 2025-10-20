# Last updated: 10/20/2025, 1:52:44 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations : 
            if op == 'X++' or op == '++X' :
                x+=1
            else : 
                x-=1
        
        return x
            