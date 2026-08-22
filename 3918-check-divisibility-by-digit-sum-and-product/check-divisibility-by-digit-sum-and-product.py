class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_of_digits = 0
        product_of_digits = 1

        temp1 = n
        while temp1 > 0 :
            r = temp1%10
            sum_of_digits += r
            temp1 = temp1//10
        
        temp2 = n
        while temp2 > 0 :
            r = temp2%10
            product_of_digits *= r
            temp2 = temp2//10
        
        return n % (sum_of_digits + product_of_digits) == 0