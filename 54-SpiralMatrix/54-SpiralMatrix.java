// Last updated: 8/13/2025, 8:23:40 PM
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList();
        int n = matrix.length;
        int m = matrix[0].length;

        int i = 0;
        int j = 0;
        int rowSteps = n-1;
        int colSteps = m-1;

        while(rowSteps >=1 && colSteps>=1){
            for(int k=0;k<colSteps;k++){
                ans.add(matrix[i][j]);
                j++;
            }
            for(int k=0;k<rowSteps;k++){
                ans.add(matrix[i][j]);
                i++;
            }
            for(int k = colSteps;k >= 1;k--){
            ans.add(matrix[i][j]);
            j--;
            
        }

        for(int k = rowSteps;k >= 1;k--){
            ans.add(matrix[i][j]);
            i--;
            
        }

            rowSteps = rowSteps -2;
            colSteps = colSteps -2;
            i++;
            j++;
        }

        if(rowSteps == 0){
            for(int k=0;k<colSteps+1;k++){
                ans.add(matrix[i][j]);
                j++;
            }
        }
        else if(colSteps==0){
            for(int k=0;k<rowSteps+1;k++){
                ans.add(matrix[i][j]);
                i++;
            }
        }
        return ans;
    }
}