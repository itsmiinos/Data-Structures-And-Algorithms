// Last updated: 8/13/2025, 8:16:54 PM
class Solution {
    public String largestOddNumber(String num) {
        int l = num.length();
        int oddIndex = -1;
        String ans = "";
        for(int i = l-1 ; i>=0;i--){
            int number = num.charAt(i) - '0';
            if(number%2!=0){
                 return num.substring(0 , i+1);
            }
        }
        return "";
    }
}