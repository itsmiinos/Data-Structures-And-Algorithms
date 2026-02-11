#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        i = len(pre_exp)-1
        stack = []
        
        while i > -1 :
            if pre_exp[i].isalnum() :
                stack.append(pre_exp[i])
            
            else :
                operand_one = stack.pop(-1)
                operand_two = stack.pop(-1)
                stack.append(operand_one  + operand_two + pre_exp[i])
            
            i-=1
        
        return stack[-1]