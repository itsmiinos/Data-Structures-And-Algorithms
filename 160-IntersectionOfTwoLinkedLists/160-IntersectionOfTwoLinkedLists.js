// Last updated: 8/13/2025, 8:21:47 PM
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    let a = headA;
    let b = headB;
    while(a!==b){
        a = !a ? headB : a.next;
        b = !b ? headA : b.next;
    }
    return a;
};