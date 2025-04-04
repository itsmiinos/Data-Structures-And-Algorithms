#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        flag = True
        
        while flag:
            flag = False
            for i in range (1,len(arr)) :
                if arr[i-1] > arr[i] :
                    flag = True
                    [arr[i-1] , arr[i]] = [arr[i] , arr[i-1]]
        
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends