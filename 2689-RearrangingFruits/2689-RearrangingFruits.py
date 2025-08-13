# Last updated: 8/13/2025, 8:15:43 PM
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        min_Ele  = float('inf')
        my_map = {}

        for i in range(len(basket1)) : 
            my_map[basket1[i]] = my_map.get(basket1[i] , 0) + 1
            min_Ele = min(min_Ele , basket1[i])
        
        for i in range(len(basket2)) : 
            my_map[basket2[i]] = my_map.get(basket2[i] , 0) - 1
            min_Ele = min(min_Ele , basket2[i])
        
        temp_arr = []
        for key in sorted(my_map.keys()) : 
            count = abs(my_map[key])
            value = key

            if count % 2 != 0 : 
                return -1
            
            else : 
                for i in range((count//2)) : 
                    temp_arr.append(value)
        
        cost = 0
        for i in range(len(temp_arr)//2) : 
            cost += min(temp_arr[i] , min_Ele * 2)
        
        return cost