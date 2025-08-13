// Last updated: 8/13/2025, 8:23:17 PM
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
    public ListNode deleteDuplicates(ListNode head) {
        HashSet<Integer> map = new HashSet();
        ListNode curr = head;
        ListNode prev = null;
        while(curr!=null){
            if(map.contains(curr.val)){
                curr = curr.next;
                prev.next = curr;
            }
            else{
                map.add(curr.val);
                prev = curr;
                curr = curr.next;
            }
        }
        return head;
    }
}