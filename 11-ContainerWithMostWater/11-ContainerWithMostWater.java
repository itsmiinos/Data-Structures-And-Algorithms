// Last updated: 8/13/2025, 8:24:39 PM
class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int i = 0;
        int j = n-1;
        int ans = Integer.MIN_VALUE;
        while(i<=j){
            int area = (j-i)*Math.min(height[i],height[j]);
            ans = Math.max(ans,area);
            if(height[i]<height[j]){
                i++;
            }
            else {
                j--;
            }
        }
        return ans;
    }
}