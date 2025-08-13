// Last updated: 8/13/2025, 8:21:32 PM
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
    public ListNode removeElements(ListNode head, int val) {
        ListNode t1 = head;
        ListNode prev = head;
        while(head!=null && head.val==val){
            head = head.next;
        }
        if(head==null){
            return head;
        }
        while(t1!=null){
            if(t1.val==val){
                prev.next = t1.next;
                t1 = t1.next;
            }
            else{
                prev = t1;
                t1 = t1.next; 
            }
        }
        return head;
    }
}