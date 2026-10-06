class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        open_brackets = 0
        i = 0

        while i < len(s) :
            if s[i] == '(' :
                open_brackets +=1
            elif s[i] == ')' and open_brackets > 0:
                open_brackets -=1
            elif s[i] == ')' and open_brackets == 0 :
                count+=1

            i+=1

        return count + open_brackets