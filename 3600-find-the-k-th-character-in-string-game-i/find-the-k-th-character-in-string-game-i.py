class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        result = ""
        while len(result) < k  : 
            result = self.createNewString(word)
            word = result
        return result[k-1]
    
    def createNewString(self , word : str) -> str :
        result = "" 
        for i in range(len(word)) : 
            if word[i] == 'z' : 
                result+= 'a'
            else :
                result += chr((ord(word[i]) + 1))
            # print(word)
        
        return word+result


        
        
        
        