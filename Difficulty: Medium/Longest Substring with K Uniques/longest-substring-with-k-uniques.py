import collections
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        right = 0
        left = 0
        max_len = -1
        lookup = collections.defaultdict(int)

        while right < len(s) :
            lookup[s[right]] +=1

            while len(lookup) > k :
                lookup[s[left]] -=1
                if lookup[s[left]] == 0 :
                    del lookup[s[left]]
                
                left+=1
            
            if len(lookup) == k :
                max_len = max(max_len , right - left + 1)
        
            right +=1
        
        return max_len
        
        