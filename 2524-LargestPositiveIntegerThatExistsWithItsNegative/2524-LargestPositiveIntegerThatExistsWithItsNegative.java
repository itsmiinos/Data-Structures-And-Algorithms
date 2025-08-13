// Last updated: 8/13/2025, 8:15:54 PM
class Solution {
    public int findMaxK(int[] nums) {
        int ans = -1;
        HashSet<Integer> h = new HashSet();
        int n = nums.length;
        for(int i=0;i<n;i++){
            int num = nums[i]*(-1);
            if(h.contains(num)){
                ans = Math.max(ans,Math.abs(num));
            }
            else{
                h.add(nums[i]);
            }
        }
        return ans;
    }
}