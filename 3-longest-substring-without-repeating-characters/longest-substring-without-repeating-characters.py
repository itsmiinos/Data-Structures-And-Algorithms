class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        window_size = 0

        for i in range(len(s)) : 
            if s[i] in hashmap : 
                break
            else : 
                hashmap[s[i]] = i
                window_size+=1
        
        i = window_size
        start = 0

        while i < len(s) : 
            if s[i] in hashmap : 
                index = hashmap[s[i]]
                while start <= index : 
                    del hashmap[s[start]]
                    
                    start +=1
            
            hashmap[s[i]] = i
            
            window_size = max(window_size , i - start + 1)
            
            i+=1
        
        return window_size
