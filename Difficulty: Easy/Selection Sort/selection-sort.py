#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range (len(arr)):
            minIndex = i
            for j in range (i,len(arr)) :
                if arr[minIndex] > arr[j] :
                    minIndex = j
            
            [arr[i] , arr[minIndex]] = [arr[minIndex] , arr[i]]
        return arr

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = [int(i) for i in input().split()]

        obj = Solution()
        obj.selectionSort(arr)

        IntArray().Print(arr)
        print("~")

# } Driver Code Ends