// Last updated: 8/13/2025, 8:23:26 PM
class Solution {
    public int[] plusOne(int[] digits) {
        int [] plus = new int[digits.length+1];
        if(digits[digits.length-1]<9){
            digits[digits.length-1] = digits[digits.length-1] +1;
            return digits;
        }
        else{
            for(int i=digits.length-1;i>=0;i--){
                if(digits[i]==9){
                    digits[i] = 0;
                }
                else{
                    digits[i] = digits[i] +1;
                    return digits;
                }
            }
            for(int i=digits.length;i>0;i--){
                plus[i] = digits[i-1];
            }
            plus[0] = 1;
        }
        return plus;
    }
}