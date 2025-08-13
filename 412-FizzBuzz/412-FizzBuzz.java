// Last updated: 8/13/2025, 8:19:49 PM
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> s = new ArrayList<>();
        int i=1;
        while(i<=n){
            if(i%3==0 && i%5==0){
                s.add("FizzBuzz");
            }
            else if(i%3==0){
                s.add("Fizz");
            }
            else if(i%5==0){
                s.add("Buzz");
            }
            else{
                s.add(i+"");
            }
            i++;
        }
        return s;
        
    }
}