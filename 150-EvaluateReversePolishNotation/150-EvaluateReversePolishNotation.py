# Last updated: 8/13/2025, 8:21:57 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []

        i = 0
        while i<len(tokens) : 
            if tokens[i] in ['+' , '-' , '*' , '/'] :  
                value2 = operand_stack.pop(-1)
                value1 = operand_stack.pop(-1)
                operator = tokens[i]
                ans = self.calculate(value1 , value2 , operator)

                operand_stack.append(ans)
            else : 
                operand_stack.append(int(tokens[i]))
            # print(operand_stack)
            i+=1
        
        
        return operand_stack[-1]
    

    def calculate(self , value1 : int , value2 : int, operator : str) -> int : 
        if operator == '+' : 
            return value1 + value2
        elif operator == '-' : 
            return value1 - value2
        elif operator == '*' : 
            return value1 * value2
        else : 
            return int(value1 / value2)
    
    def precedence(self , operator : str) -> int :
        if operator == '*' or operator == '/' : 
            return 2
        elif operator == '+' or operator == '-' : 
            return 1
        return 0