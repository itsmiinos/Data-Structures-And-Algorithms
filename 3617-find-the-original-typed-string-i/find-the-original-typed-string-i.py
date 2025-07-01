class Solution:
    def possibleStringCount(self, word: str) -> int:
        sum = 0
        for i in range(1,len(word)) : 
            if word[i-1] == word[i] : 
                sum = sum+1
        return sum+1
