// Last updated: 8/13/2025, 8:17:33 PM
class Solution {
    public int subtractProductAndSum(int n) {
        int sum = 0;
        int multiply = 1;
        while(n>0){
            int lastDigit = n%10;
            sum = sum+lastDigit;
            multiply = multiply*lastDigit;
            n=n/10;
        }
        return multiply-sum;
    }
}