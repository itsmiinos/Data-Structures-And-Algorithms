class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        s = s.lower()
        for i in range(len(s)) :
            if s[i].isalnum() :
                word.append(s[i])
        
        i = 0
        j = len(word)-1
        
        while i <= j :
            if word[i] != word[j] :
                return False
            
            i+=1
            j-=1

        return True