// Last updated: 8/13/2025, 8:19:08 PM
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        int[] pMax = new int[n];
        int[] sMin = new int[n];

        pMax[0] = arr[0];
        for(int i=1;i<n;i++){
            pMax[i] = Math.max(pMax[i-1],arr[i]);
        }

        sMin[n-1] = arr[n-1];
        for(int i = n-2; i>=0; i--){
            sMin[i] = Math.min(sMin[i+1],arr[i]);
        }

        int ans = 0;
        
        for(int i =0;i<n-1;i++){
            if(pMax[i] <= sMin[i+1]){
                ans++;
            }
        }
        
        ans++;
        return ans;

    }
}