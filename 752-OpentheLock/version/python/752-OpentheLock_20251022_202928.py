# Last updated: 10/22/2025, 8:29:28 PM
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        self.dead = set(deadends)
        self.visited = set()
        if "0000" in self.dead : 
            return -1
        result = self.doBFS("0000" , target)
        return result
    
    def doBFS(self , src : str , target : str) -> int : 
        queue = []
        queue.append([src,0])
        self.visited.add(src)

        while len(queue) > 0 : 
            curr , turns = queue.pop(0)

            if curr == target : 
                return turns

            for child in self.children(curr) : 

                if child not in self.visited and child not in self.dead : 
                    self.visited.add(child)
                    queue.append([child,turns+1])
        
        return -1


    def children(self , curr : str) -> list[str] : 

        result = []

        for i in range(4) : 
            result.append(curr[:i] + str(((int(curr[i]) + 1) + 10) % 10) + curr[i+1 :])
            result.append(curr[:i] + str(((int(curr[i]) - 1) + 10) % 10) + curr[i+1 :])

        return result
