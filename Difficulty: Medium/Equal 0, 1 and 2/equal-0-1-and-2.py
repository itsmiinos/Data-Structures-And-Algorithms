#User function Template for python3

class Solution:

    def getSubstringWithEqual012(self, Str):
        # code here
        prefixCountZero = [None]*len(Str)
        prefixCountOne = [None]*len(Str)
        prefixCountTwo = [None]*len(Str)
        
        self.makePrefix(Str , prefixCountZero , '0')
        self.makePrefix(Str , prefixCountOne , '1')
        self.makePrefix(Str , prefixCountTwo , '2')
        
        map = {}
        map['0,0'] = 1
        count = 0
        for i in range(len(Str)) : 
            diff1 = prefixCountZero[i] - prefixCountOne[i]
            diff2 = prefixCountZero[i] - prefixCountTwo[i]
            toCheck = str(diff1) + ',' + str(diff2) 
            count += map.get(toCheck , 0)
            map[toCheck] = map.get(toCheck , 0) + 1
        
        return count
                
                
    def makePrefix(self , string : str , prefixArray : list[None] , k : str) :
        currentCount = 0
        for i in range (len(string)) : 
            if string[i] == k : 
                prefixArray[i] = currentCount+1
                currentCount+=1
            else : 
                prefixArray[i] = currentCount