// Last updated: 8/13/2025, 8:23:13 PM
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int totalNum = (1<<nums.length);
        System.out.print(totalNum);
        List<List<Integer>> ans = new ArrayList();
        for(int i=0;i<totalNum;i++){
            List<Integer> temp = new ArrayList();
            for(int j=0;j<nums.length;j++){
                if(checkBit(i,j)==true){
                    temp.add(nums[j]);
                }
            }
            ans.add(temp);
        }
        return ans;
    }

    public boolean checkBit(int n, int i){
        if((n&(1<<i))==0){
            return false;
        }
        return true;
    }
}