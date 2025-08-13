// Last updated: 8/13/2025, 8:19:14 PM
class Solution {
    public int maximumSwap(int num) {
        char[] c = Integer.toString(num).toCharArray();
        int[] last = new int[10];
        
        // Record the last occurrence of each digit (0 through 9)
        for (int i = 0; i < c.length; i++) {
            last[c[i] - '0'] = i;
        }
        
        // Traverse the number and try to find a larger digit to swap
        for (int i = 0; i < c.length; i++) {
            for (int d = 9; d > c[i] - '0'; d--) {
                if (last[d] > i) {
                    // Swap the current digit with the larger digit found later
                    char temp = c[i];
                    c[i] = c[last[d]];
                    c[last[d]] = temp;
                    
                    // Convert back to integer and return
                    return Integer.parseInt(new String(c));
                }
            }
        }
        
        return num; // If no beneficial swap found, return the original number
    }
}
