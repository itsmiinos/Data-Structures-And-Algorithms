class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        my_chars = collections.defaultdict(int)
        i = 0
        j = 0
        count = 0

        while j < len(s) :
            my_chars[s[j]]+=1

            while my_chars['a'] > 0 and my_chars['b'] > 0 and my_chars['c'] > 0 :
                count += len(s) - j
                my_chars[s[i]]-=1
                i+=1
            
            j+=1
        
        return count