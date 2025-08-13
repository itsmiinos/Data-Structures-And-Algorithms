// Last updated: 8/13/2025, 8:19:16 PM
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
    Stack<Integer> stack = new Stack<>();
    int n = asteroids.length;
    int i=0;
    while(i < n){
        if(asteroids[i]<0){
            if(stack.size()==0 || stack.peek()<0){
                stack.push(asteroids[i]);
                i++;
            }
            else if(stack.peek()>Math.abs(asteroids[i])){
                i++;
            }
            else if(stack.peek()<Math.abs(asteroids[i])){
                stack.pop();
            }
            else{
                stack.pop();
                i++;
            }
        }
        else{
            stack.push(asteroids[i]);
            i++;
        }
}
int[] ans = new int[stack.size()];
for(int j=ans.length-1;j>=0;j--){
ans[j] = stack.pop();


}
return ans;
}

}