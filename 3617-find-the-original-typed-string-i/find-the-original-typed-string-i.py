class Solution:
    def possibleStringCount(self, word: str) -> int:
        possiblity = 1

        for i in range(1 , len(word)) : 
            if word[i-1] == word[i] : 
                possiblity+=1
        
        return possiblity