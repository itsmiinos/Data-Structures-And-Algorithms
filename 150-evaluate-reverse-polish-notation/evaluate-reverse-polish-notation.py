class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []

        for i in tokens :
            if i == '+' :
                val1 = myStack.pop()
                val2 = myStack.pop()
                sum = val1 + val2
                myStack.append(sum)
            elif i == '-' :
                val2 = myStack.pop()
                val1 = myStack.pop()
                minus = val1 - val2
                myStack.append(minus)
            elif i == '*' : 
                val2 = myStack.pop()
                val1 = myStack.pop()
                product = val1 * val2
                myStack.append(product)
            elif i == '/' :
                val2 = myStack.pop()
                val1 = myStack.pop()
                remainder = int(val1 / val2)
                myStack.append(remainder)
            else : 
                myStack.append(int(i))
        return myStack[0]
