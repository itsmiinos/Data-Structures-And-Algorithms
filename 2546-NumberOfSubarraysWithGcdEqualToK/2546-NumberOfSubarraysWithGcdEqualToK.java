// Last updated: 8/13/2025, 8:15:56 PM
class Solution {
    public int subarrayGCD(int[] nums, int k) {
        int count = 0;
        int n = nums.length;
        for(int i=0;i<n;i++){
            int ans = 0;
            for(int j=i;j<n;j++){
                ans = gcd(nums[j],ans);
                if(ans<k){
                    break;
                }
                if(ans==k){
                    count++;
                }
            }
        }
        return count;
    }

    public int gcd(int a , int b){
        if(a==0){
            return b;
        }
        int temp = gcd(b%a,a);
        return temp;
    }
}