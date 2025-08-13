# Last updated: 8/13/2025, 8:19:37 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_stack = []
        i = 0
        hashmap = {}

        while i < len(nums2) : 

            while len(my_stack) > 0 and my_stack[-1][0] < nums2[i] : 
                popped = my_stack.pop(-1)
                popped_element = popped[0]
                popped_index = popped[1]
                hashmap[nums2[popped_index]] = nums2[i]
            
            my_stack.append([nums2[i] , i])
            i+=1
        
        result = []

        for i in range(len(nums1)) : 
            result.append(hashmap.get(nums1[i])) if nums1[i] in hashmap else result.append(-1)
        
        return result
