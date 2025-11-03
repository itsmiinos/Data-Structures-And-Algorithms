# Last updated: 11/3/2025, 8:11:22 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp  = {} #dp need to keep track of total and index, total can be a lot so taking hashmap instead of array
        
        return self.solve(coins , len(coins)-1 , amount , dp)
    
    def solve(self , coins : list , index : int , amount : int , dp : tuple) -> int :

        if amount < 0 : 
            return 0 

        if index < 0 : 
            if amount == 0 : 
                return 1
            else : 
                return 0
        
        if (index , amount) in dp : 
            return dp[(index , amount)]
        
        take_coin = self.solve(coins , index , amount - coins[index] , dp)
        dont_take_coin = self.solve(coins , index - 1 , amount , dp)

        dp[(index , amount)] = take_coin + dont_take_coin

        return dp[(index , amount)]