# Last updated: 10/25/2025, 10:01:12 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_map = set()
        for i in range(len(wordList)) : 
            word_map.add(wordList[i])
        
        if endWord not in word_map : 
            return 0
        
        queue = []
        queue.append((beginWord , 1))
        if beginWord in word_map : 
            word_map.remove(beginWord)
        
        while len(queue) > 0 : 
            curr , iterations = queue.pop(0)

            if curr == endWord : 
                return iterations
            
            for i in range(len(curr)) : 
                for j in range(26) : 
                    char = chr(ord('a') + j)
                    changed_word = curr[:i] + char + curr[i+1:]
                    if changed_word in word_map : 
                        queue.append((changed_word , iterations + 1))
                        word_map.remove(changed_word)
        
        return 0
            
