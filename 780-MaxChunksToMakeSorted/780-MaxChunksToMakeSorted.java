// Last updated: 8/13/2025, 8:19:05 PM
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        int maxTillNow = Integer.MIN_VALUE;
        int count = 0;
        for(int i=0;i<n;i++){
            maxTillNow = Math.max(maxTillNow,arr[i]);
            if(maxTillNow==i){
                count++;
            }
        }
        return count;
    }
}