// Last updated: 8/13/2025, 8:15:17 PM
class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        int nq = queries.length;
        int a[] = new int[n];
        int counter=0;

        for(int i=0;i<n-1;i++){
            boolean flag1 = nums[i]%2==0;
            boolean flag2 = nums[i+1]%2==0;
            if(flag1^flag2==false)counter++;
            a[i+1] = counter;
        }

        boolean res[] = new boolean[nq];

        for(int i=0;i<nq;i++){
            if(a[queries[i][1]]-a[queries[i][0]]==0)res[i]=true;
        }

        return res;


    }
}