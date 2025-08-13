// Last updated: 8/13/2025, 8:19:43 PM
class Solution {
    public int[] nextGreaterElement(int[] a, int[] b) {
    int[] c = new int [a.length];
    int counter =0;
    int flag;
    for(int i=0;i<a.length;i++){
        flag = 0;
      for(int j=0;j<b.length;j++){
        if(a[i]==b[j]){
          counter = j;
          while(counter<b.length){
            if(b[counter]>b[j]){
              c[i] = b[counter];
              flag = 1;
              break;
            }
            counter++;
          }
          if(flag ==0){
            c[i] = -1;
          }
        }
      }
    }
  return c;
  }
}