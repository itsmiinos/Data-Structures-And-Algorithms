class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        ans = ""
        for i in range(len(s)) :
            if s[i] == ')' :
                depth-=1
                if depth >= 1 :
                    ans += s[i]
            else :
                depth+=1
                if depth > 1 :
                    ans += s[i]
            print(s[i] , depth)
        
        return ans
            