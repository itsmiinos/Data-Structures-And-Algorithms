// Last updated: 8/13/2025, 8:18:13 PM
class Solution {
    public int fib(int n) {
        if(n==1 || n==0){
            return n;
        }
        int a = fib(n-1);
        int b = fib(n-2);
        return a+b;
    }
}