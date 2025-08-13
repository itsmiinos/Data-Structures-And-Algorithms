# Last updated: 8/13/2025, 8:16:23 PM
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        count = 0 
        sum = 0

        for i in range (1 , 100) : 
            number = [int(d) for d in str(i)]
            k_value = self.kValue(i,k) #gives an array
            if self.PalindromeOrNot(number) and self.PalindromeOrNot(k_value) : 
                count+=1
                sum = sum+i
                if count == n : 
                    break
        
        L = 3
        while count<n : 
            half_length = (L+1)//2
            isEven = True if L%2==0 else False
            min_number = 10**(half_length-1)
            max_number = (10**half_length)-1
            for i in range(min_number , max_number+1) : 
                generated_number = self.generatePalindrome(i , isEven , half_length)
                number = [int(d) for d in str(generated_number)]
                k_value = self.kValue(generated_number,k) #gives an array
                if self.PalindromeOrNot(number) and self.PalindromeOrNot(k_value) : 
                    print(number , k_value)
                    count+=1
                    sum = sum+generated_number
                    if count == n : 
                        break
            L+=1
        
        return sum
    

    def kValue(self, n:int , k:int) -> [int]:
        result = []
        while n > 0 : 
            result.append(n%k)
            n = n//k
        
        return result
        

    def PalindromeOrNot(self , result:[int]) -> bool :
        start = 0
        end = len(result) - 1
        while start<=end : 
            if result[start] != result[end] :
                return False
            start+=1
            end-=1
        return True
    
    def generatePalindrome(self , number: int , isEven : bool , half_length : int) -> int : 
        string_number = str(number)
        reverse_number = string_number[::-1]
        generated_number = ""
        if isEven : 
            generated_number = string_number + reverse_number
        else : 
            generated_number = string_number + reverse_number[1:]
        
        return int(generated_number)