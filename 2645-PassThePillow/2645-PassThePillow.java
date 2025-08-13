// Last updated: 8/13/2025, 8:15:44 PM
class Solution {
    public int passThePillow(int n, int time) {
        int i = time / (n-1);
        if(i%2==0){
            return time%(n-1) + 1;
        }
        else{
            return n-time%(n-1);
        }
    }
}