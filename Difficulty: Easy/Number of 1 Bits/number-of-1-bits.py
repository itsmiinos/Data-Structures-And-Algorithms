#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		count = 0
		for i in range(32) : 
		    if self.checkBit(n , i) : 
		        count+=1
		 
		return count
    
    def checkBit(self , n:int , i : int) : 
        if n & (1<<i) :
            return True
        return False