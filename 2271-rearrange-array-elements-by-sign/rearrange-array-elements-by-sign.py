class Solution(object):
    def rearrangeArray(self, nums):
        negativeStack = []
        positiveStack = []
        ans = []

        for i in range(len(nums)) :
            if nums[i] < 0 :
                negativeStack.append(nums[i])
            else :
                positiveStack.append(nums[i])
        
        print(negativeStack)
        print(positiveStack)
        
        pi = 0
        ni = 0
        index = 0
        previous = -1

        while index<len(nums) :
            if previous < 0 :
                ans.append(positiveStack[pi])
                pi+=1
            else : 
                ans.append(negativeStack[ni])
                ni+=1
            previous = ans[index]
            index+=1
        
        return ans
        