# Last updated: 11/17/2025, 12:26:45 AM
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_map = set()

        for i in range(len(deadends)) : 
            dead_map.add(deadends[i])

        if target in dead_map or '0000' in dead_map : 
            return -1

        queue = []
        queue.append(('0000' , 0))
        visited = set()
        visited.add('0000')

        while len(queue) > 0 : 
            curr , iterations = queue.pop(0)

            if curr == target : 
                return iterations

            for i in range(4) : 
                new_combination_forward = curr[:i] + str(((int(curr[i]) + 1) + 10 )%10) + curr[i+1:]
                new_combination_backward = curr[:i] + str(((int(curr[i]) - 1) + 10 )%10) + curr[i+1:]

                if new_combination_forward not in dead_map and new_combination_forward not in visited : 
                    visited.add(new_combination_forward)
                    queue.append((new_combination_forward , iterations + 1))
                
                if new_combination_backward not in dead_map and new_combination_backward not in visited : 
                    visited.add(new_combination_backward)
                    queue.append((new_combination_backward , iterations + 1))
        
        return -1