#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        #code here
        for i in range (1,len(arr)) : 
            for j in range (i , 0 , -1) :
                if arr[j-1] > arr[j] :
                    [arr[j] , arr[j-1]] = [arr[j-1] , arr[j]]
                
        return arr


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.insertionSort(arr)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends