# Last updated: 8/13/2025, 8:24:22 PM
class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        
        for i in s :
            if i=='(' or i=='{' or i=='[' or len(myStack) == 0 :
                myStack.append(i)
            elif i == ')' :
                if myStack[len(myStack)-1] == '(' :
                    myStack.pop()
                else :
                    return False
            elif i == '}' :
                if myStack[len(myStack)-1] == '{' :
                    myStack.pop()
                else :
                    return False
            elif i == ']' :
                if myStack[len(myStack)-1] == '[' :
                    myStack.pop()
                else :
                    return False
        if len(myStack) == 0 :
            return True
        return False
        