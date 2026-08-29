class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_map = collections.defaultdict(int)
        maxi = 0
        max_len = 0
        i = 0
        j = 0

        while j < len(s) :
            
            my_map[s[j]] +=1
            maxi = max(maxi , my_map[s[j]])

            while (j - i + 1) - maxi > k :
                my_map[s[i]] -=1
                i+=1
            
            if (j - i + 1) - maxi <= k :
                max_len = max(max_len , j - i + 1)

            j+=1
        
        return max_len