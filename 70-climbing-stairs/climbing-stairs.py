class Solution:
    def climbStairs(self, n: int) -> int:
        dynamic_answers = [-1]*(n+1)
        result = self.climbStairsHelper(n , dynamic_answers)
        return result
    
    def climbStairsHelper(self , n: int , dynamic_answers : [int]) -> int :
        if n == 1 or n == 2: return n
        if dynamic_answers[n]!=-1 : return dynamic_answers[n]
        a = self.climbStairsHelper(n-1 , dynamic_answers)
        b = self.climbStairsHelper(n-2 , dynamic_answers)
        dynamic_answers[n] = a+b
        return a+b

    


        