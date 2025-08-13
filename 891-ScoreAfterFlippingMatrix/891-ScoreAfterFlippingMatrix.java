// Last updated: 8/13/2025, 8:18:38 PM
class Solution {
    public int matrixScore(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        for(int i=0;i<n;i++){
            if(grid[i][0]!=1){
                for(int j=0;j<m;j++){
                    grid[i][j]^=1;
                }
            }
        }
        for(int j=1;j<m;j++){
            int count = 0;
            for(int i=0;i<n;i++){
                if(grid[i][j]==1){
                    count+=grid[i][j];
                }
            }
            if(count<n-count){
                for(int i=0;i<n;i++){
                    grid[i][j]^=1;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                System.out.print(grid[i][j]+" ");
            }
            System.out.println();
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ans += grid[i][j] * (1 << (m - 1 - j));
            }
        }
        return ans;
        
        // return 0;
    }
}