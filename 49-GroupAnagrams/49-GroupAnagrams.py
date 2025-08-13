# Last updated: 8/13/2025, 8:23:43 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs : #each string
            count = [0]*26 #a-z
            for c in s : #each character
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            if key in res :
                res[key].append(s)
            else : 
                res[key] = [s]
        
        return list(res.values())