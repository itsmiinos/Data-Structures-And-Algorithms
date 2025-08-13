// Last updated: 8/13/2025, 8:20:41 PM
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n=nums.size();
        vector<int> answer;
        int s=0;;
        for(int x:nums){
            if(x!=0){
                nums[s]=x;
                s++;
            }
                
        }
        for(int i=s;i<n;i++)
            nums[i]=0;
            
                
        }
    
    
};