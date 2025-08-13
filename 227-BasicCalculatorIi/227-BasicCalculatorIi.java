// Last updated: 8/13/2025, 8:21:08 PM
class Solution {
    public int calculate(String s) {
        Stack<Integer> operand = new Stack();
        Stack<Character> operator = new Stack();
        int i = 0;
        while(i<s.length()){
            char c = s.charAt(i);
            if(c>='0' && c<='9'){
                int num = 0;
                while(i<s.length() && s.charAt(i)>='0' && s.charAt(i)<='9'){
                    num = num *10 + (s.charAt(i) - '0');
                    i++;
                }
                i--;
                operand.add(num);
            }
            else if(c=='+' || c=='-' || c=='/' || c=='*'){
                while(operator.size()>0 && precedence(c)<=precedence(operator.peek())){
                    int val2 = operand.pop();
                    int val1 = operand.pop();
                    char op = operator.pop();
                    int a = calculation(val1,val2,op);
                    operand.push(a);
                }
                operator.push(c);
            }
            i++;
        }

        while(operator.size()>0){
            int val2 = operand.pop();
            int val1 = operand.pop();
            char op = operator.pop();
            int a = calculation(val1,val2,op);
            operand.push(a);
        }
        return operand.pop();
    }

    public int calculation(int a, int b , char c){
        if(c=='+'){
            return a+b;
        }
        else if(c=='-'){
            return a-b;
        }
        else if(c=='*'){
            return a*b;
        }
        return a/b;
    }

    public int precedence(char c){
        if(c=='+' || c=='-'){
            return 0;
        }
        return 1;
    }
}