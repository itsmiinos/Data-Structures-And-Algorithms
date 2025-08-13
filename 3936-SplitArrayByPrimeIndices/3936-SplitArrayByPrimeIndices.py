# Last updated: 8/13/2025, 8:14:46 PM
import math
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        sumPrime = 0
        sumNotPrime = 0

        for i in range(len(nums)) : 
            if self.isPrime(i) and i > 1 : 
                sumPrime += nums[i]

            else : 
                sumNotPrime += nums[i]

        return abs(sumPrime - sumNotPrime)


    def isPrime(self , number : int) -> bool :
        count = 0
        for i in range(2 , int(math.sqrt(number))+1) : 
            if number % i == 0 : 
                count+=1

        if count > 0 : 
            return False
        return True