# Last updated: 10/19/2025, 8:21:00 PM
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        visited = set()
        self.smallest = s
        self.dfs(s , a , b , visited)

        return self.smallest
        
    def dfs(self , s , a , b , visited) -> str : 

        if s in visited:
            return
        visited.add(s)
        
        # Update smallest if current is smaller
        if s < self.smallest:
            self.smallest = s

        # Operation 1: add 'a' to all digits at odd indices
        added = self.addOddIntegers(s, a)
        self.dfs(added, a, b, visited)

        # Operation 2: rotate right by 'b'
        rotated = self.rotateString(s, b)
        self.dfs(rotated, a, b, visited)
        
    
    def rotateString(self , s : str , b : int) -> int :
        return s[b:] + s[:b]

    def addOddIntegers(self , s : str , a : int) -> int :
        temp = s
        for i in range(len(temp)) :
            if i%2 != 0 : 
                # temp[i] = str((int(temp[i]) + a)%10)
                temp = temp[:i] + str((int(temp[i]) + a)%10) + temp[i+1 : ]

        return temp 
        
