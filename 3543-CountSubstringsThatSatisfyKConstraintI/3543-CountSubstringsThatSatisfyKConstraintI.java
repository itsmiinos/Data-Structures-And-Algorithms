// Last updated: 8/13/2025, 8:15:08 PM
class Solution {
    public int countKConstraintSubstrings(String s, int k) {
        int count=0;
        for(int i=0;i<s.length();i++){
            for(int j=i+1;j<=s.length();j++){
                String temp = s.substring(i,j);
                if(countK(temp,k)==true){
                    count++;
                }
            }
        }
        return count;
    }

    public boolean countK(String s, int k){
        int countOne = 0;
        int countZero = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='1'){
                countOne++;
            }
            else{
                countZero++;
            }
        }

        if(countOne <= k || countZero<= k){
            return true;
        }
        return false;
    }
}