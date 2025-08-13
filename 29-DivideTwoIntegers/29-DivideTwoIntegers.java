// Last updated: 8/13/2025, 8:24:13 PM
class Solution {
    public int divide(int dividend, int divisor) {
        int sign = 1;
        if(dividend<0){
            sign = sign * -1;
        }
        if(divisor<0){
            sign = sign * -1;
        }

        long a = dividend;
        long b = divisor;

        a = Math.abs(a);
        b = Math.abs(b);

        long res = 0;

        long t = 0;
        for (int x = 31; x >= 0; x--){
            if ((t + (b << x)) <= a) {
                res += ((long)1 << x);
                t += b << x;
            }
        }  

        System.out.println(res);
        if(sign < 0){
            res = -res;
        }

        
        if(res > Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }else if(res < Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }else{
            return (int)res;
        }       
    }

}