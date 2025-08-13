// Last updated: 8/13/2025, 8:20:15 PM
class NumMatrix {

    int[][] matrix;

    public NumMatrix(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        this.matrix = matrix;

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(j==0){
                    matrix[i][j] = matrix[i][j];
                }
                else{
                    matrix[i][j] = matrix[i][j-1] + matrix[i][j];
                }
            }
        }

        for(int j=0;j<m;j++){
            for(int i=1;i<n;i++){
                matrix[i][j] = matrix[i][j] + matrix[i-1][j];
            }
        }

        //prefix sum created;
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int ans = matrix[row2][col2];

        if(row1>0){
            ans = ans - matrix[row1-1][col2];
        }
        if(col1 >0){
            ans = ans - matrix[row2][col1-1];
        }
        if(row1>0 && col1>0){
            ans = ans + matrix[row1-1][col1-1];
        }

        return ans;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */