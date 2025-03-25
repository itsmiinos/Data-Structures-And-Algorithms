#User function Template for python3

class Solution:
    def switchCase(self, choice, arr):
        # Code here
        if (choice == 1) :
            R = arr[0]
            return 3.141592653589793*R*R
        else :
            L = arr[0]
            B = arr[1]
            return L*B

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        choice = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        if choice == 1:
            res = ob.switchCase(choice, arr)
            print("%.2f"%round(res,2))
        else:
            res = ob.switchCase(choice, arr)
            print(int(res))

# } Driver Code Ends