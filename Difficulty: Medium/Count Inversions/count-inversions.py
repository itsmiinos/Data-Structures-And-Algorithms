class Solution:
    def inversionCount(self, arr):
        # Code Here
        self.count = 0
        self.mergeSort(arr , 0 , len(arr)-1)
        return self.count
    
    def mergeSort(self , arr : list , low : int , high : int) -> None :
        if low >= high : 
            return
        mid = low + (high - low) // 2
        
        self.mergeSort(arr , low , mid)
        self.mergeSort(arr , mid + 1 , high)
        self.merge(arr , low , mid , high)
    
    def merge(self , arr , low  : int, mid : int , high : int) -> None :
        temp = []
        left = low
        right = mid + 1
        
        while left <= mid and right <= high :
            if arr[left] <= arr[right] :
                temp.append(arr[left])
                left+=1
            else :
                temp.append(arr[right])
                self.count += (mid - left + 1)
                right+=1
        
        while left <= mid :
            temp.append(arr[left])
            left+=1
        
        while right <= high :
            temp.append(arr[right])
            right+=1
        
        for i in range(len(temp)) :
            arr[i + low] = temp[i]