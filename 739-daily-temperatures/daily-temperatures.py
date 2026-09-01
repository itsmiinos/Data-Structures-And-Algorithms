class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)) :
            while len(my_stack) > 0 and temperatures[i] > my_stack[-1][0] :
                value , index = my_stack.pop(-1)

                ans[index] = i - index

            my_stack.append([temperatures[i] , i])
        
        return ans