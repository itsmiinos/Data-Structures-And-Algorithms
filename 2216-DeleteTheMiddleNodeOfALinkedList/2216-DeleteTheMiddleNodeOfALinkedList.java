// Last updated: 8/13/2025, 8:16:28 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if(head.next==null){
            return null;
        }
        ListNode h1 = head;
        ListNode h2 = head;
        ListNode prev = null;
        int i =0;
        while(h2!=null && h2.next!=null){
            prev = h1;
            h1 = h1.next;
            h2 = h2.next.next;
            i++;
        }
        ListNode t = head;
        for(int j=0;j<i-1;j++){
            t = t.next;
        }
        t.next = h1.next;
        
        return head;
        
    }
}