// Last updated: 8/13/2025, 8:23:59 PM
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
       int a=0;
       int max_sum=nums[0];
       for(int x:nums){
           a=a+x;
           max_sum=max(max_sum,a);
           a=max(a,0);
       }
        return max_sum;
    }
};