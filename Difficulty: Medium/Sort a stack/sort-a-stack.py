class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        self.sortStack(s)
        return s
    
    def sortStack(self,s) :
        if len(s) == 1 :
            return 
        
        temp = s.pop()
        self.sortStack(s)
        self.insertStack(s , temp)
        return
    
    def insertStack(self,s , temp) :
        if len(s) == 0 or s[-1] <= temp :
            s.append(temp)
            return
        val = s.pop()
        self.insertStack(s,temp)
        s.append(val)
        


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


        print("~")
# } Driver Code Ends