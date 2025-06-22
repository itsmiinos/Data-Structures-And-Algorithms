class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        while len(s)%k != 0 : 
            s = s + fill

        l = len(s)
        
        result = []
        last_added_index = 0
        count = 0

        for i in range(l) : 
            if count==k: 
                result.append(s[last_added_index : i])
                last_added_index = i
                count=0
            count+=1
        result.append(s[last_added_index : l])
        
        return result
        
