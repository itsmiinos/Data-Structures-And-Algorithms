class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for i in range(len(s)) :
            if len(my_stack) == 0 :
                my_stack.append(s[i])

            elif s[i] == ')' and my_stack[-1] == '(' :
                my_stack.pop(-1)
            
            elif s[i] == '}' and my_stack[-1] == '{' :
                my_stack.pop(-1)
            
            elif s[i] == ']' and my_stack[-1] == '[' :
                my_stack.pop(-1)
            
            else :
                my_stack.append(s[i])
        print(my_stack)
        return len(my_stack) == 0