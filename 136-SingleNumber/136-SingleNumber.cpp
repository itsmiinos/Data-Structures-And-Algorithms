// Last updated: 8/13/2025, 8:22:42 PM
class Solution {
public:
    int singleNumber(vector<int>& nums) {       
        
        int num = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            num ^= nums[i];  
    }
    return num;
}
        
    

};