// Last updated: 8/13/2025, 8:23:38 PM
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for(int i=0;i<m;i++){
            Arrays.fill(dp[i],-1);
        }

        return uniquePathsHelper(m-1,n-1,dp);
    }

    public int uniquePathsHelper(int m,int n,int[][]dp){
        if(m<0 || n<0)return 0;
        if(m==0&&n==0)return 1;
        if(dp[m][n]!=-1)return dp[m][n];
        int down = uniquePathsHelper(m-1,n,dp);
        int right = uniquePathsHelper(m,n-1,dp);
        dp[m][n] = down+right;
        return down+right;
    }
}