// Last updated: 8/13/2025, 8:20:26 PM
class Solution {
    public int numSquares(int n) {
        int[]dp = new int[n+1];
        Arrays.fill(dp,-1);
        return numSquaresHelper(n,dp);
    }

    public int numSquaresHelper(int n,int[]dp){
        int minSquare = Integer.MAX_VALUE;
        if(n==0||n==1)return n;
        if(dp[n]!=-1)return dp[n];
        for(int i=1;i*i<=n;i++){
            int temp = numSquaresHelper(n-i*i,dp);
            minSquare = Math.min(minSquare,temp);
        }
        dp[n] = minSquare+1;
        return minSquare+1;
    }
}