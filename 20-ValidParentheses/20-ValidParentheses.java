// Last updated: 8/13/2025, 8:24:28 PM
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(stack.isEmpty() || ch == '(' || ch == '[' || ch == '{'){
                stack.push(ch);
            }else{
                if((ch == ')' && stack.peek() == '(') || (ch == ']' && stack.peek() == '[') || (ch == '}' && stack.peek() == '{')){
                 stack.pop();
                }
                else{
                return false;
            }
            }

        }
        if(stack.size()!=0){
            return false;
        }
        else{
            return true;
        }
    }
}