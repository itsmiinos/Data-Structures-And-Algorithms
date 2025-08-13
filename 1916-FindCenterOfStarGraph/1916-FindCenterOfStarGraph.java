// Last updated: 8/13/2025, 8:16:52 PM
class Solution {
    public int findCenter(int[][] e) {
        return e[0][0] == e[1][0] || e[0][0] == e[1][1] ? e[0][0] : e[0][1];
    }
}