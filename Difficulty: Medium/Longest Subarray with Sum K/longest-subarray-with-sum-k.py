# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
       # code here
        prefixSum = 0
        diff = 0
        maxSubArrayLength = 0
        map = {}
        for i in range(len(arr)) : 
            prefixSum += arr[i]
            if prefixSum == k :
                maxSubArrayLength = i+1
            diff = prefixSum - k
            if diff in map :
                subArrayLength = i-map[diff]
                maxSubArrayLength = max(maxSubArrayLength , subArrayLength)
            if prefixSum not in map :
                map[prefixSum] = i
            
            # maxSubArrayLength = max(subArrayLength , maxSubArrayLength)
        
        return maxSubArrayLength
        
        ## The below can be used with only positive array
        
        # i=0
        # j=0
        # sum = arr[0]
        # subArrayLength = 0
        # while j<len(arr) and i<len(arr) :
        #     while sum > k and i<=j :
        #         sum = sum - arr[i]
        #         i+=1
        #     if sum == k :
        #         subArrayLength = max(subArrayLength , j-i+1)
        #     j+=1
        #     if sum < k : 
        #         sum += arr[j]
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends
