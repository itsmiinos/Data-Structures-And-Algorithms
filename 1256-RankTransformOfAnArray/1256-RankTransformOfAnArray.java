// Last updated: 8/13/2025, 8:17:50 PM
class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int n = arr.length;
        HashMap<Integer,Integer> h = new HashMap();
        int[] sortedArray = Arrays.stream(arr).distinct().sorted().toArray();
        for(int i=0;i<sortedArray.length;i++){
            h.put(sortedArray[i],i+1);
        }

        for(int i=0;i<n;i++){
            arr[i] = h.get(arr[i]);
        }

        return arr;
    }
}