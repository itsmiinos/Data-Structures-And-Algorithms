import sys
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        my_map = {}

        for i in range(len(arr)) : 
            my_map[arr[i]] = my_map.get(arr[i] , 0) + 1

        maxi = -sys.maxsize
        for key in my_map : 
            if my_map[key] == key : 
                maxi = max(maxi , key)

        return maxi if maxi >=1 else -1