class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        map = {}

        for bricks in wall : 
            gap = 0
            for i in range(len(bricks)-1) : 
                gap = gap + bricks[i]
                map[gap] = map.get(gap , 0) + 1
            
        max_break = 0
        for values in map.values() : 
            max_break = max(max_break , values)
        
        return len(wall) - max_break