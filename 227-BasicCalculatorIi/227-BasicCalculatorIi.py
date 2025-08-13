# Last updated: 8/13/2025, 8:21:00 PM
class Solution:
    def calculate(self, s: str) -> int:
        operand = []
        operator = []
        i = 0
        while i < len(s) : 
            if s[i] in ['+' ,'-' , '*' , '/'] : 
                while len(operator) > 0 and self.precedence(operator[-1]) >= self.precedence(s[i]) : 
                    value2 = operand.pop(-1)
                    value1 = operand.pop(-1)
                    op = operator.pop(-1)
                    
                    value = self.calculation(value1, value2 , op)
                    operand.append(value)
                
                operator.append(s[i])
            elif s[i] == '(' : 
                operator.append(s[i])
            elif s[i] == ')' : 
                while operator[-1] != '(' : 
                    value2 = operand.pop(-1)
                    value1 = operand.pop(-1)
                    op = operator.pop(-1)
                    
                    value = self.calculation(value1 , value2 , op)
                    operand.append(value)

                operator.pop(-1)
            elif s[i] != ' ' : 
                number = 0
                while i < len(s) and s[i] not in ['+' ,'-' , '*' , '/' , ' '] : 
                    number = number * 10 + int(s[i])
                    i+=1
                
                operand.append(number)
                i-=1
            i+=1
        
        while len(operator) > 0: 
            value2 = operand.pop(-1)
            value1 = operand.pop(-1)
            op = operator.pop(-1)
                    
            value = self.calculation(value1, value2 , op)
            operand.append(value)
        
        return operand.pop(-1)
        
    
    def calculation(self , a : int , b : int , o : str) -> int : 
        if o == '+' : 
            return a + b
        elif o == '-' : 
            return a - b
        elif o == '*' : 
            return a * b
        else : 
            return a // b

    def precedence(self , c : str) -> int : 
        if c == '*' or c == '/' : 
            return 2
        elif c == '+' or c == '-' : 
            return 1
        return 0