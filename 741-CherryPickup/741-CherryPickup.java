// Last updated: 8/13/2025, 8:19:07 PM
class Solution {
    public int cherryPickup(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][][] dp = new int[n][m][n];
        int ans = cherryPickupHelper(0,0,0,grid,dp);
        if(ans<0){
            return 0;
        }
        else{
            return ans;
        }
    }

    public int cherryPickupHelper(int n1,int m1, int n2, int[][]grid, int[][][]dp){
        int m2 = n1+m1-n2;

        if(n1>=grid.length || n2>=grid.length || m1>=grid[0].length || m2>=grid[0].length || grid[n1][m1]==-1 || grid[n2][m2]==-1){
            return Integer.MIN_VALUE;
        }

        if(n1==grid.length-1 && n2==grid.length-1 && m1==grid[0].length-1 && m2==grid[0].length-1){
            return grid[n1][m1];
        }

        if(dp[n1][m1][n2]!=0){
            return dp[n1][m1][n2];
        }


        int rightRight = cherryPickupHelper(n1,m1+1,n2,grid,dp);
        int rightDown = cherryPickupHelper(n1,m1+1,n2+1,grid,dp);
        int downRight = cherryPickupHelper(n1+1,m1,n2,grid,dp);
        int downDown = cherryPickupHelper(n1+1,m1,n2+1,grid,dp);

        int max = Math.max(Math.max(rightRight,rightDown),Math.max(downRight,downDown));

        int counter = 0;

        if(n1==n2 && m1==m2){
            counter = grid[n1][m1];
        }
        else{
            counter = grid[n1][m1] + grid[n2][m2];
        }

        if(max==Integer.MIN_VALUE){
            dp[n1][m1][n2] = Integer.MIN_VALUE;
            return max;
        }

        else{
            dp[n1][m1][n2] = max+counter;
            return max+counter;
        }
    }
}