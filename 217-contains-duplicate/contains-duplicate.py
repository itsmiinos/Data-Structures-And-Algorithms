class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for i in range (0,len(nums)):
            if nums[i] in mySet :
                return True
            else :
                mySet.add(nums[i])

        return False
        