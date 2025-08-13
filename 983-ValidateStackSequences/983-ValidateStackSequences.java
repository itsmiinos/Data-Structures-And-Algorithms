// Last updated: 8/13/2025, 8:18:16 PM
class Solution {
    Stack<Integer> stack = new Stack();
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int i = 0;
        int j= 0;
        while(i<pushed.length && j<popped.length){
            if(stack.size()==0){
                stack.push(pushed[i]);
                i++;
            }
            else{
                if(stack.peek()==popped[j]){
                    stack.pop();
                    j++;
                }
                else{
                    stack.push(pushed[i]);
                    i++;
                }
            }
        }
        if(i==pushed.length){
            while(j<popped.length){
                if(stack.peek()==popped[j]){
                    stack.pop();
                    j++;
                }
                else{
                    return false;
                }
            }
        }
        if(stack.size()==0){
            return true;
        }
        return false;
    }

}