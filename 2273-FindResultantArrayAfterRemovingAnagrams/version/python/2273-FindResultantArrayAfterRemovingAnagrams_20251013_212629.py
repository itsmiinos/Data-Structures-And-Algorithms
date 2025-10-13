# Last updated: 10/13/2025, 9:26:29 PM
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        result.append(words[0])

        for i in range(1 , len(words)) : 
            if len(words[i]) != len(result[-1]) : 
                result.append(words[i])
            elif self.checkAnagram(result[-1] , words[i]) == False : 
                result.append(words[i])
        
        return result
    
    def checkAnagram(self , word1 : str , word2 : str) -> bool : 

        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(word1)) : 
            if word1[i] in hashmap1 :
                hashmap1[word1[i]] +=1
            else :
                hashmap1[word1[i]] = 1
        
        for i in range(len(word2)) : 
            if word2[i] in hashmap2 :
                hashmap2[word2[i]] +=1
            else :
                hashmap2[word2[i]] = 1
        
        for key in sorted(hashmap1.keys()) :
            if key not in hashmap2 or hashmap1[key] != hashmap2[key]: 
                return False
        
        return True

