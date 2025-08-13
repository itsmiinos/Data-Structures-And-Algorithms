// Last updated: 8/13/2025, 8:23:46 PM
class Solution {
    public double myPow(double x, int n) {
        if(n<0) return myUtils(1/x,Math.abs((long)n));
        else return myUtils(x,n);
    }

    public double myUtils(double x , long n){
        if(n==0){
            return 1.0;
        }
        if(x==0){
            return 0.0;
        }
        if(n%2==0){
            return myUtils(x*x,n/2);
        }
        else{
            return x * myUtils(x,n-1);
        }
    }
}