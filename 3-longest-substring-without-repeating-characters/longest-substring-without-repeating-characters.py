class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_word = set()
        i = 0
        j = 0
        max_len = 0

        while j < len(s) :
            
            while s[j] in my_word :
                my_word.remove(s[i])
                i+=1
            
            my_word.add(s[j])

            max_len = max(max_len , j - i + 1)
        
            j+=1
        
        return max_len