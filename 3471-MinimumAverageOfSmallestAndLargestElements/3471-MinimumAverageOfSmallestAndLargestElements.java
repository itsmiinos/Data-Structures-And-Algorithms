// Last updated: 8/13/2025, 8:15:14 PM
class Solution {
    public double minimumAverage(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int left = 0;
        int right = n-1;
        double averages[] = new double[n/2];
        int i = 0;
        double minAverage = Double.MAX_VALUE;
        
        while(left<right){
            averages[i] = (double)(nums[left] + nums[right])/2;
            minAverage = Math.min(minAverage,averages[i]);
            i++;
            left++;
            right--;
        }
        
        return minAverage;
    }
}