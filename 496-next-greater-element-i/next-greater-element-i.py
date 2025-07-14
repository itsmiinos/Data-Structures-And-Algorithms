class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_stack = []
        i = 0
        next_greater = [-1]*len(nums2)

        while i < len(nums2) : 

            while len(my_stack) > 0 and my_stack[-1][0] < nums2[i] : 
                popped = my_stack.pop(-1)
                popped_element = popped[0]
                popped_index = popped[1]
                next_greater[popped_index] = nums2[i]
            
            my_stack.append([nums2[i] , i])
            i+=1
        
        result = []

        for i in range(len(nums1)) : 
            for j in range(len(nums2)) : 
                if nums1[i] == nums2[j] : 
                    result.append(next_greater[j])
        
        return result
