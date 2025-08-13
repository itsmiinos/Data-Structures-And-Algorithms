# Last updated: 8/13/2025, 8:18:18 PM
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        feq_map = {}

        for i in range(len(deck)) : 
            feq_map[deck[i]] = feq_map.get(deck[i] , 0) + 1 
        
        ans = 0
        for key in feq_map.keys() : 
            ans = self.gcdCalculator(ans , feq_map[key])
            if ans <=1 : 
                return False
        
        return True
    
    def gcdCalculator(self , a:int , b:int) -> int : 
        if a == 0 : 
            return b
        
        temp = self.gcdCalculator(b%a , a)
        return temp