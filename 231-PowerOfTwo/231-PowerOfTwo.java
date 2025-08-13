// Last updated: 8/13/2025, 8:21:02 PM
class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n==1){
            return true;
        }
        else if(n%2!=0 || n==0){
            return false;
        }
        else{
            return isPowerOfTwo(n/2);
        }
    }
}