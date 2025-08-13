// Last updated: 8/13/2025, 8:23:07 PM
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> s = new Stack();
        int ans = Integer.MIN_VALUE;
        int nsel[] = new int[heights.length];
        int nser[] = new int[heights.length];
        int n = heights.length;

        for(int i=0;i<n;i++){
            while(s.size()>0 && heights[i]<heights[s.peek()]){
                int temp = s.pop();
                nser[temp] = i;
            }
            s.add(i);
        }
        while(s.size()>0){
            int temp = s.pop();
            nser[temp] = heights.length;
        }

        for(int i=n-1;i>=0;i--){
            while(s.size()>0 && heights[i]<heights[s.peek()]){
                int temp = s.pop();
                nsel[temp] = i;
            }
            s.add(i);
        }

        while(s.size()>0){
            int temp = s.pop();
            nsel[temp] = -1;
        }

        for(int i=0;i<n;i++){
            int val1 = nser[i] - 1;
            int val2 = nsel[i] + 1;
            int wd = val1 - val2 +1;
            int h = heights[i];
            int area = wd*h;
            ans = Math.max(area,ans);
        }

        return ans;
    }
}