//{ Driver Code Starts
// Initial Template for JavaScript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

function printList(head) {
    let current = head;
    let s = '';
    while (current !== null) {
        s += current.data + " ";
        current = current.next;
    }
    console.log(s.trim());
}

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let inputArr = readLine().split(' ').map(x => parseInt(x));
        let n = inputArr.length;
        let arr = new Array(n);
        for (let i = 0; i < n; i++) {
            arr[i] = inputArr[i];
        }
        let obj = new Solution();
        let head = obj.construct(arr);
        printList(head);
    }
}

// } Driver Code Ends


// User function Template for javascript
/**
 * class Node{
 *     constructor(data){
 *         this.data = data;
 *         this.next = null;
 *     }
 * }
 */

class Solution {
    // Function to construct linked list from given array.
    construct(arr) {
        // your code here
        let head = new Node(-1);
        let curr = head;
        for(let i=0;i<arr.length;i++){
            let tempNode = new Node(arr[i]);
            curr.next = tempNode;
            curr = curr.next;
        }
        return head.next;
    }
}