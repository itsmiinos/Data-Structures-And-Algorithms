// Last updated: 8/13/2025, 8:20:03 PM
class Solution {
    public boolean isPowerOfFour(int n) {
        if(n==1){
            return true;
        }
        else if(n%4!=0 || n==0){
            return false;
        }
        else{
            return isPowerOfFour(n/4);
        }
    }
}