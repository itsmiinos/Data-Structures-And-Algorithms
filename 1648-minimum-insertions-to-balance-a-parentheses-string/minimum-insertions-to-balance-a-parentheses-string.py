class Solution:
    def minInsertions(self, s: str) -> int:
        needed_right = 0
        count = 0

        for i in range(len(s)) :
            if s[i] == ')' :
                needed_right -=1
                if needed_right < 0 :
                    count+=1
                    needed_right = 1
            else :
                if needed_right % 2 != 0 :
                    count+=1
                    needed_right -=1
                
                needed_right += 2
            
        return count + needed_right

