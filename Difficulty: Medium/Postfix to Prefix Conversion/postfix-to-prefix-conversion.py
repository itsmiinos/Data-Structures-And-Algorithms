#User function Template for python3

class Solution:
    def postToPre(self, pre_exp):
        # Code here
        i = 0
        stack = []
        
        while i < len(pre_exp) :
            if pre_exp[i].isalnum() :
                stack.append(pre_exp[i])
            
            else :
                operand_one = stack.pop(-1)
                operand_two = stack.pop(-1)
                stack.append(pre_exp[i] + operand_two  + operand_one )
            
            i+=1
        
        return stack[-1]