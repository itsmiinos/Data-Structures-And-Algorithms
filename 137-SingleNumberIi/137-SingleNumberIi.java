// Last updated: 8/13/2025, 8:22:30 PM
class Solution {
    public int singleNumber(int[] nums) {
        int count;
        int ans=0;
        int n = nums.length;
        for(int i=0;i<32;i++){
            count = 0;
            for(int j=0;j<n;j++){
                if(checkBit(nums[j],i)){
                    count++;
                }
            }
            if(count%3!=0){
                ans = (ans + (1<<i));
            }
        }
        return ans;
    }

    public boolean checkBit(int n, int k){
        if((n & (1<<k))==0){
            return false;
        }
        return true;
    }
}