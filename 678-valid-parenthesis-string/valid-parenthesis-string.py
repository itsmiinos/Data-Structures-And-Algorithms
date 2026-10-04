class Solution:
    def checkValidString(self, s: str) -> bool:
        brackets = []
        stars = []

        for i in range(len(s)) :
            if s[i] == '(' :
                brackets.append(i)
            elif s[i] == '*' :
                stars.append(i)
            else :
                if len(brackets) == 0 and len(stars) == 0 :
                    return False
                else :
                    if len(brackets) > 0 :
                        brackets.pop(-1)
                    else :
                        stars.pop(-1)

        while len(brackets) > 0 and len(stars) > 0 :
            if s[brackets[-1]] == '(' and stars[-1] < brackets[-1] : 
                return False
            brackets.pop(-1)
            stars.pop(-1)         
        
        return len(brackets) == 0
