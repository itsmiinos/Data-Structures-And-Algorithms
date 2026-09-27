class Solution:
    def reverseParentheses(self, s: str) -> str:
        my_stack = []
        i = 0
        ans = ""

        while i < len(s) :
            if s[i].isalpha() == False :
                if s[i] == "(" :
                    my_stack.append("(")
                else :
                    string = ""
                    while my_stack[-1] != "(" :
                        string += my_stack.pop(-1)[::-1]
                    my_stack.pop(-1)
                    my_stack.append(string)

            else :
                if len(my_stack) != 0 :
                    my_stack.append(s[i])

                else :
                    ans += s[i]
            print(my_stack)
            i+=1
        
        for i in range(len(my_stack)) :
            ans+= my_stack[i]
        
        return ans