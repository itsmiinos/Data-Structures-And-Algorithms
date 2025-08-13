// Last updated: 8/13/2025, 8:20:55 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        int newData = node.next.val;
        ListNode newNext = node.next.next;

        node.val = newData;
        node.next = newNext;
    }
}