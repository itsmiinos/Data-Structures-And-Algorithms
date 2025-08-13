// Last updated: 8/13/2025, 8:17:18 PM
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int start = 0;
        int end = arr.length-1;
        int missing = 0;
        
        while(start<=end){
            int mid = start + (end-start)/2;
            missing = arr[mid]-(mid+1);
            if(k<=missing){
                end = mid-1;
            }
            else{
                start = mid+1;
            }
        }
        return k + end + 1;
    }
}