class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        operands = []

        i = 0
        while i < len(s) : 
            if s[i] >= '0' and s[i] <='9' : 
                number = ''
                while i < len(s) and s[i] >= '0' and s[i] <='9' : 
                    number += s[i]
                    i+=1
                
                number = int(number)
                operands.append(number)
            
            else : 
                if s[i] == '+' or s[i] == '-' : 
                    if len(operands) > 1 : 
                        while len(operands) > 1 : 
                            second_number = operands.pop(-1)
                            first_number = operands.pop(-1)
                            operator = operators.pop(-1)
                            answer = self.calculation(first_number , second_number , operator)
                            operands.append(answer)
                        
                    operators.append(s[i])
                    
                elif s[i] == '*' or s[i] == '/' : 
                    
                    if len(operators) > 0 and (operators[-1] == '*' or operators[-1] == '/') : 
                        second_number = operands.pop(-1)
                        first_number = operands.pop(-1)
                        operator = operators.pop(-1)
                        answer = self.calculation(first_number , second_number , operator)
                        operands.append(answer)

                    operators.append(s[i])
                i+=1
            print(operands , operators)
        
        while len(operators) > 0 : 
            second_number = operands.pop(-1)
            first_number = operands.pop(-1)
            operator = operators.pop(-1)
            answer = self.calculation(first_number , second_number , operator)
            operands.append(answer)
        
        return operands.pop(-1)
        
                    
    

    def calculation(self , a : int , b : int , c : str) -> int :
        if c == '+' : 
            return a + b
        elif c == '-' : 
            return a - b
        elif c == '*' :
            return a * b
        else : 
            return a // b