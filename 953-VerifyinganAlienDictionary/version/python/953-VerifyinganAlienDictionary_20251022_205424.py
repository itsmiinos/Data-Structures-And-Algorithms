# Last updated: 10/22/2025, 8:54:24 PM
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapp = {}

        for i in range(len(order)):
            mapp[order[i]] = i

        word1 = ''
        word2 = ''

        for k in range(len(words) - 1):
            word1 = words[k]
            word2 = words[k + 1]
            if len(word1) > len(word2) and word2 in word1:
                return False
            for i, j in zip(word1, word2):
                if i != j:
                    if mapp[i] < mapp[j]:
                        break
                    elif mapp[i] > mapp[j]:
                        return False   
        return True