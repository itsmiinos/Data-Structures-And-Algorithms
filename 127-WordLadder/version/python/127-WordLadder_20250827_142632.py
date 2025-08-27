# Last updated: 8/27/2025, 2:26:32 PM
class Pair :
    def __init__(self , word : str , steps : int) -> None : 
        self.word = word
        self.steps = steps

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashset = set()

        for i in range(len(wordList)) : 
            hashset.add(wordList[i])

        
        queue = []
        queue.append(Pair(beginWord , 1 ))
        # hashset.remove(beginWord)

        while len(queue) > 0 : 
            rem = queue.pop(0)

            word = rem.word
            steps = rem.steps

            if word == endWord : 
                return steps

            for i in range(len(word)) :
                original_letter = word[i]
                for j in range(26) :
                    ch = chr(ord('a') + j)

                    transformed_word = word[:i] + ch + word[i+1:]
                    if transformed_word in hashset :
                        queue.append(Pair(transformed_word , steps + 1))
                        hashset.remove(transformed_word)
        
        return 0
        