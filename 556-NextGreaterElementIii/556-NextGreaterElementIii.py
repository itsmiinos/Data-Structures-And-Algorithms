# Last updated: 8/13/2025, 8:19:26 PM
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = self.convertNumberToArray(n) #this will provide an array
        l = len(nums)

        dip_index = -1 #the index where the first number is smaller than the second number
        for i in range(l-2 , -1 , -1) :
            if nums[i+1] > nums [i] : 
                dip_index = i
                break

        if dip_index == -1 : 
            return -1

        next_greater_element = -1 #the next greater element which we need to swap with

        for i in range(l-1 , dip_index , -1):
            if nums[i] > nums[dip_index] : 
                next_greater_element = i
                break
        
        [nums[dip_index] , nums[next_greater_element]] = [nums[next_greater_element] , nums[dip_index]] #swapping

        # we have now go the first number of the next greater element in place
        # now a possiblity of a smaller number to exits can be in place so we need to reverse all the elements after dip_index to get the actual smallest number

        self.reversePartOfArray(dip_index+1 , l-1 , nums)

        smallest_number = self.convertArrayToNumber(nums)

        return smallest_number if smallest_number <= 2**31 -1 else -1


    
    def convertNumberToArray(self , n:int) -> [int] : 
        return [int(d) for d in str(n)] #1. convert the number to string, 2. for each charachter of the string convert it to decimal 3. store every decimal in an array form

    def reversePartOfArray(self , start : int , end : int , nums : [int]) -> None : 
        while start <= end : 
            [nums[start] , nums[end]] = [nums[end] , nums[start]]
            start+=1
            end-=1

    def convertArrayToNumber(self , nums : [int]) -> int : 
        number = 0

        for i in range(len(nums)) : 
            number = number*10 + nums[i]
        
        return number
        