// Last updated: 8/13/2025, 8:24:52 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        vector<int>::iterator i;
        vector<int>::iterator j;
        for(i=nums.begin();i<nums.end();i++)
        {   
            for(j=i+1;j<nums.end();j++){
                if(*i+*j==target){
                    ans.push_back(i - nums.begin());
                    ans.push_back(j - nums.begin());
                    //return ans;
                }
                else if(i==j)
                    //return ans;
                    break;
            }  
        }
        return ans;
    }
};
