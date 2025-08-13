// Last updated: 8/13/2025, 8:19:13 PM
class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        
        for (String op : operations) {
            if (op.equals("+")) {
                stack.push(stack.peek() + stack.get(stack.size() - 2));
            } else if (op.equals("D")) {           
                stack.push(2 * stack.peek());    
            } else if (op.equals("C")) {        
                stack.pop();                    
            } else {          
                stack.push(Integer.parseInt(op));           
            }
        }
        
        int sum = 0;   
        for (int score : stack) {
            sum += score;
        }
        
        return sum;
    }
}