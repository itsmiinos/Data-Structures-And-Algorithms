// Last updated: 8/13/2025, 8:23:55 PM
class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] maxPrefix = new int[n];
        int[] maxSuffix = new int[n];
        maxPrefix[0] = height[0];
        for(int i=1;i<n;i++){
            maxPrefix[i] = Math.max(maxPrefix[i-1],height[i]);
        }
        maxSuffix[n-1] = height[n-1];
        for(int i=n-2;i>=0;i--){
            maxSuffix[i] = Math.max(maxSuffix[i+1],height[i]);
        }
        int contribution = 0;
        for(int i=0;i<n;i++){
            int minHeight = Math.min(maxPrefix[i],maxSuffix[i]);
            if(minHeight - height[i]>0){
                contribution += minHeight - height[i];
            }
        }
        return contribution;
    }
}