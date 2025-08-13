// Last updated: 8/13/2025, 8:23:35 PM
class Solution {
    public int minPathSum(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int [][]dp = new int[n][m];
        for(int i=0;i<n;i++){
            Arrays.fill(dp[i],-1);
        }
        return minPathSumHelper(n-1,m-1,grid,dp);
    }

    public int minPathSumHelper(int n,int m,int[][] grid,int[][] dp){
        if(n<0 || m<0){
            return Integer.MAX_VALUE;
        }
        if(n==0 && m==0){
            return grid[n][m];
        }
        if(dp[n][m]!=-1){
            return dp[n][m];
        }


        int right = minPathSumHelper(n,m-1,grid,dp);
        int down = minPathSumHelper(n-1,m,grid,dp);

        int minSum = Math.min(right,down) + grid[n][m];
        dp[n][m] = minSum;
        return minSum;

    }
}