class Solution:
	def subsetSums(self, arr):
		# code here
		sum = 0
		self.result = []
		def helper(index , sum) : 
		    if index > len(arr)-1 : 
		        self.result.append(sum)
		        return
		    
		    helper(index + 1 , sum + arr[index]) #take
		    helper(index + 1 , sum) #dont take
		    
		    return 0
		helper(0,0)
		self.result.sort()
		return self.result
		       
		    