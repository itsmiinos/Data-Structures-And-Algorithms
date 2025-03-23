//{ Driver Code Starts
// Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

/* Function to print an array */
function printArray(arr, size) {
    let i;
    let s = '';
    for (i = 0; i < size; i++) {
        s += arr[i] + " ";
    }
    console.log(s);
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let a = readLine().split(' ').map(x => parseInt(x, 10));
        let b = readLine().split(' ').map(x => parseInt(x, 10));
        let obj = new Solution();
        let res = obj.findUnion(a, b);
        printArray(res, res.length);

        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} a
 * @param {number[]} b
 * @returns {number[]}
 */

class Solution {
    // Function to return a list containing the union of the two arrays.
    findUnion(a, b) {
        // your code here
        let arr = new Array();
        let p1 = 0;
        let p2 = 0;
        let previous = -1;
        while(p1<a.length && p2<b.length){
            if(a[p1]<b[p2]){
                if(previous===-1 || arr[previous]!==a[p1]){
                    arr[previous+1] = a[p1];
                    previous++;
                }
                else{
                    p1++;
                }
            }
            else{
                if(previous===-1 || arr[previous]!==b[p2]){
                    arr[previous+1] = b[p2];
                    previous++;
                }
                else{
                    p2++;
                }
            }
        }
        while(p1<a.length){
            if(previous===-1 || arr[previous]!==a[p1]){
                    arr[previous+1] = a[p1];
                    previous++;
                }
                else{
                    p1++;
                }
        }
        while(p2<b.length){
            if(previous===-1 || arr[previous]!==b[p2]){
                    arr[previous+1] = b[p2];
                    previous++;
                }
                else{
                    p2++;
                }
        }
        return arr;
    }
}