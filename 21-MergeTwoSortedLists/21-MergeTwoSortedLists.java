// Last updated: 8/13/2025, 8:24:31 PM
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode temp = new ListNode();
        ListNode ans = new ListNode();
        if(list1==null || list2==null){
            if(list1!=null){
                ans = list1;
            }
            else{   
                ans = list2;
            }
            return ans;
        }
        if(list1.val<list2.val){
            ans = list1;
            temp = list1;
            list1 = list1.next;
        }
        else{
            ans = list2;
            temp = list2;
            list2 = list2.next;
        }

        while(list1!=null && list2!=null){
            if(list1.val<list2.val){
                temp.next = list1;
                temp = temp.next;
                list1 = list1.next;
            }
            else{
                temp.next = list2;
                temp = temp.next;
                list2 = list2.next;
            }
        }
        if(list1!=null){
            temp.next = list1;
        }
        else{
            temp.next = list2;
        }

        return ans;
    }
}