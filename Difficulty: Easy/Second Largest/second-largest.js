//{ Driver Code Starts
// Initial Template for javascript

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split("\n").map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        const arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        let ans = obj.getSecondLargest(arr);
        console.log(ans);
        console.log("~");
    }
}

// } Driver Code Ends

// } Driver Code Ends


// User function Template for javascript

class Solution {
    // Function returns the second largest element
    getSecondLargest(arr) {
        // Code Here
        let largest = arr[0];
        let secondLargest = arr[0];
        for(let i =0; i<arr.length ; i++){
            if(largest<arr[i]){
                secondLargest = largest;
                largest = arr[i];
            }
            else if(arr[i]>secondLargest && arr[i]<largest){
                secondLargest = arr[i];
            }
            else if(arr[i]<secondLargest && secondLargest===largest){
                secondLargest = arr[i];
            }
        }
        if(largest === secondLargest){
            return -1;
        }
        return secondLargest;
    }
}