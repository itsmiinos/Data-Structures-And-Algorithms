import sys
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        feq_map = {}

        for i in range(len(word)) : 
            feq_map[word[i]] = feq_map.get(word[i] , 0) + 1
        
        min_count_del = sys.maxsize 

        for val1 in feq_map : 
            count_del = 0
            for val2 in feq_map : 
                if val1 != val2 : 
                    if feq_map[val2] < feq_map[val1] : 
                        count_del += feq_map[val2]
                    elif feq_map[val2] > feq_map[val1] + k : 
                        count_del += feq_map[val2] - (feq_map[val1] + k)

            min_count_del = min(min_count_del , count_del)

        return min_count_del