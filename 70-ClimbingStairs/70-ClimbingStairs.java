// Last updated: 8/13/2025, 8:23:28 PM
class Solution {
    public int climbStairs(int n) {
        int []dp = new int[n+1];
        for(int i=0;i<n+1;i++){
            dp[i] = -1;
        }
        return climbStairsHelper(n,dp);
    }

    public int climbStairsHelper(int n,int[]dp){
        if(n==1||n==2){
            return n;
        }
        if(dp[n]!=-1)return dp[n];
        int x = climbStairsHelper(n-1,dp);
        int y = climbStairsHelper(n-2,dp);
        dp[n] = x+y;
        return x+y;
    }
}